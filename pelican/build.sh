#!/usr/bin/env bash
# Build the Pelican site into pelican/output/.
# Run from any directory — the script changes into the pelican/ folder first.
set -euo pipefail

cd "$(dirname "$0")"

echo "Installing Python dependencies..."
python3 -m pip install -q -r requirements.txt

echo "Building site..."
pelican content -s pelicanconf.py -o output

echo "Done — site built in pelican/output/"
