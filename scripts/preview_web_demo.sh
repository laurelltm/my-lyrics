#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PREVIEW_ROOT="${ROOT_DIR}/.local-pages-preview"
PORT="${PORT:-5179}"

rm -rf "${PREVIEW_ROOT}"
mkdir -p "${PREVIEW_ROOT}/my-lyrics"

rsync -a \
  --exclude ".git" \
  --exclude ".local-pages-preview" \
  "${ROOT_DIR}/" \
  "${PREVIEW_ROOT}/my-lyrics/"

cat <<EOF
Serving GitHub Pages-shaped preview at:
  http://127.0.0.1:${PORT}/my-lyrics/web-demo/

Press Ctrl-C to stop.
EOF

python3 -m http.server "${PORT}" --bind 127.0.0.1 --directory "${PREVIEW_ROOT}"
