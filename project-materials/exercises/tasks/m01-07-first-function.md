# M01 Step 7 — Write A Reservation Calculation Function

Prerequisites: the exercise environment and pytest startup are available;
dependencies and assisted setup documentation are recorded under
[m01-06-dependencies-and-setup-notes.md](m01-06-dependencies-and-setup-notes.md).

At the learner's request, use the structurally different greeting example in
[m01-01-function-syntax-and-type-annotations.md](../../lectures/m01-01-function-syntax-and-type-annotations.md)
for syntax support. Argument and return annotations are now required.

## Inputs And Assumptions

The following data is fictional. All reservations belong to the same day D.
Each dictionary is one separate reservation; the outer list contains the
reservations supplied to the function.

```python
reservations = [
    {"reservation_id": 1, "room": "A", "duration_minutes": 20},
    {"reservation_id": 2, "room": "B", "duration_minutes": 35},
    {"reservation_id": 3, "room": "A", "duration_minutes": 40},
    {"reservation_id": 4, "room": "B", "duration_minutes": 15},
]
```

- `reservation_id`: unique integer reservation identifier.
- `room`: nonempty string room identifier; matching is exact and case-sensitive.
- `duration_minutes`: positive integer booked duration in minutes.
- Records are valid and complete, with no duplicate identifiers, missing values,
  cancellations, or overlapping reservations. The input list may be empty.
- The calculation concerns booked minutes for the supplied day, not an occupancy
  percentage or attendance. No additional calendar or room lookup is required.

A dictionary holds named key/value pairs. For a single reservation dictionary
named `reservation`, `reservation["room"]` reads its room value. The argument
`room` separately identifies the room requested by the caller.

## Task

Create `reservations.py` yourself inside
`project-materials/exercises/workspaces/m01-reservations/`, outside `.venv`.
Define a function named `total_minutes_for_room` with arguments `reservations`
and `room`.

The function must:

1. Accept a list with the disclosed record structure and the requested room string.
2. Return an integer total of booked minutes for that room in the supplied list.
3. Return `0` when there are no matching reservations, including an empty list.
4. Leave the input unchanged. Return the result rather than printing it inside
   the calculation function.

Use plain Python; no external library is needed. Invalid-input validation,
file reading, reporting, and automated tests are outside this first attempt.
Annotate both arguments and the return type. The explained introductory baseline
is `list[dict[str, int | str]]` for `reservations`, `str` for `room`, and `int`
for the result. More precise equivalents can be discussed; a passing static
type-checker run is not required at this step. The function should compute from
its arguments rather than hardcode results or depend on a global sample list.

First derive expected results manually for the supplied data with rooms A, B,
and C, and for an empty list with room A. Then describe your intended approach
in one or two sentences and attempt the function. A simple loop is acceptable.
You may send the plan first if syntax is blocking you; name the specific gap
so the mentor can give a targeted hint before supplying more help.

Send the manually derived results, your approach, and your code or the saved
file path. You are not required to set up an execution/import command unaided
before it has been explained. The mentor will review the attempt, then guide
running it and writing a pytest test in a subsequent step.

## Review Criterion

The learner explains the manually derived expectations and writes code matching
the disclosed contract, with annotations on both arguments and the return type.
Review any gaps through gradual hints, without replacing
the implementation. If assistance is needed, distinguish supplied explanations
from independently written code.

This prompt provides input data and requirements, not the implementation or
expected numeric answers. No learner attempt, execution, passing test, completed
M01, or readiness for main-project work is established by creating this file.
