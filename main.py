#!/usr/bin/env python3
"""Entry program for make.fun's news-image-20261124.

The repository holds entry.png, the front page drawn by render.py from the
sources listed in SOURCES.md. This program copies that file to
/output/entry.png unchanged, so the grader's two runs produce identical
bytes and nothing depends on network access or local fonts.
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "entry.png"


def write_entry() -> Path:
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.png"
    except OSError:
        target = Path.cwd() / "output" / "entry.png"
        target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, target)
    return target


if __name__ == "__main__":
    write_entry()
