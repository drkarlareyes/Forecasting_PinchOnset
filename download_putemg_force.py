"""Download the putEMG-Force recordings used by putemg_force.ipynb.

putEMG-Force, Biomedical Engineering group, Poznan University of Technology
(https://biolab.put.poznan.pl/putemg-dataset/), CC BY-NC 4.0.
All force trials of the 44 participants (HDF5, about 20 GB) and the participants table.

    python download_putemg_force.py                # into data/putemg_force
    PUTEMG_FORCE=/path/to/folder python download_putemg_force.py

Safe to re-run: files already downloaded are skipped, and a file only gets its
final name once it has downloaded completely.
"""
import os
import sys
import urllib.parse
import urllib.request

SHARE = os.environ.get("PUTEMG_URL", "https://chmura.put.poznan.pl/s/45NY5snj0U4tgQz/download")
OUT = os.environ.get("PUTEMG_FORCE", os.path.join("data", "putemg_force"))


def url(folder, name):
    return f"{SHARE}?{urllib.parse.urlencode({'path': '/' + folder, 'files': name})}"


def fetch(folder, name):
    out = os.path.join(OUT, name)
    if os.path.exists(out):
        return True
    try:
        with urllib.request.urlopen(url(folder, name), timeout=60) as r, open(out + ".part", "wb") as f:
            size = int(r.headers.get("Content-Length", -1))
            got = 0
            while True:
                b = r.read(1 << 20)
                if not b:
                    break
                f.write(b)
                got += len(b)
        if size >= 0 and got != size:
            raise IOError(f"incomplete ({got} of {size} bytes)")
        os.replace(out + ".part", out)
        return True
    except Exception as e:
        print(f"  failed: {e}")
        if os.path.exists(out + ".part"):
            os.remove(out + ".part")
        return False


def main():
    os.makedirs(OUT, exist_ok=True)
    with urllib.request.urlopen(url("", "records.txt"), timeout=60) as r:
        records = [l.strip() for l in r.read().decode("utf-8").splitlines() if l.strip().startswith("emg_force-")]
    failed = [] if fetch("", "putEMG-participants.csv") else ["putEMG-participants.csv"]
    for i, rec in enumerate(records, 1):
        print(f"[{i}/{len(records)}] {rec}.hdf5", flush=True)
        if not fetch("Data-HDF5", rec + ".hdf5"):
            failed.append(rec + ".hdf5")
    if failed:
        print(f"{len(failed)} files failed, run the script again.")
        sys.exit(1)
    print(f"Done: {len(records)} recordings in {OUT}")


if __name__ == "__main__":
    main()
