# M00 Part 4 — Environment, Configuration, And Notebook State

This continues the theoretical introduction after
[m00-03-provenance-snapshots-and-reproducibility.md](m00-03-provenance-snapshots-and-reproducibility.md).
Examples use fictional reservation durations. This lesson does not choose
interpreter or dependency versions or perform installation or setup.
Hands-on environment setup belongs to M01 after the M00 introduction.

## Contents

- [Interpreter And Dependencies](#interpreter-and-dependencies)
- [Virtual Environments And Their Limits](#virtual-environments-and-their-limits)
- [Configuration And Git](#configuration-and-git)
- [Notebook State And Execution Order](#notebook-state-and-execution-order)
- [Modules And A Fresh Run](#modules-and-a-fresh-run)
- [Understanding Check](#understanding-check)

## Interpreter And Dependencies

The Python interpreter is the program that executes Python code. An editor lets
you write the code but need not execute it using the Python installation you
expect. Several interpreters can coexist on one computer.

A library provides reusable code. A dependency is a package the project relies
on, such as pandas for working with tables; `sum`, by contrast, is a built-in
Python function and needs no external package. Python also includes a standard
library of modules supplied with the interpreter, including `sys`, which
provides information about the running Python process.

Installing a package for one interpreter does not necessarily make it available
to another. A terminal may use one Python while a notebook uses another.
If an import reports that a module cannot be found, compare the active
interpreters and their installed packages before installing again. An `import`
statement makes an available module accessible in the program; it does not
download and install a missing package.

The following introspection can help identify the running interpreter. It is
an illustration for later diagnosis, not a command we have executed here:

```python
import sys
print(sys.executable)
```

Run in the terminal's Python and in the notebook, it shows the executable path
for each process. Comparing those paths is a useful first check; matching them
does not by itself establish that every other execution condition is identical.

## Virtual Environments And Their Limits

A virtual environment is a project-specific Python environment with its own
installed packages, normally isolated from packages in other environments.
It allows two projects to use different library versions without continually
changing each other's installations. It is not a separate computer or operating
system, and creating one does not install every library needed by the project.

Environment activation adjusts a shell so commands preferentially use that
environment's executables. It does not automatically switch the interpreter
already selected by an editor or a running notebook. Interpreter selection and
notebook execution must point to the intended environment.

For reproducibility, describe the Python version and dependency versions, along
with how to recreate the environment. Installing a library may also install
packages it needs; these indirect packages are transitive dependencies. Recording
only one top-level library version may therefore leave other versions unspecified.
Files such as `requirements.txt` can list requirements, while a lock file records
a resolved dependency selection for a particular tool. File names alone do not
prove a complete or working environment: the actual contents and a fresh setup
check matter. The simplest appropriate mechanism will be chosen during setup.

The virtual-environment directory itself is not a portable setup recipe.
Normally recreate it from tracked setup instructions and dependency definitions
rather than commit that directory to Git. Operating-system differences or other
external resources can still matter; a virtual environment does not freeze the
entire computer or preserve the data snapshot.

## Configuration And Git

Configuration consists of explicit choices governing a run, such as which room
to analyze, which snapshot to read, or whether an incomplete daily series stops
the run or yields a labelled partial result. The computation can stay unchanged
while a configuration change produces a different answer. For example, in the
original reservation sample, room A totals 90 minutes while both rooms total
135; the scope selection explains the difference.

Keep ordinary reproducibility-relevant settings and dependency definitions
under version control where appropriate. Git tracks selected file versions;
it does not automatically capture an editor's selected interpreter or live
variables in a notebook. A `.gitignore` file identifies untracked files or
directories Git should normally ignore, such as a local virtual environment.
It does not stop tracking an already tracked file. Credentials belong outside
tracked configuration; use fictional placeholders in shared examples.

## Notebook State And Execution Order

A notebook is a document, commonly stored as `.ipynb`, containing code cells,
explanatory text, and potentially saved outputs. A cell is a separately runnable
block of content. A kernel is the process executing the notebook's code; for
a Python notebook, it holds variables, imported modules, and function definitions
in memory between executions.

Consider three code cells in this visible order:

```python
# Cell 1
durations = [30, 60, 45]
```

```python
# Cell 2
total = sum(durations)
```

```python
# Cell 3
print(total)
```

Executing cells 1, 2, and 3 in order prints 135. Now edit cell 1 to use
`[30, 90, 45]`, execute cell 1, then execute cell 3, skipping cell 2. The printed
value remains 135. Reassigning `durations` does not automatically recompute
`total`; the earlier value of `total` remains in kernel memory. Executing cell 2
again, followed by cell 3, produces 165. A normal Python variable assignment is
not a spreadsheet formula with automatic dependency recalculation.

Hidden state is the execution history affecting the live kernel that is not
fully represented by reading the currently visible code from top to bottom.
For example, a removed cell may have defined a variable that still exists in
memory. Saved outputs can also reflect older code and are not proof that the
currently visible notebook can regenerate them. Saving the notebook does not
recompute its outputs or normally preserve all live kernel memory.

## Modules And A Fresh Run

Restarting the kernel clears the live Python session. Running all cells from
top to bottom afterward checks whether the notebook supplies its own required
definitions and computations in a valid order. If a variable was defined only
in a deleted cell, a fresh run exposes that missing step. External files and
other effects are not undone by a kernel restart, so this check does not replace
preserving inputs or recreating the environment.

A fresh-kernel run tests the notebook's dependence on retained session state.
A fresh-environment run additionally tests whether the recorded setup supplies
the required interpreter and dependencies. Both are useful, but neither alone
proves correct formulas or sound interpretation.

A module, commonly a `.py` file, organizes reusable code into functions and
other definitions. Starting a script in a new Python process executes its
top-level code in order. This helps make execution order explicit. However,
modules can still use mutable global state or external files, and an imported
module is normally cached within the running Python process. Moving code to a
`.py` file does not automatically guarantee a clean state or reproducibility.
Keep exploration and explanations in notebooks; put reusable calculations and
other stable responsibilities in modules with explicit inputs and outputs.

## Understanding Check

1. A library is installed for the Python used in your terminal, but the notebook
   cannot import it. What would you compare first, and why might another
   installation attempt fail to solve the problem?
2. In the three-cell example, the notebook displays 135 even after cell 1 was
   changed and executed with `[30, 90, 45]`; only cell 3 was rerun afterward.
   Explain why 135 remains and how you would check that the visible notebook
   can reproduce its result without retained kernel state.

Explain your reasoning without installing packages or executing commands.
These are M00 understanding checks, not the independent M01/M02 exercises.
