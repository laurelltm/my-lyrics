#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEFAULT_APP_REPO="${ROOT_DIR}/../opensongbook/open_songbook_3"
APP_REPO="${1:-${OPEN_SONGBOOK_APP_REPO:-${DEFAULT_APP_REPO}}}"
PAGES_BASE_PATH="${PAGES_BASE_PATH:-/my-lyrics/}"
APP_BASE_HREF="${PAGES_BASE_PATH%/}/web-demo/app/"
APP_OUTPUT_DIR="${ROOT_DIR}/web-demo/app"

if [[ ! -f "${APP_REPO}/pubspec.yaml" ]]; then
  echo "Flutter app repo not found: ${APP_REPO}" >&2
  echo "Pass the app path as the first argument or set OPEN_SONGBOOK_APP_REPO." >&2
  exit 1
fi

rm -rf "${APP_OUTPUT_DIR}"
mkdir -p "${APP_OUTPUT_DIR}"

(
  cd "${APP_REPO}"
  fvm flutter build web --base-href="${APP_BASE_HREF}"
)

cp -R "${APP_REPO}/build/web/." "${APP_OUTPUT_DIR}/"

cat <<EOF

Web demo app bundle copied to:
  ${APP_OUTPUT_DIR}

GitHub Pages URL after push:
  https://laurelltm.github.io/my-lyrics/web-demo/

Local preview with the GitHub Pages path:
  ./scripts/preview_web_demo.sh
EOF
