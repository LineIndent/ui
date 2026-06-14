#!/bin/bash
# dev.sh - Helper script for Buridan UI development
# Usage:
#   ./dev.sh page getting-started/introduction components/button
#   ./dev.sh off
#   ./dev.sh list

# Function to list available pages by scanning the docs directory
list_pages() {
  echo "Available pages (slugs):"
  # Find all markdown files, remove 'docs/' prefix and '.md' suffix,
  # and replace underscores with hyphens to create the page slug.
  find docs -name "*.md" | sed 's_docs/\(.*\)\.md_\1_' | sed 's/_/-/g' | sort
}

MODE=$1
shift

case $MODE in
  list)
    list_pages
    exit 0
    ;;
  page)
    if [ -z "$1" ]; then
      echo "Error: No pages specified for 'page' mode."
      echo "Usage: ./dev.sh page <slug1> <slug2> ..."
      exit 1
    fi
    export BURIDAN_DEV_MODE=true
    export BURIDAN_DEV_PAGES=$(echo "$@" | tr ' ' ',')
    echo "Development mode: Loading only specified pages - ${BURIDAN_DEV_PAGES}"
    ;;
  off)
    unset BURIDAN_DEV_MODE
    unset BURIDAN_DEV_PAGES
    echo "Development mode: Disabled (loading all pages)"
    ;;
  *)
    echo "Invalid mode. Use: page, list, or off"
    exit 1
    ;;
esac

# Run Reflex
uv run reflex run
