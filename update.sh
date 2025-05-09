#!/usr/bin/env bash

echo "Check for updates to the patterns file"
PATTERNS_FILE="is_bot/_patterns.py"
SOURCE_BASE="https://raw.githubusercontent.com/omrilotan/isbot/refs/heads/main"
package=$(curl -s "$SOURCE_BASE/package.json")
version=$(echo "$package" | jq -r '.version')
currentversion=$(head -n 1 "$PATTERNS_FILE" | grep -o '[0-9]\+\.[0-9]\+\.[0-9]\+')
if [ "$currentversion" == "$version" ]; then
    echo "Patterns file is already up to date (version $currentversion)"
else
    echo "# https://github.com/omrilotan/isbot/blob/v$version/src/patterns.json" > "$PATTERNS_FILE"
    curl -s "$SOURCE_BASE/src/patterns.json" | \
        sed 's/^  /    /' | \
        sed '1s/.*/default_patterns = {/' | \
        sed '$s/.*/}/' >> "$PATTERNS_FILE"
    echo "Generated patterns file with version $version"
fi
