"""news-image-01 entry #2: write the broadsheet image to the output directory.

Deterministic: the same bytes are written on every run.
No network, standard library only. The image is bundled with this
program (entry.png) and is copied verbatim to the output directory.
"""
import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Fail loudly on a truncated copy instead of submitting a broken image.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("entry.png copy incomplete")


if __name__ == "__main__":
    main()
    sys.exit(0)
