#!/usr/bin/env bash
# Publish the DSA site to GitHub Pages: rebuild, commit Preparation/DSA, push it to the dsa-site remote.
set -euo pipefail
cd "$(dirname "$0")"
python3 build.py
cd "$(git rev-parse --show-toplevel)"
git add Preparation/DSA
git diff --cached --quiet || git commit -q -m "DSA: update site"
git subtree push --prefix Preparation/DSA dsa-site main
echo "Pushed. GitHub Pages updates in about a minute."
