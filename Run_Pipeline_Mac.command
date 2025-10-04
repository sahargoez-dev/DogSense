#!/bin/bash
cd "$(dirname "$0")"
/usr/bin/python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python scripts/analyze_annotations.py
read -n 1 -s -r -p "Press any key to close..." 