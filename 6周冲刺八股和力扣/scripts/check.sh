#!/bin/sh
set -eu

cd "$(dirname "$0")/.."
python3 scripts/validate_vault.py
git diff --check
