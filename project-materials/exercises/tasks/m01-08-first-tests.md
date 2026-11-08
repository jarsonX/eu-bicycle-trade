# M01 Step 8 — Write The First Pytest Tests

Prerequisite: the calculation attempt and assisted typing/refactoring discussion
under [m01-07-first-function.md](m01-07-first-function.md). The learner has applied
the reference generator implementation, TypedDict, and data-list annotation.
The reference implementation is mentor-assisted; the learner owns these tests.

## Table Of Contents

- [What A Test Does](#what-a-test-does)
- [Prepare Imports](#prepare-imports)
- [Task](#task)
- [Completion Criterion](#completion-criterion)

## What A Test Does

A test calls the real function on known inputs and checks an independently
derived expected result. `assert actual == expected` continues when the values
are equal and raises an assertion error otherwise; pytest reports that as a
failed test. `==` compares values. Derive the expectation manually, rather than
calling the tested function to construct its own expected answer.

A test function named `test_...` is discovered by pytest. It has no arguments
in this exercise and uses return annotation `-> None`: it returns no useful
value, while an assertion failure signals a failed check. Do not return a boolean
as a substitute for an assertion.

Syntax example using the previously explained greeting function, not the
reservation calculation:

```python
def test_make_greeting_formal() -> None:
    result = make_greeting("Jan", True)
    assert result == "Good morning, Jan."
```

This example illustrates test syntax and assumes `make_greeting` is available;
it is not a test to copy into the reservation test file.

## Prepare Imports

In `reservations.py`, protect the example print so importing the module does
not execute it:

```python
if __name__ == "__main__":
    print(total_minutes_for_room(reservations, "A"))
```

`__name__` is a Python-provided module name. It is `"__main__"` when the file
is executed directly; on import here it is `"reservations"`. Therefore the
indented example call runs only during direct execution. The calculation
function itself remains available to imports.

Create `test_reservations.py` yourself next to `reservations.py`, outside `.venv`.
Import the names you need:

```python
from reservations import Reservation, total_minutes_for_room
```

Here `reservations` means the neighboring `reservations.py` module, not its
sample data variable. `from ... import ...` makes the named type and function
available in the test module. Running from the exercise directory with
`python -m pytest` makes that directory available for module lookup.

## Task

Write three no-argument test functions, each annotated `-> None`:

1. A normal calculation: prepare your own fictional list of three valid same-day
   reservations, with two different IDs for the requested room and one record
   for another room. Use positive integer minutes and no overlaps or missing
   fields. Annotate the local input as `list[Reservation]`, derive the expected
   total manually, call the real function, and assert equality with that total.
2. A nonempty valid input list with no reservation matching the requested room.
   Check the documented no-match result.
3. An empty list for the requested room. Check the documented empty-input result.

Use descriptive names beginning with `test_`. Tests must prepare their own
inputs rather than import the module's global example data. Invalid-input
validation, fixtures, parametrization, and test plugins are not required here.
Do not change the requirements or install additional dependencies for this task.

From `project-materials/exercises/workspaces/m01-reservations/`, run:

```console
.\.venv\Scripts\python.exe -m pytest -q test_reservations.py
```

The shared command explanation is in
[COMMANDS.md](../../COMMANDS.md#run-the-reservation-tests).
Pytest discovers and calls the test functions: do not add manual calls such as
`test_example()` at module scope or print a test's `None` return. With `-q`,
`.` indicates a passed test and `F` a failed test; read the summary for counts
such as `3 passed`. An assertion failure includes a diagnostic explaining the
failed comparison. A zero-test result does not establish success for this task.
Send the test-file path, run output, and your manual reasoning for the normal
case. If a test fails, retain its diagnostic; a failure is material to investigate.

## Completion Criterion

The learner creates the tests, explains the independent expected value, and
supplies an actual run result showing all three tests were collected and passed.
The mentor reviews the learner's attempt and helps diagnose gaps without writing
the tests for him. This step does not establish a clean-environment run, full
input validation, independent authorship of the supplied refactor, or completed
M01. Diff review, configuration, and environment reproduction remain later work.

Source: [First pytest test](https://docs.pytest.org/en/stable/getting-started.html#create-your-first-test).
