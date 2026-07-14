#!/usr/bin/env bash
set -euo pipefail

VERSION="${1:-}"

if [ -z "$VERSION" ]; then
  echo "Usage: $0 <version>" >&2
  exit 1
fi

# semantic-release dev branch produces e.g. 2.24.1-dev.1
# Poetry needs PEP 440: 2.24.1.dev1
if echo "$VERSION" | grep -q -- '-dev.'; then
  VERSION="$(echo "$VERSION" | sed 's/-dev./.dev/')"
fi

echo "Setting version to $VERSION"
poetry version "$VERSION"
poetry lock
