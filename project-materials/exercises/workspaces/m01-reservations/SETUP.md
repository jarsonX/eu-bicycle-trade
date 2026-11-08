# Development Setup

Set up the reservation exercise environment on Windows, run the example,
and execute the tests.

## Table Of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Verify Installation](#verify-installation)
- [Usage](#usage)

## Prerequisites

- Python 3.15.2, available through the `py` command.
- PowerShell or Command Prompt (CMD).

Package versions are pinned in [requirements-dev.txt](requirements-dev.txt).

## Setup

From the repository root, navigate to the exercise directory.

PowerShell:

```powershell
Set-Location 'project-materials/exercises/workspaces/m01-reservations'
```

Command Prompt (CMD):

```bat
cd project-materials\exercises\workspaces\m01-reservations
```

Check that the base interpreter is Python 3.15.2:

```console
py -V:3.15 --version
```

Create a virtual environment:

```console
py -V:3.15 -m venv .venv
```

Install pip 26.3 and the pinned dependencies:

```console
.\.venv\Scripts\python.exe -m pip install pip==26.3
```

```console
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

All commands above run from `project-materials/exercises/workspaces/m01-reservations/`.
Using the environment's executable directly works in PowerShell and CMD without
activation. Keep source files and tests outside `.venv`.

## Verify Installation

Run from the exercise directory:

```console
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable)"
```

The interpreter path should end with `m01-reservations\.venv\Scripts\python.exe`.

```console
.\.venv\Scripts\python.exe --version
```

```console
.\.venv\Scripts\python.exe -m pip --version
```

```console
.\.venv\Scripts\python.exe -m pytest --version
```

Expected versions:

| Tool | Version |
| --- | --- |
| Python | 3.15.2 |
| pip | 26.3 |
| pytest | 9.2.0 |

## Usage

Run all commands below from `project-materials/exercises/workspaces/m01-reservations/`.
They use the environment's interpreter directly and do not require activation.

### Run The Example

```console
.\.venv\Scripts\python.exe reservations.py
```

The example in [reservations.py](reservations.py) prints the total booked
minutes for room `B` in the bundled sample data:

```text
50
```

### Run The Tests

```console
.\.venv\Scripts\python.exe -m pytest
```

The defaults in [pytest.ini](pytest.ini) search for tests from the exercise
directory and enable compact output. No test-file argument or `-q` is needed.

Expected summary: `3 passed`. The tests in
[test_reservations.py](test_reservations.py) cover summing the selected room's
reservations while excluding another room, an absent room, and an empty list.
Elapsed time can vary. A result reporting zero collected tests does not verify
these cases.
