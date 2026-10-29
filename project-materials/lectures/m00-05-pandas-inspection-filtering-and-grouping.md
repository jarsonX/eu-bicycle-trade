# M00 Part 5 — pandas Inspection, Filtering, And Grouping

This follows
[m00-04-environment-configuration-and-notebook-state.md](m00-04-environment-configuration-and-notebook-state.md).
It is a conceptual lecture using fictional data, not an independent exercise or
project implementation. The examples were checked against official pandas
documentation; they were not executed in the repository and require pandas
in the intended environment. No package installation is requested here.

## Contents

- [DataFrame And Disclosed Data](#dataframe-and-disclosed-data)
- [Inspect Before Calculating](#inspect-before-calculating)
- [Selecting Rows And Columns](#selecting-rows-and-columns)
- [Grouping And Meaning](#grouping-and-meaning)
- [Understanding Check](#understanding-check)
- [References](#references)

## DataFrame And Disclosed Data

A DataFrame is a pandas object representing a two-dimensional table with named
columns and labelled rows. A Series represents one labelled dimension, such as
a selected column. Neither object automatically enforces a database primary key.
The row index labels are not automatically the business key `reservation_id`.

For the example, one row is one reservation, all reservations are for the same
day, IDs are globally unique, durations are positive integer minutes, and there
are no missing values, duplicates, or overlaps:

```python
import pandas as pd

reservations = pd.DataFrame({
    "reservation_id": [1, 2, 3],
    "room": ["A", "A", "B"],
    "duration_minutes": [30, 60, 45],
})
```

`pd` is an alias for the imported pandas module. The dictionary inside braces
maps each column name to its list of values. Values at the same position form
one row. The default row labels are 0, 1, and 2; reservation IDs are 1, 2, and 3.
An alias or a variable name does not create a separate database table.

## Inspect Before Calculating

A method is a callable operation belonging to an object, such as
`reservations.head()`. An attribute such as `reservations.shape` exposes a
property without a method call. Useful inspection operations include:

| Expression | What it shows |
| --- | --- |
| `reservations.head()` | The first five rows by default, or all rows when fewer exist |
| `reservations.shape` | Number of rows and columns, here `(3, 3)` |
| `reservations.info()` | A printed overview of columns, types, and nonmissing counts for this small table |
| `reservations.dtypes` | Each column's data type |
| `reservations.isna().sum()` | Number of missing values in each column |

`isna()` produces boolean indicators: `True` for missing values and `False`
otherwise. Summing these indicators by column counts missing values. A number
stored as text is not a missing value; checking missingness does not replace
checking types or parsing. This disclosed sample has no missing values.
`info()` prints a description and returns `None`, rather than returning a new
DataFrame. Inspecting a few rows with `head()` cannot establish full-data quality.

Check repeated expected keys explicitly rather than dropping rows:

```python
reservations.duplicated(subset=["reservation_id"]).sum()
```

`subset` specifies the columns used for comparison. With the default behavior,
the first occurrence is marked `False` and additional occurrences of the same
key are marked `True`; summing counts repeated occurrences beyond the first.
The sample's expected result is zero. This expression diagnoses duplicates but
does not enforce uniqueness or stop a pipeline. It also cannot prove correct
units or complete source delivery.

## Selecting Rows And Columns

Filtering selects rows that satisfy a condition. Selecting columns determines
which fields appear in the result. Compare with SQL's `WHERE` and `SELECT`:

```python
room_a = reservations.loc[
    reservations["room"] == "A",
    ["reservation_id", "duration_minutes"],
]
```

`reservations["room"]` selects a Series. Comparing it with `"A"` creates a
boolean mask: a true/false decision for each row, here `True, True, False`.
The `.loc[row_selector, column_selector]` expression uses that mask to retain
matching rows and uses the list of names to select columns. Its result has
reservation 1 for 30 minutes and reservation 2 for 60 minutes.

```sql
SELECT reservation_id, duration_minutes
FROM reservations
WHERE room = 'A';
```

Filtering retains the original grain: one row still represents one reservation.
It creates a selected result; the shown expression does not remove reservations
from the original object or rewrite the preserved source snapshot.

## Grouping And Meaning

Grouping assigns rows to groups, then an aggregation such as a sum combines
values within each group. For the complete sample:

```python
room_totals = (
    reservations.groupby("room", as_index=False)["duration_minutes"]
    .sum()
)
```

`groupby("room")` defines groups, `["duration_minutes"]` selects the measure,
and `.sum()` performs the calculation for each group. `as_index=False` keeps
the group key as a regular output column instead of making it the row index.
This corresponds to:

```sql
SELECT room, SUM(duration_minutes) AS duration_minutes
FROM reservations
GROUP BY room;
```

The manually derived results are A = 90 and B = 45 minutes. Grain has changed
to one room for the sample day. The calculation assumes the explicitly disclosed
complete, comparable, valid inputs. The existence of a returned DataFrame is
not evidence that those assumptions hold on a different dataset. Missingness,
units, duplicate keys, and coverage still require contract checks.

Filtering before grouping changes which reservations contribute. For example,
restricting the input to reservations longer than a threshold answers a question
about that subset, not automatically about all reserved time. Label the result
according to the actual selection. Joins and charts will be covered next.

## Understanding Check

Use exactly the three disclosed reservations and read this code conceptually:

```python
selected = reservations.loc[reservations["duration_minutes"] >= 45]
result = selected.groupby("room", as_index=False)["duration_minutes"].sum()
```

What totals will appear for A and B, and what does one result row represent?
Can the result be described as the total of all reservations for each room?
Explain which input records contribute. No installation or execution is needed.

## References

Consulted on 2026-10-29; these are technical references, not a selected project
dependency version. Fictional data and manually reasoned results are original
teaching examples; no documentation text is quoted.

- [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [DataFrame.info](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html)
- [DataFrame.duplicated](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html)
- [DataFrame.loc](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)
- [DataFrame.groupby](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)
