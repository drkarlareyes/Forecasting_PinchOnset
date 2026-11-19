"""Download the Hyser files used by hyser.ipynb and hyser_multisubject.ipynb (PhysioNet hd-semg 2.0.0).

Random task, trials 1 and 2 (raw HD-sEMG and finger force), sessions 1 and 2 of subjects 1 to 20: about 2 GB.
Files go to data/hyser/subjectXX_sessionY/. Files already downloaded are skipped, so the script can be run again.

    python download_hyser.py                # all 20 subjects
    python download_hyser.py 1 2 3          # some subjects only
"""
import os
import sys
import urllib.request

BASE = os.environ.get("HYSER_URL", "https://physionet.org/files/hd-semg/2.0.0/random_dataset")
OUT = os.environ.get("HYSER_RANDOM", os.path.join("data", "hyser"))


def get(url, path):
    if os.path.exists(path):
        return True
    try:
        with urllib.request.urlopen(url, timeout=120) as r, open(path + ".part", "wb") as f:
            while True:
                chunk = r.read(1 << 20)
                if not chunk:
                    break
                f.write(chunk)
        os.replace(path + ".part", path)
        return True
    except Exception as e:
        print(f"  failed: {url} ({e})")
        if os.path.exists(path + ".part"):
            os.remove(path + ".part")
        return False


def main(subjects):
    failed = 0
    for s in subjects:
        for session in (1, 2):
            sub = f"subject{s:02d}_session{session}"
            os.makedirs(os.path.join(OUT, sub), exist_ok=True)
            print(sub)
            for n in (1, 2):
                for kind in ("raw", "force"):
                    for ext in ("hea", "dat"):
                        name = f"random_{kind}_sample{n}.{ext}"
                        failed += not get(f"{BASE}/{sub}/{name}", os.path.join(OUT, sub, name))
    print("done" if not failed else f"done, {failed} files failed: run the script again")


if __name__ == "__main__":
    main([int(a) for a in sys.argv[1:]] or range(1, 21))
