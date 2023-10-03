name: Linter
on:
  push:
    branches: [main]
  pull_request:
    paths:
      - '*.yml'
  workflow_dispatch:
jobs:
  linter:
    runs-on: windows-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
        with:
          fetch-depth: 0
      # - name: Set up Python 3.8
      #   uses: actions/setup-python@v2
      #   with:
      #     python-version: 3.6.9
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flake8
          #pip install pylint
          # if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
      # - name: Lint with flake8
        # run: |
        #   flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics
        #   flake8 src --count --max-complexity=10 --max-line-length=79 --statistics
      - name: Lint with Pylint
        run: |
          #pylint $(git ls-files '*.py')
          #pylint $(git diff origin/main --name-only --diff-filter=d) works
          flake8 $(git diff origin/main --name-only --diff-filter=d)
          #pylint $(git diff --name-only --diff-filter=ACMR)
          #pylint $(git diff-tree --name-only -r $CI_MERGE_REQUEST_DIFF_BASE_SHA $CI_COMMIT_SHA)
          # DIFF=$(git diff --name-only --diff-filter=d $(git merge-base HEAD $BRANCH) | grep -E '\.py$')
          # pylint $DIFF

