# Python testing workshop starter

## Development instructions

## With devcontainer

This repository comes with a devcontainer (a Dockerized Python environment). If you open it in Codespaces, it should automatically initialize the devcontainer.

Locally, you can open it in VS Code with the Dev Containers extension installed.

## Without devcontainer

If you can't or don't want to use the devcontainer, then you should first create a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

Then install the dev tools:

```
python3 -m pip install --user -r requirements-dev.txt
```

## Adding code and tests

This repository contains `texter.py` and a test file for it at `texter_test.py`.

Once you've written a test, run:

```
python3 -m pytest
```
