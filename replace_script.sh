#!/bin/bash

# Script to replace aaPanel references with wwwPanel

echo "Starting replacements..."

# Replace URLs
find . -type f -name "*.py" -o -name "*.sh" -o -name "*.md" -o -name "*.txt" -o -name "*.json" -o -name "*.yml" -o -name "*.yaml" | xargs sed -i 's|node\.aapanel\.com|plugins.wwwpanel.org|g'
find . -type f -name "*.py" -o -name "*.sh" -o -name "*.md" -o -name "*.txt" -o -name "*.json" -o -name "*.yml" -o -name "*.yaml" | xargs sed -i 's|www\.aapanel\.com|www.wwwpanel.com|g'
find . -type f -name "*.py" -o -name "*.sh" -o -name "*.md" -o -name "*.txt" -o -name "*.json" -o -name "*.yml" -o -name "*.yaml" | xargs sed -i 's|api\.aapanel\.com|api.wwwpanel.com|g'
find . -type f -name "*.py" -o -name "*.sh" -o -name "*.md" -o -name "*.txt" -o -name "*.json" -o -name "*.yml" -o -name "*.yaml" | xargs sed -i 's|wafapi2\.aapanel\.com|wafapi2.wwwpanel.com|g'
find . -type f -name "*.py" -o -name "*.sh" -o -name "*.md" -o -name "*.txt" -o -name "*.json" -o -name "*.yml" -o -name "*.yaml" | xargs sed -i 's|forum\.aapanel\.com|forum.wwwpanel.com|g'
find . -type f -name "*.py" -o -name "*.sh" -o -name "*.md" -o -name "*.txt" -o -name "*.json" -o -name "*.yml" -o -name "*.yaml" | xargs sed -i 's|doc\.aapanel\.com|doc.wwwpanel.com|g'
find . -type f -name "*.py" -o -name "*.sh" -o -name "*.md" -o -name "*.txt" -o -name "*.json" -o -name "*.yml" -o -name "*.yaml" | xargs sed -i 's|demo\.aapanel\.com|demo.wwwpanel.com|g'

# Replace aaPanel with wwwPanel in text
find . -type f -name "*.py" -o -name "*.sh" -o -name "*.md" -o -name "*.txt" -o -name "*.json" -o -name "*.yml" -o -name "*.yaml" | xargs sed -i 's|aaPanel|wwwPanel|g'
find . -type f -name "*.py" -o -name "*.sh" -o -name "*.md" -o -name "*.txt" -o -name "*.json" -o -name "*.yml" -o -name "*.yaml" | xargs sed -i 's|aapanel|wwwpanel|g'

# Replace GitHub repo
find . -type f -name "*.py" -o -name "*.sh" -o -name "*.md" -o -name "*.txt" -o -name "*.json" -o -name "*.yml" -o -name "*.yaml" | xargs sed -i 's|aaPanel/aaPanel|yourorg/wwwpanel|g'

echo "Replacements completed."
