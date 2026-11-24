#!/usr/bin/env python3
"""news-image-20261124 entry: write the day's front page to /output/entry.png.

The image shipped beside this file sums up Tuesday 24 November 2026 in one
page: the lead story plus five more from around the world. Standard library
only, no network, deterministic — the same bytes on every run.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
source = HERE / "entry.png"
if not source.is_file():
    raise SystemExit("entry.png is missing beside main.py")
target = OUT / "entry.png"
shutil.copyfile(source, target)
if target.stat().st_size != source.stat().st_size:
    raise SystemExit("entry.png did not copy completely")
