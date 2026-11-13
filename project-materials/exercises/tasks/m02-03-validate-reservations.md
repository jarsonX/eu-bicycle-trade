# M02 Step 3 — Implement Reservation Validation

Prerequisite: the loader stage and its record-type/import-guard corrections
have been reviewed. Continue in
[mixed_reservations.py](../workspaces/m02-reservations/mixed_reservations.py),
in `project-materials/exercises/workspaces/m02-reservations/`.
The shared input contract is in
[m02-01-responsibilities-and-interfaces.md](m02-01-responsibilities-and-interfaces.md#input-and-contract).

## Contents

- [Interface](#interface)
- [Task](#task)
- [Hint](#hint)
- [Review Criterion](#review-criterion)

## Interface

Write a function named `validate_reservations`.

| Item | Annotation | Meaning |
| --- | --- | --- |
| `reservations` argument | `list[Reservation]` | The complete parsed export for the supplied fictional day. |
| Return value | `None` | Successful validation completes normally without a data result. |

The return annotation `-> None` expresses that a successful call returns
Python's `None` value. Reaching the end of the function produces that value.
If a required rule is violated, raise `ValueError` with an explanation that
identifies the rule and the affected reservation where applicable.

Required fields and basic types are guaranteed by this exercise. Validate the
business rules on the actual argument. Preserve the supplied list and records.

## Task

Check the following rules across the complete export.

1. Every `reservation_id` is unique across all rooms.
2. Every `duration_unit` equals `"minutes"` exactly.
3. Every `duration` is strictly positive, so zero and negative values fail.
4. Every `room` contains at least one non-whitespace character.

An empty list is valid. A rule violation stops validation with `ValueError`.
The order in which rules are checked is your design choice.
Data validation here takes place in memory. Loading belongs to the existing
loader, and output belongs to the main-guard code.

Under `if __name__ == "__main__"`, call the validator after `load_reservation`
and before the current data print. Let validation errors interrupt that flow.
Keep the supplied data file as the valid baseline. Use the existing execution
command in [COMMANDS.md](../../COMMANDS.md#run-the-m02-starting-script).

Submit your saved validator for review. Dedicated automated tests will follow
discussion of the implementation and exception-test syntax.

## Hint

Consider which rule requires knowledge of more than one reservation. The other
rules can be checked using the fields of an individual record. Choose how to
organize those checks before writing the function body.

## Review Criterion

The annotated function implements the four disclosed rules, accepts an empty
list, preserves its inputs, and observes the successful-return/error contract.
It validates all rooms independently of `requested_room`. The guarded flow
validates before printing the data. Review is limited to this validation step.
