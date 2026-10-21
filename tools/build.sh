#!/usr/bin/env bash
# Rebuild the API archive from Drupal 7 core.
# Usage: tools/build.sh [version]   (default 7.103, the final Drupal 7 release)
set -euo pipefail
VERSION="${1:-7.103}"
HERE="$(cd "$(dirname "$0")/.." && pwd)"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

git clone -q --depth 1 --branch "$VERSION" https://github.com/drupal/drupal "$WORK/drupal"

rm -rf "$HERE/source"
# Keep the hand-written api/INDEX.md; everything else in api/ is generated.
[ -d "$HERE/api" ] && find "$HERE/api" -mindepth 1 ! -name INDEX.md -delete
mkdir -p "$HERE/source"
(cd "$WORK/drupal" && tar --exclude=.git -cf - .) | tar -xf - -C "$HERE/source"

php -d memory_limit=2G "$HERE/tools/extract.php" "$HERE/source" > "$WORK/items.json"
python3 "$HERE/tools/render.py" "$WORK/items.json" "$HERE/source" "$HERE" "$VERSION"
