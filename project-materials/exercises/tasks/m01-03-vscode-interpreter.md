# M01 Step 3 — Select The Exercise Interpreter In Visual Studio Code

Prerequisite: learner-supplied environment execution under
[m01-02-virtual-environment.md](m01-02-virtual-environment.md).

Outcome: the learner supplied the diagnostic output pointing to the assigned
exercise's `.venv/Scripts/python.exe` while his terminal was at the repository
root. The terminal-interpreter check is met; the editor UI was not inspected
by the mentor. Reusable commands are collected in the shared
[COMMANDS.md](../../COMMANDS.md).

## Purpose

Selecting an interpreter tells the editor's Python support which environment to
use. A terminal has its own process environment; a previously open terminal may
still resolve `python` differently. Two interpreters can report the same Python
version, so inspect the executable path as well as the version.

Activation makes an environment's executable directory take precedence for
commands such as `python` in that terminal. It is distinct from choosing the
editor's interpreter. The previous explicit executable path worked without
requiring either editor selection or activation.

## Task

1. In the Visual Studio Code window containing the repository, check that the
   Microsoft Python extension is installed. If absent, install that extension.
2. Open the command palette with Ctrl+Shift+P and choose
   `Python: Select Interpreter`.
3. Select the interpreter at
   `project-materials/exercises/workspaces/m01-reservations/.venv/Scripts/python.exe`.
   If it is not listed, use `Enter interpreter path...` to select that file.
4. Open a new integrated PowerShell terminal using Terminal > New Terminal.
   Run the diagnostic below and send its output, along with confirmation of
   which interpreter you selected. Report any activation or command error.

```powershell
python -c "import sys; print(sys.executable)"
```

`-c` executes the quoted Python code. `import sys` makes Python's built-in
interpreter-information module available; `sys.executable` holds the running
interpreter's executable path, and `print` displays it. This is explained
diagnostic scaffolding, not an independently written exercise solution.

The expected path ends with the assigned workspace's
`m01-reservations/.venv/Scripts/python.exe` (Windows normally shows backslashes).
If a different path appears, retain it for troubleshooting before installing
dependencies. A selected editor entry alone does not verify terminal resolution.

## Completion Criterion And Next Step

The learner confirms editor selection and supplies integrated-terminal output
pointing to the exercise environment. Then check Git ignore behavior and guide
dependency setup before assigning the learner's function and test. No coding
mastery, pytest installation, or completed M01 is inferred from this task.

Interpreter selection and editor/extension roles were checked against the
official [Visual Studio Code Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial).
No editor setting or environment activation was performed by the mentor.
