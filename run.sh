#!/usr/bin/env bash
set -e
source .venv/bin/activate || true
python scripts/analyze_annotations.py
