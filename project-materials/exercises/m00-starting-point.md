# M00 Starting-Point Diagnostic

This is a short diagnosis before the lecture, not the M01/M02 exercise or a pass
for M00. Answer without installing or running anything. Explain your reasoning;
state openly when a topic needs refreshing. No solution is supplied before an attempt.

## Prior Preparation

State whether you have already completed any of this module's theory or independent
exercises elsewhere. Identify the material and what you did; it can be reviewed
before repeating completed work.

## Disclosed Example

The following data is fictional. Each row is one separate, valid meeting-room
reservation. `reservation_id` is unique, `room` identifies the room, and
`duration_minutes` is a positive integer duration in minutes. All three rows
belong to the same day. There are no missing values, duplicates, or overlaps.

| reservation_id | room | duration_minutes |
| --- | --- | --- |
| 1 | A | 30 |
| 2 | A | 60 |
| 3 | B | 45 |

## Questions

1. Python: what value does the following function return for
   `total_minutes([30, 60, 45])`? Explain the role of `total`, the loop, and `return`.

   ```python
   def total_minutes(durations):
       total = 0
       for duration in durations:
           total += duration
       return total
   ```

2. SQL (Structured Query Language, a language for querying relational data):
   assuming the table above is named `reservations`, write a query returning
   total reserved minutes separately for each room. Include the expected result.
   Plain-language reasoning is acceptable if you cannot recall the syntax.
3. Git: you have edited a tracked `.py` file locally and have not staged or
   committed the change. Which commands would you use to see the working-tree
   status and inspect the changed lines? Do not commit or push anything.

The review will identify what to refresh in Python, SQL, and Git from these
specific answers. A difficulty or an unknown answer is diagnostic information,
not a failed learning unit.
