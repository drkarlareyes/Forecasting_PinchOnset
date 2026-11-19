"""Download the WAY-EEG-GAL files used by way_eeg_gal.ipynb.

WAY-EEG-GAL (Luciw, Jarocka and Edin 2014, Scientific Data 1:140047), figshare collection
https://doi.org/10.6084/m9.figshare.988376, CC BY 4.0. One zip file per participant, 12 files, 10.3 GB.

    python download_way_eeg_gal.py                 # into data/way_eeg_gal
    WAY_EEG_GAL=/path/to/folder python download_way_eeg_gal.py

Safe to re-run: complete files are skipped, interrupted downloads resume, and every file is
checked against the size and MD5 published on figshare before it gets its final name.
"""
import hashlib
import os
import sys
import urllib.request

BASE = "https://ndownloader.figshare.com/files/"
OUT = os.environ.get("WAY_EEG_GAL", os.path.join("data", "way_eeg_gal"))
FILES = [  # name, figshare file id, size (bytes), MD5
    ("P1.zip", 3229301, 838738355, "db738ebf022abd6826879d9afee3202c"),
    ("P2.zip", 3229304, 949516152, "1bd75993ae538c35f8c403e4e5ff40e5"),
    ("P3.zip", 3229307, 743891763, "891bfca8516056201e5a214b2fde4558"),
    ("P4.zip", 3229310, 802120619, "b921d5e1d82151bf00fc041419ef22e9"),
    ("P5.zip", 3229313, 842392342, "2ef0bc0c9bc2840fd28190a6fc5e9602"),
    ("P6.zip", 3209486, 862474753, "5cf49ca627cbc3e8ef8e3c03a180c1d3"),
    ("P7.zip", 3209501, 1036731427, "125e2958872b3c06aeb3b729f282482a"),
    ("P8.zip", 3209504, 781620401, "56e39cfa3e7ea8361d51e8810fd65cb2"),
    ("P9.zip", 3209495, 832268248, "6e3eda3b36de5c1bbf09c5432258af79"),
    ("P10.zip", 3209492, 852411764, "4037a88eedc22bc6a3cbb786ab993ac2"),
    ("P11.zip", 3209498, 888190528, "45b7e844786b4707f5cd0dda42ecb63a"),
    ("P12.zip", 3209489, 908902695, "d8e1d2bfd8cf58ceff8d9d21a7114e85"),
]


def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def fetch(name, fid, size, digest):
    out = os.path.join(OUT, name)
    part = out + ".part"
    if os.path.exists(out) and os.path.getsize(out) == size and md5(out) == digest:
        print("  already complete")
        return True
    for attempt in range(3):
        have = os.path.getsize(part) if os.path.exists(part) else 0
        if have > size:
            os.remove(part)
            have = 0
        if have < size:
            req = urllib.request.Request(BASE + str(fid), headers={"Range": f"bytes={have}-"} if have else {})
            try:
                with urllib.request.urlopen(req, timeout=60) as r, open(part, "ab" if r.status == 206 else "wb") as f:
                    while True:
                        b = r.read(1 << 20)
                        if not b:
                            break
                        f.write(b)
            except Exception as e:
                print(f"  interrupted: {e}")
                continue
        if os.path.getsize(part) == size:
            if md5(part) == digest:
                os.replace(part, out)
                print("  done, checksum OK")
                return True
            print("  checksum does not match, downloading again")
            os.remove(part)
    return False


def main():
    os.makedirs(OUT, exist_ok=True)
    failed = []
    for i, (name, fid, size, digest) in enumerate(FILES, 1):
        print(f"[{i}/{len(FILES)}] {name} ({size / 1e9:.2f} GB)", flush=True)
        if not fetch(name, fid, size, digest):
            failed.append(name)
    if failed:
        print(f"{len(failed)} files failed ({', '.join(failed)}), run the script again.")
        sys.exit(1)
    print(f"Done: {len(FILES)} files in {OUT}")


if __name__ == "__main__":
    main()
