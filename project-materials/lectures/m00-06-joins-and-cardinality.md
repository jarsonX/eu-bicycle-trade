# M00 Part 6 — Joins And Cardinality

This follows
[m00-05-pandas-inspection-filtering-and-grouping.md](m00-05-pandas-inspection-filtering-and-grouping.md).
It uses fictional reservations and room descriptions. The examples were checked
against official pandas documentation and reasoned through manually; they were
not executed and no dependencies or project components were added.

## Contents

- [Two Grains And A Shared Key](#two-grains-and-a-shared-key)
- [Enriching Reservations](#enriching-reservations)
- [How Matching Multiplies Rows](#how-matching-multiplies-rows)
- [Uniqueness And Coverage Are Separate](#uniqueness-and-coverage-are-separate)
- [Understanding Check](#understanding-check)
- [References](#references)

## Two Grains And A Shared Key

A join combines related records using a matching condition. Here the goal is to
add each room's building to every reservation, preserving one reservation per
row. All room identifiers are nonmissing, globally identify a room, and match
exactly; each room belongs to one building in this example.

The original complete reservations all belong to one day, have unique reservation
IDs, positive integer durations in minutes, and no overlaps:

| reservation_id | room | duration_minutes |
| --- | --- | --- |
| 1 | A | 30 |
| 2 | A | 60 |
| 3 | B | 45 |

The room lookup is a reference table, with one row per room:

| room | building |
| --- | --- |
| A | North |
| B | South |

Cardinality describes matching multiplicity. One-to-one requires unique join
keys on both sides. One-to-many allows repeated keys on the right but unique
keys on the left. Many-to-one allows repeated keys on the left but unique keys
on the right. Many-to-many permits repeated keys on both sides. These statements
describe uniqueness, not a guarantee that every row finds a match.

Reservations to rooms is the expected many-to-one case: several reservations
can refer to the same unique room description. `room` is a join key in both
tables, but is only the row-identifying key in the lookup. `reservation_id`
remains the reservation key.

## Enriching Reservations

Using the `reservations` DataFrame introduced previously:

```python
rooms = pd.DataFrame({
    "room": ["A", "B"],
    "building": ["North", "South"],
})

enriched = reservations.merge(
    rooms,
    on="room",
    how="left",
    validate="many_to_one",
    indicator=True,
)
```

`on` specifies the shared matching field. A left join retains each left-side
reservation, including those without a lookup match; multiple matches can still
produce multiple output rows. `validate="many_to_one"` checks right-side key
uniqueness and rejects a lookup with repeated room keys. `indicator=True` adds
`_merge`, which records whether a row matched both sources or came only from
one side. All three reservations in the complete example match both sources.

Ignoring the diagnostic column, the expected enriched rows are reservation 1,
A, 30, North; reservation 2, A, 60, North; and reservation 3, B, 45, South.
There are three rows and their durations still sum to 135. The SQL data matching
corresponds to:

```sql
SELECT r.reservation_id, r.room, r.duration_minutes, s.building
FROM reservations AS r
LEFT JOIN rooms AS s ON r.room = s.room;
```

The shown SQL does not itself add the pandas validation or diagnostic indicator.
The example assumes complete keys. With missing keys, pandas can match null
join keys to each other, unlike usual SQL equality-join semantics; validate
required key completeness rather than treating all behavior as identical.

## How Matching Multiplies Rows

Suppose a faulty lookup contains A/North twice and B/South once. Without the
cardinality check, each A reservation matches both A lookup records:

| reservation_id | room | duration_minutes | building |
| --- | --- | --- | --- |
| 1 | A | 30 | North |
| 1 | A | 30 | North |
| 2 | A | 60 | North |
| 2 | A | 60 | North |
| 3 | B | 45 | South |

There are five rows and the summed duration is now 225 minutes. No actual
reservation became longer. The join produced a row for each matching pair,
repeating reservation measures. For a particular matched key, m left rows and
n right rows produce m × n pairs. This is valid matching behavior, but it
violates our intended one-reservation-per-row result.

With `validate="many_to_one"`, pandas rejects the repeated right-side key
instead of returning that multiplied result. Do not change the declared
cardinality to many-to-many merely to suppress the failure. Investigate whether
the lookup is faulty or a different grain/key is actually needed. Likewise,
arbitrary deduplication could discard meaningful conflicting records.

## Uniqueness And Coverage Are Separate

Now suppose the lookup contains only A/North. Its room key is unique, so
many-to-one validation passes. A left join retains reservation 3 but supplies
a missing building and `_merge = "left_only"` for it. An inner join instead
retains matching pairs only, so B's reservation disappears, and the remaining
duration total becomes 90.

Whether unmatched descriptions are allowed is a contract decision. This
enrichment task requires a building for every reservation, so an unmatched room
must be flagged and resolved before a complete building-level report is accepted.
Unique lookup keys alone do not establish full match coverage. An inner join
does not repair missing descriptions; it changes which reservations survive.

For this specific enrichment, review lookup uniqueness, match coverage, output
row count, reservation-ID uniqueness, and the preserved duration sum. These
checks detect relevant failures but do not prove that building labels are true
or that source delivery was complete. Checks follow the intended grain and
meaning; not every legitimate join must preserve counts or sums.

## Understanding Check

Keep the three original reservations. In a new faulty room lookup, A/North
appears once and B/South appears twice; no keys are missing. Perform a left
join on `room` without the cardinality check.

1. How many output rows and what summed duration would you obtain? Explain
   which reservation is repeated.
2. Would adding `validate="many_to_one"` allow this lookup? Explain why.

Reason from the disclosed data; no installation or code execution is needed.
Basic chart construction and interpretation follow in the next lecture part.

## References

Consulted on 2026-10-31. Fictional data and manually derived totals are original
teaching examples. These references do not select a project dependency version.

- [DataFrame.merge](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)
- [Merge, join, concatenate and compare](https://pandas.pydata.org/docs/user_guide/merging.html)
