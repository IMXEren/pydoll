#!/usr/bin/env bash
set -euo pipefail

VERSION="${1:-}"

if [ -z "$VERSION" ]; then
  echo "Usage: $0 <version>" >&2
  exit 1
fi

# semantic-release dev branch produces e.g. 3.0.1-dev.1 (PEP 440: 3.0.1.dev1).
VERSION="${VERSION/-dev./.dev}"

echo "Setting version to $VERSION"
uv version --no-sync "$VERSION"
uv lock --check
