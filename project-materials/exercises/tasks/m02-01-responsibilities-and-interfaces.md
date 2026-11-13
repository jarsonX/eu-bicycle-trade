# M02 Step 1 — Plan Responsibilities And Interfaces

Prerequisites: completed M00 and M01. This exercise uses fictional meeting-room
reservations, with no bicycle data or external service. Work in
`project-materials/exercises/workspaces/m02-reservations/`.

## Contents

- [Starting Point](#starting-point)
- [Input And Contract](#input-and-contract)
- [Reading The File Operations](#reading-the-file-operations)
- [Current Task](#current-task)
- [Review And Later Steps](#review-and-later-steps)

## Starting Point

Read [mixed_reservations.py](../workspaces/m02-reservations/mixed_reservations.py)
and [reservations.json](../workspaces/m02-reservations/reservations.json).
The script reads a local file, checks for blank room labels, calculates a total,
and prints it. It deliberately mixes these activities at module scope, so
importing it also reads the file and prints. It is an unfinished starting point,
not an example of the intended design. It does not yet enforce the three new
validation rules below.

A responsibility is one coherent job performed by a part of the program. An
interface describes the agreement between parts: accepted input, returned result,
and failure behavior. Include meaning and units, not just Python types.
An effect is an interaction outside the returned value, such as reading a file
or printing. These distinctions let a calculation be checked without requiring
a file or terminal output.

Refactoring means changing code organization while preserving agreed behavior.
Here, preserve the valid-data calculation and report while adding the explicitly
required rejection of invalid inputs. Several functions in one file can suffice;
there is no required function count or one-file-per-function rule.

## Input And Contract

The file is a complete export for one fictional day D. Each record represents
one reservation. There are no cancellations or overlapping bookings. This
exercise measures booked minutes, not attendance or a percentage of capacity.

JSON means JavaScript Object Notation: a text format for structured data. This
file contains a list of records; loading it produces a Python list of dictionaries.
All required fields and their basic types are supplied correctly for this
exercise, including the later invalid examples. Generic schema/type validation
is outside the assigned scope.

| Field | Basic type | Required meaning/value |
| --- | --- | --- |
| `reservation_id` | `int` | Unique reservation identifier across the entire export. |
| `room` | `str` | Label containing at least one non-whitespace character. Matching is exact and case-sensitive; do not normalize labels. |
| `duration` | `int` | Strictly positive booked duration; zero is invalid too. |
| `duration_unit` | `str` | Must equal `"minutes"` exactly. Other labels, such as `"hours"`, must be rejected, without conversion. |

The requested room is a nonblank string. The result is an integer number of
booked minutes for that room. An empty export or no matching reservation yields
zero. Leave input records unchanged.

The three new invalid cases are a repeated reservation ID, a unit other than
`"minutes"`, and a negative duration. Validate the entire export before accepting
a total, including records for other rooms. An invalid export must raise
`ValueError` with a useful explanation and produce no successful total report.
Do not silently drop records, deduplicate, substitute zero, or convert units.
The existing nonblank-room rule must also be preserved. Missing/unreadable files
and malformed JSON must remain failures rather than becoming an empty export.

## Reading The File Operations

These supplied operations are scaffolding, not syntax you must invent:

- `from pathlib import Path` supplies an object representing a filesystem path.
- `__file__` identifies this Python file. `Path(__file__).with_name(...)` selects
  the named data file alongside the script, independently of the working directory.
- `read_text(encoding="utf-8")` reads that file into a string.
- `json.loads(...)` parses the JSON string into Python values; it does not check
  uniqueness, positivity, or the required unit.

The script uses only Python's standard library. M02 uses an exercise-local
`.venv`; setup and execution are documented in
[COMMANDS.md](../../COMMANDS.md#create-the-m02-environment).
Running the supplied starter is optional for this reading/planning step; the
execution command and its working directory are in
[COMMANDS.md](../../COMMANDS.md#run-the-m02-starting-script).

## Current Task

Read the two supplied files. Propose your own division into functions, without
implementing it yet. Send a small table in chat with one row per proposed part:

| Proposed part | Responsibility | Input | Return value | Effects or possible failures |
| --- | --- | --- | --- | --- |

Describe inputs/outputs in plain language, including relevant units. A proposed
function name is welcome but no exact Python signature is required yet. Add one
line showing the order in which your parts would cooperate. Account for all
current script activities and the whole-export failure policy.

Keep the starter and data unchanged during this step. We will discuss every
submitted design point before moving to implementation. If an operation is
unclear, name it for a focused explanation.

## Review And Later Steps

This step passes when the learner proposes and explains a coherent division,
the data passed across its boundaries, and the execution order. Discuss design
trade-offs; do not require a hidden preferred naming scheme or architecture.
After review, save the agreed plan with the exercise implementation.

Later steps will guide the learner through annotated function implementation,
designing the three new validations and their tests, and distinguishing unit
tests (one focused part) from integration tests (connected parts). The test data
and validation implementations remain learner-owned. Exception-test syntax and
any new type notation must be explained before their use is assessed.

M02 acceptance additionally requires working exercise code, the saved plan,
the three validations/tests, and an explanation of design/testing demonstrating
independent reasoning or a tested change, under
[LEARNING.md](../../../project-guidance/LEARNING.md#m02--engineering-concepts-and-readiness).
Creating the starter and prompt establishes none of that learner evidence.
