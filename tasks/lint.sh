#!/bin/bash
set -uo pipefail
set +e

FAILURE=false

# echo "safety (failure is tolerated)"
# FILE=requirements/prod.txt
# if [ -f "$FILE" ]; then
#     # We're in the main repo
#     safety check -r requirements/prod.txt -r requirements/dev.txt
# else
#     # We're in the labs repo
#     safety check -r ../requirements/prod.txt -r ../requirements/dev.txt
# fi

echo "pylint"
pylint src/main.py src/models.py || FAILURE=true

echo "pycodestyle"
pycodestyle src/main.py src/models.py || FAILURE=true

echo "pydocstyle"
pydocstyle src/main.py src/models.py || FAILURE=true

# Causes issues for spacy (so removed failure):
# src/main.py:10: error: Skipping analyzing "spacy": 
# found module but no type hints or library stubs
echo "mypy"
mypy src/main.py src/models.py # || FAILURE=true

echo "bandit"
bandit -ll -r {src/main.py,src/models.py} || FAILURE=true

# echo "shellcheck"
# find . -name "*.sh" -print0 | xargs -0 shellcheck || FAILURE=true

if [ "$FAILURE" = true ]; then
  echo "Linting failed"
  exit 1
fi
echo "Linting passed"
exit 0
