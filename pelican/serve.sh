#!/usr/bin/env bash
# Build and serve the Pelican site locally with live autoreload.
# Serves at http://localhost:8000
# Run from any directory — the script changes into the pelican/ folder first.
set -euo pipefail

cd "$(dirname "$0")"

echo "Installing Python dependencies..."
python -m pip install -q -r requirements.txt

echo "Building and serving at http://localhost:8000 (autoreload enabled)..."
pelican content -s pelicanconf.py -o output --autoreload --listen --port 8000
