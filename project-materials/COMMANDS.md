# Command Reference

One shared reference for useful commands introduced during learning, across all
modules and exercises. Entries explain purpose and working directory; inclusion
does not mean that the learner has run or mastered a command. Learning evidence
is recorded separately in [PROGRESS.md](PROGRESS.md).

The repository root is the `eu-bicycle-trade` directory. The current exercise
directory is `project-materials/exercises/workspaces/m01-reservations/`.
Python and Git commands below work in Windows PowerShell and Command Prompt
(CMD). Navigation commands are labelled by shell. Run each command separately.

## Table Of Contents

- [Python Interpreter](#python-interpreter)
- [Virtual Environments](#virtual-environments)
- [Navigation](#navigation)
- [Git Inspection](#git-inspection)

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

For the current exercise, expect a path ending in
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

## Virtual Environments

**Where:** the current exercise directory, not the repository root.

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

### Check Why An Environment File Is Ignored

```console
git check-ignore -v -- project-materials/exercises/workspaces/m01-reservations/.venv/Scripts/python.exe
```

`-v` displays the matching rule's source, line number, pattern, and checked path.
A pattern beginning with `!` reverses an exclusion, so inspect the actual rule.
No output is not proof that the file is safe to commit: by default this command
also skips tracked files. Check whether Git already tracks the same file:

```console
git ls-files -- project-materials/exercises/workspaces/m01-reservations/.venv/Scripts/python.exe
```

Output from `git ls-files` identifies a tracked path; no output means this exact
path is not in the index. Ignore rules do not automatically untrack files.
If the result is unexpected, discuss it before changing tracking rules.

Sources: [Git ignore diagnostics](https://git-scm.com/docs/git-check-ignore),
[Git tracked-file listing](https://git-scm.com/docs/git-ls-files).
