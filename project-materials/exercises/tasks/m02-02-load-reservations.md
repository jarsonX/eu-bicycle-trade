# M02 Step 2 — Implement The Record Type And Loader

The learner has chosen separate loading and validation, with both reservations
and the requested room passed to the calculation. The responsibility plan is
saved in [DESIGN.md](../workspaces/m02-reservations/DESIGN.md).

## Contents

- [Working File And Input](#working-file-and-input)
- [Required Interfaces](#required-interfaces)
- [Implementation Task](#implementation-task)
- [Review Criterion](#review-criterion)

## Working File And Input

Work in `project-materials/exercises/workspaces/m02-reservations/` and edit
[mixed_reservations.py](../workspaces/m02-reservations/mixed_reservations.py).
Use the existing [reservations.json](../workspaces/m02-reservations/reservations.json).
The single-day grain, field assumptions, and calculation/validation contract
remain defined in
[m02-01-responsibilities-and-interfaces.md](m02-01-responsibilities-and-interfaces.md#input-and-contract).

This step moves the supplied file-reading operation into an annotated function.
The original expression already demonstrates reading text and parsing it.
Select its dependencies from the function arguments.

## Required Interfaces

Define `Reservation` using the previously explained `TypedDict` notation. Its
four fields match this exercise's file, including the separate duration unit.

| Field | Annotation |
| --- | --- |
| `reservation_id` | `int` |
| `room` | `str` |
| `duration` | `int` |
| `duration_unit` | `str` |

Define `load_reservations` with these argument and return annotations.

| Item | Annotation | Meaning |
| --- | --- | --- |
| `input_path` | `Path` | A filesystem path represented by the class already imported from `pathlib`. |
| `encoding` | `str` | The text encoding supplied by the caller. |
| Return value | `list[Reservation]` | All parsed reservation records, before business-rule validation. |

`Path` in an annotation names the same class used by `Path(__file__)` in the
starter. `list[Reservation]` describes the record shape. The exercise guarantees
the required fields and basic types, while the separate validator will check
the business rules. A static-checker run is outside this step's acceptance.

## Implementation Task

1. Add the annotated `Reservation` definition before code that refers to it.
2. Write `load_reservations` with the disclosed interface. It reads from its
   path argument using its encoding argument, parses the content, and returns
   the complete list. Room selection and business-rule validation belong to
   subsequent functions.
3. Place the executable example flow under `if __name__ == "__main__"` and use
   the new loader there. Keep the existing room-label check, calculation, and
   print together in that guarded flow until their later refactoring steps.
   Preserve the adjacent-data-file path and the room-B example.

File-access and parsing errors must propagate. The valid JSON value `[]`
produces an empty list. An empty or malformed text file produces a parsing
failure. Preserve these distinct outcomes.

Use M02's exercise-local `.venv` and standard-library imports. Environment
creation and the script command are documented in
[COMMANDS.md](../../COMMANDS.md#create-the-m02-environment).
Submit the saved file for review. Automated test implementation follows after
the relevant functions and test syntax have been discussed.

## Review Criterion

The record type matches the four fields. The loader uses its arguments and
returns all parsed records. Importing the module defines its types/functions,
and file reading and reporting occur through the guarded executable flow.
Direct execution preserves the existing valid-data report.

Review the function boundary and returned data before moving to the separate
validator. No validation implementation or test solution is supplied by this
task.
