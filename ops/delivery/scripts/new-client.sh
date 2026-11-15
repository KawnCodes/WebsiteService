#!/usr/bin/env bash
# Create a new client site from the Running Tab template.
# Usage: ops/delivery/scripts/new-client.sh <client-slug> [target-dir]
#   e.g. ops/delivery/scripts/new-client.sh the-blue-door ../clients/the-blue-door
# Then: cd <target-dir> && npm install && npm run dev
set -euo pipefail

slug="${1:?Usage: new-client.sh <client-slug> [target-dir]}"
if [[ ! "$slug" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "Slug must be lowercase letters, numbers and hyphens, e.g. the-blue-door" >&2; exit 1
fi
here="$(cd "$(dirname "$0")" && pwd)"
repo_root="$(cd "$here/../../.." && pwd)"
target="${2:-$repo_root/../clients/$slug}"

if [[ -e "$target" ]]; then echo "Target already exists: $target" >&2; exit 1; fi

mkdir -p "$target"
cp -R "$here/../client-template/." "$target/"
mkdir -p "$target/src/templates/venue"
# Always copy the latest version of the template from the agency site, so there's one source of truth.
cp "$repo_root/site/src/templates/venue/VenueSite.astro" "$target/src/templates/venue/"
cp "$repo_root/site/public/favicon.svg" "$target/public/favicon.svg"

# Start from the Larkspur demo data, marked as a real (non-demo) site.
python3 - "$repo_root/site/demos/larkspur.json" "$target/venue.json" "$slug" <<'PY'
import json, sys
src, dst, slug = sys.argv[1:4]
v = json.load(open(src))
v.update({"slug": slug, "demo": False, "name": "CLIENT NAME", "siteUrl": "", "formAccessKey": "", "notice": ""})
json.dump(v, open(dst, "w"), indent=2, ensure_ascii=False)
open(dst, "a").write("\n")
PY

cd "$target"
git init -q -b main
git add -A
git commit -q -m "Start $slug site from Running Tab template"
echo "Created $target"
echo "Next: edit venue.json, then: cd $target && npm install && npm run dev"
