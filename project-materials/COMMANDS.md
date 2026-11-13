# Command Reference

One shared reference for useful commands introduced during learning, across all
modules and exercises. Entries explain purpose and working directory; inclusion
does not mean that the learner has run or mastered a command. Learning evidence
is recorded separately in [PROGRESS.md](PROGRESS.md).

The repository root is the `eu-bicycle-trade` directory. The active M02 workspace
is `project-materials/exercises/workspaces/m02-reservations/`; it uses its own
`.venv`. Earlier M01 entries retain their stated
working directories under `project-materials/exercises/workspaces/m01-reservations/`.
Python and Git commands below work in Windows PowerShell and Command Prompt
(CMD). Navigation commands are labelled by shell. Run each command separately.

## Table Of Contents

- [Python Interpreter](#python-interpreter)
- [Virtual Environments](#virtual-environments)
- [Packages And Test Tools](#packages-and-test-tools)
- [Navigation](#navigation)
- [Git Inspection](#git-inspection)
- [Git Staging](#git-staging)

## Python Interpreter

### Find The Interpreter Actually Running

**Where:** any directory in the terminal you want to check.
**Effect:** displays information; changes no files.

```console
python -c "import sys; print(sys.executable)"
```

- `python` is resolved by the current terminal environment.
- `-c` executes the Python code inside the quotes.
- `import sys` loads the built-in module exposing interpreter information.
- `sys.executable` is the path to the running interpreter executable.
- `print(...)` displays that value; the semicolon separates two statements.

For the M01 environment check, expect a path ending in
`m01-reservations\.venv\Scripts\python.exe`. The terminal's current directory
can still be the repository root. The executable path establishes interpreter
selection more precisely than the version: different environments can use the
same Python version.

### Inspect Versions

**Where:** any directory.

| Command | Meaning |
| --- | --- |
| `python --version` | Version of the interpreter resolved by the current terminal. |
| `py --version` | Version launched by `py` without an explicit version selector. |
| `py -V:3.15 --version` | Version of the Python 3.15 interpreter explicitly selected through `py`. |

`--version` prints the version and exits. The learner has reported Python
3.15.2. An explicit selector for an absent series reports an error; it does not
mean that an already installed different series is broken.

Sources: [Python command-line options](https://docs.python.org/3.15/using/cmdline.html),
[Python on Windows](https://docs.python.org/3/using/windows.html).

### Run A Python Script

**Where:** `project-materials/exercises/workspaces/m01-reservations/`,
in PowerShell or CMD, with the prepared exercise environment.

```console
.\.venv\Scripts\python.exe reservations.py
```

The interpreter executes the named Python file. The script path is relative
to the terminal's working directory. The current example prints `50`, the
total booked minutes for room `B` in its sample data. This invokes the script
directly; it does not run pytest. The explicit interpreter path works without
environment activation.

### Run The M02 Starting Script

**Where:** `project-materials/exercises/workspaces/m02-reservations/`,
in PowerShell or CMD. **Prerequisite:** the M02 `.venv` created under
[Create The M02 Environment](#create-the-m02-environment).

```console
.\.venv\Scripts\python.exe mixed_reservations.py
```

The executable and script belong to the M02 workspace. The explicit executable
path works without activation. The supplied example reads its adjacent
`reservations.json` and prints the room-B booked total in minutes. This command
executes the current working script. Automated test commands will be introduced
with the testing step.

## Virtual Environments

**Where:** `project-materials/exercises/workspaces/m01-reservations/`,
not the repository root. This is the earlier M01 setup reference, not a step
to repeat for M02.

Create the exercise environment using Python 3.15:

```console
py -V:3.15 -m venv .venv
```

`-m` runs a module as a program; `venv` is Python's built-in environment-creation
module. `.venv` is the destination directory. This is a setup command that
creates local files, not a diagnostic to rerun routinely. Store exercise code
outside `.venv`; keep generated environment files out of Git.

Run that environment's interpreter directly to inspect its version:

```console
.\.venv\Scripts\python.exe --version
```

The explicit path works without activation. Activation is a convenience that
makes commands such as `python` resolve to the environment in that terminal;
choosing an interpreter in the editor and activating a terminal are separate.

Source: [Python virtual environments](https://docs.python.org/3.15/library/venv.html).

### Create The M02 Environment

**Where:** `project-materials/exercises/workspaces/m02-reservations/`,
in PowerShell or CMD. **Prerequisite:** Python 3.15 is already available and
the target `.venv` directory has not yet been created.

```console
py -V:3.15 -m venv .venv
```

Creates an exercise-local environment using the installed Python 3.15. Its
interpreter is `.venv\Scripts\python.exe`, and its installed packages are
isolated from the M01 environments. Run the creation command once for this
workspace. The current loader uses Python's standard library. Package setup
for the later automated tests will be introduced at that step.

The same Python version can underpin several separate virtual environments.
Each environment provides its own interpreter entry point and package directory.
The existing interpreter-inspection commands above can also use this explicit
executable path.

### Create And Inspect A Reproduction Environment

**Where:** `project-materials/exercises/workspaces/m01-reservations/`,
in PowerShell or CMD. **Prerequisite:** `.venv-repro` does not already exist.
Keep the original `.venv`; run each command separately.

```console
py -V:3.15 -m venv .venv-repro
```

Creates a second environment with isolated installed packages. Its name is a
chosen directory name. If the target already exists, inspect that situation
before proceeding: venv can reuse an existing directory, which would not prove
a fresh setup. Do not copy packages from the original environment.

```console
.\.venv-repro\Scripts\python.exe --version
```

```console
.\.venv-repro\Scripts\python.exe -c "import sys; print(sys.executable)"
```

These show the Python version and confirm the executable belongs to
`.venv-repro`. Explicit paths work without activation or changing VS Code's
interpreter selection.

```console
.\.venv-repro\Scripts\python.exe -m pip freeze
```

Inspects dependency inventory without installing packages or changing the
requirements file. Before exercise dependency installation, a fresh environment
here normally gives no package lines; pip itself is omitted by default on
Python 3.12 and later. Empty output is therefore an expected baseline, not
proof that the pip tool is missing. Reproduction requires subsequent installation
and successful example/test execution; this baseline alone is insufficient.

Sources: [venv](https://docs.python.org/3/library/venv.html),
[pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/).

### Install And Verify Reproduction Dependencies

**Where:** the same exercise directory, in PowerShell or CMD, after the fresh
`.venv-repro` baseline is reviewed. Run commands separately; retain an error
for diagnosis before advancing past a failed installation.

```console
.\.venv-repro\Scripts\python.exe -m pip install pip==26.3
```

```console
.\.venv-repro\Scripts\python.exe -m pip --version
```

```console
.\.venv-repro\Scripts\python.exe -m pip install -r requirements-dev.txt
```

The install commands change the reproduction environment and may download
packages. Verify pip 26.3 and its path inside `.venv-repro`; `-r` reads the
recorded requirements. The original `.venv` is not the selected installation
target. Keep the requirements file unchanged while checking reproduction.

```console
.\.venv-repro\Scripts\python.exe -m pip freeze
```

Compare installed names and versions with `requirements-dev.txt`; report
differences rather than overwriting the file. Freeze omits pip by default.

```console
.\.venv-repro\Scripts\python.exe reservations.py
```

```console
.\.venv-repro\Scripts\python.exe -m pytest
```

These run the unchanged example and tests with the reproduction interpreter.
Expect `50` and `3 passed`; execution may write local caches. Installing packages
alone is not a passing reproduction check. These commands do not exercise the
notebook tooling even though its dependencies are included in the inventory.

## Packages And Test Tools

**Where:** any directory in a terminal already verified to use the exercise's
`.venv/Scripts/python.exe`. PowerShell or Command Prompt (CMD).

| Command | Purpose And Effect |
| --- | --- |
| `python -m pip --version` | Displays the pip version, its installation path, and Python version. Check that the path is inside the exercise environment before installing packages. |
| `python -m pip install pytest` | Downloads and installs pytest and its required dependencies into that interpreter's environment. This changes the environment and may contact the package index. |
| `python -m pytest --version` | Starts pytest through the selected interpreter and prints its version; does not run the exercise's tests. |
| `python -m pip freeze` | Prints installed package versions in requirements format, including installed dependencies. Changes no files. |
| `python -m pip install --upgrade pip` | Updates pip in this interpreter's environment; may download packages. The long option is `--upgrade`, with two hyphens. An update notice does not make an upgrade a prerequisite for every installation. |
| `python -m pip install pip==26.3` | Installs the pip version recorded for this exercise, rather than selecting a newer release. This changes the environment and may download packages. |

`pip` is Python's package installer; a package is installable reusable code.
`pytest` is a package for discovering and running automated tests. `python -m`
binds the invoked tool to that particular interpreter, rather than relying on
the terminal to resolve a separate `pip` or `pytest` executable.

If the pip installation path is outside the exercise environment, resolve the
interpreter mismatch before installing anything. Record the observed pytest
version before preparing the exercise dependency file; a version display alone
does not establish a reproducible setup or passed tests.

### Record And Reinstall Exercise Dependencies

For this small exercise, copy the actual `python -m pip freeze` output into
`requirements-dev.txt` in the exercise directory using Visual Studio Code, saved
as UTF-8. `name==version` pins that installed package version. Keep the displayed
dependencies too, rather than recording only pytest. Review the output before
recording it. On Python 3.15, freeze normally omits pip; record Python and pip
versions separately in the learner's exercise setup notes.

The file is an installed-package inventory for this exercise environment, not
a complete environment definition or a guarantee of identical behavior on a
different platform. Verify fresh-environment reproduction later in M01.

**Where:** exercise directory containing `requirements-dev.txt`.
**Effect:** the following command installs packages from that file into the
selected interpreter's environment and may download them. Use it during later
recreation, rather than reinstalling the current environment just to record it.

```console
python -m pip install -r requirements-dev.txt
```

`-r` means read package requirements from the specified file. Its path is
relative to the terminal's current directory. Creating/editing the file alone
does not install or change packages.

For setup instructions that should work without activation, invoke the exercise
interpreter directly. **Where:** the exercise directory, in PowerShell or CMD.

```console
.\.venv\Scripts\python.exe -m pip install pip==26.3
```

```console
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

The explicit-path prefix can also be used with the `--version` and `-c`
diagnostics above. The exercise-specific sequence is documented in
[SETUP.md](exercises/workspaces/m01-reservations/SETUP.md).

Sources: [Running pip](https://pip.pypa.io/en/stable/user_guide/#running-pip),
[Installing pytest](https://docs.pytest.org/en/stable/getting-started.html#install-pytest).
Dependency references: [pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/),
[Repeatable installations](https://pip.pypa.io/en/stable/topics/repeatable-installs/).

### Run The Reservation Tests

**Where:** `project-materials/exercises/workspaces/m01-reservations/`.
**Prerequisite:** the learner has created `test_reservations.py` next to
`reservations.py`. PowerShell or CMD; activation is not required for this form.

```console
.\.venv\Scripts\python.exe -m pytest -q test_reservations.py
```

`-m pytest` runs the test runner with the explicitly selected interpreter.
`-q` reduces output verbosity. The final argument restricts the run to that file.
Test files and functions use the `test_` naming convention so pytest can discover
them. A zero-test result does not verify a function. A passing result establishes
only the checked cases. Execution may create pytest/Python cache files locally.

Pytest calls the discovered test functions; do not also call them at module scope
or print their return values. In the compact output, `.` denotes a passed test,
`F` a failed test, and the summary reports counts such as `3 passed` or `1 failed`.
A test normally returns `None`; the runner's report communicates the outcome.
Errors while importing or collecting tests are reported separately as errors.

Source: [First pytest test](https://docs.pytest.org/en/stable/getting-started.html#create-your-first-test).

### Run Tests With Exercise Configuration

**Where:** `project-materials/exercises/workspaces/m01-reservations/`.
**Prerequisite:** the learner has created `pytest.ini` in that directory with
the exercise's search-location and compact-output defaults. PowerShell or CMD.

```console
.\.venv\Scripts\python.exe -m pytest
```

Without explicit test paths, pytest uses the configured `testpaths` when run
from the configuration root. `addopts` supplies default command-line options,
including `-q` for this exercise. Read the pass/fail summary; three discovered
tests must actually execute and pass. This command may write local caches.

Inspect the selected configuration and collected tests separately:

```console
.\.venv\Scripts\python.exe -m pytest --collect-only -o addopts=
```

`--collect-only` discovers tests without running their bodies. Collection imports
modules, so their top-level statements can execute. `-o addopts=` temporarily
overrides the extra default options with an empty value so the normal startup
header is visible; it does not change the configuration file. Inspect the
`configfile` entry and the collected-test count. Collection alone does not prove
that assertions pass. This inspection may also write local caches.

Sources: [pytest configuration](https://docs.pytest.org/en/stable/reference/customize.html),
[pytest settings and options](https://docs.pytest.org/en/stable/reference/reference.html#configuration-options).

### Check Requirements Against The Existing Environment

This checks whether `requirements-dev.txt` matches installed packages, not
whether newer releases are available. It does not install or upgrade anything.

1. In Visual Studio Code, use File > Open Folder to open the repository root.
2. Open a new integrated terminal with Terminal > New Terminal. If its working
   directory is the repository root, enter the exercise directory using the
   command below, which works in both PowerShell and CMD:

   ```console
   cd project-materials\exercises\workspaces\m01-reservations
   ```

3. Invoke the existing environment's interpreter directly:

   ```console
   .\.venv\Scripts\python.exe -m pip freeze
   ```

4. Open the exercise's `requirements-dev.txt` in the editor. Compare package
   names and versions with the displayed output. Note added packages, missing
   packages, and changed versions. Review differences before deciding whether
   to change the file; do not overwrite it merely to make it match.

The explicit executable path selects the intended environment without relying
on activation or editor interpreter selection. If the terminal starts elsewhere,
navigate to the exercise directory first instead of reusing a relative path
from an unknown location. A missing executable is a finding to diagnose, not
an instruction to recreate the environment automatically.

This terminal inspection is separate from the kernel selected for an open
notebook. A notebook kernel is the Python process executing its cells; when
checking notebook behavior, inspect/select that environment separately.

## Navigation

**Where:** start at the repository root. These commands change the current
directory of the terminal, not the location of any files.

PowerShell:

```powershell
Set-Location 'project-materials/exercises/workspaces/m01-reservations'
```

Command Prompt (CMD):

```bat
cd project-materials\exercises\workspaces\m01-reservations
```

Paths beginning with `.` refer to the current directory. Navigation matters
because a relative path such as `.venv` is interpreted from that directory.

To move from the M01 workspace to the neighbouring M02 workspace, in PowerShell
or CMD, use the following command. `..` refers to the parent `workspaces` directory.

```console
cd ..\m02-reservations
```

## Git Inspection

**Where:** repository root for the paths shown below. These commands inspect
state; they do not stage files, create commits, or contact a remote server.

| Command | Purpose |
| --- | --- |
| `git status --short` | Compact overview of changed and untracked files; ignored files are normally omitted. |
| `git diff` | Unstaged changes to tracked files; does not show the contents of untracked files. |
| `git diff -- project-materials/PROGRESS.md` | Unstaged changes to one named tracked file. `--` separates paths from options. |
| `git diff --staged` | Changes already staged for a possible commit. |
| `git diff --check` | Checks the unstaged patch for whitespace errors; does not establish code correctness. |

### Review Workspace Files And A Tracked Patch

**Where:** repository root, in PowerShell or CMD.
**Effect:** inspection only; no staging, commit, or remote access.

```console
git status --short --untracked-files=all -- project-materials/exercises/workspaces/m01-reservations/
```

`--untracked-files=all` lists individual untracked files instead of collapsing
their directory. The path restricts this listing to the workspace. `??` means
untracked; ` M` means a tracked file has an unstaged modification, while `M `
means a staged modification. Normally ignored files are omitted.

```console
git diff -- project-materials/exercises/tasks/m01-02-virtual-environment.md
```

This compares the named tracked working file with its indexed version.
Added content lines start with `+`, removed content lines with `-`.
The `---` and `+++` headers identify files; `@@` identifies changed line ranges.
If a pager opens, `q` exits it. For untracked files, open their contents in the
editor: ordinary `git diff` does not include them. A path-limited status is not
a review of other repository changes.

Sources: [git status](https://git-scm.com/docs/git-status),
[git diff](https://git-scm.com/docs/git-diff).

### Check Why An Environment File Is Ignored

```console
git check-ignore -v -- project-materials/exercises/workspaces/m01-reservations/.venv/Scripts/python.exe
```

`-v` displays the matching rule's source, line number, pattern, and checked path.
A pattern beginning with `!` reverses an exclusion, so inspect the actual rule.
No output is not proof that the file is safe to commit: by default this command
also skips tracked files. Check whether Git already tracks any files in the
exercise environment:

```console
git ls-files -- project-materials/exercises/workspaces/m01-reservations/.venv/
```

Output from `git ls-files` identifies tracked paths; no output means no paths
under this environment directory are in the index. Ignore rules do not
automatically untrack files.
If the result is unexpected, discuss it before changing tracking rules.

Sources: [Git ignore diagnostics](https://git-scm.com/docs/git-check-ignore),
[Git tracked-file listing](https://git-scm.com/docs/git-ls-files).

## Git Staging

**Where:** within the repository. **Effect:** changes the index (staging area),
which holds content prepared for the next commit. This is reference material
from the ignore/tracking discussion, not an instruction to stage the current
working tree during the diagnostic exercise.

```console
git add --all
```

`git add -A` is the equivalent short form. Without a path restriction, it stages
additions, modifications, and deletions across the repository, while respecting
ignore rules for untracked files. It does not create a commit.

| File state | What happens during `git add --all` |
| --- | --- |
| Already tracked, modified, and now matching a `.gitignore` pattern | The modification is staged; ignore rules do not end existing tracking. |
| Untracked and excluded by an ignore rule | The file is skipped. |

The next ordinary commit records the staged content. Later edits require
staging again to include them. Review staged content with `git diff --staged`.

`git add all` without the hyphens treats `all` as a path argument; it is not the
option meaning all changes.

Source: [Git staging](https://git-scm.com/docs/git-add).
