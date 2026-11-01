# M00 Part 8 — Type Hints And Runtime Validation

This follows [m00-07-charts-and-interpretation.md](m00-07-charts-and-interpretation.md)
and continues M00 theory using fictional meeting-room data. The examples were
reviewed against official documentation and reasoned through, not executed.
No interpreter, type checker, or dependency was installed or selected. The
`list[int]` notation in the examples requires Python 3.9 or later.

## Contents

- [Types And Annotations](#types-and-annotations)
- [Static Checking](#static-checking)
- [What Annotations Do At Runtime](#what-annotations-do-at-runtime)
- [Valid Types And Valid Data](#valid-types-and-valid-data)
- [A Runtime Value Check](#a-runtime-value-check)
- [Combining The Safeguards](#combining-the-safeguards)
- [Understanding Check](#understanding-check)
- [References](#references)

## Types And Annotations

A type describes the kind of value and the operations associated with it.
Python's `int` represents integers, `float` floating-point numbers, `str` text,
and `bool` the truth values `True` and `False`. A list is an ordered collection;
`list[int]` expresses a list whose elements are expected to be integers.

A type annotation, also called a type hint, records an expected type in code.
The reservation-summing function can be written as:

```python
def total_minutes(durations: list[int]) -> int:
    return sum(durations)
```

`durations` is the parameter name. The annotation after its colon describes
the expected argument type. `-> int` describes the expected returned type.
The function still receives an argument and sums it as before. The annotations
document its interface for readers, editors, and checking tools. They do not
encode positive values, minute units, unique reservation IDs, or source coverage.

## Static Checking

Static analysis examines code without running its computation. A static type
checker, such as mypy or Pyright, uses annotations and inferred types to detect
inconsistent uses. For a checked, annotated call, supplying a list of text
values where a list of integers is required can be reported before execution.
Likewise, a function promising an integer but returning text has a detectable
return-type inconsistency.

The tool must actually run over the relevant code with an appropriate
configuration. Unchecked code, insufficient type information, dynamic inputs,
or exclusions can limit its conclusions. An editor warning is not runtime
enforcement, and a successful type-checking run is not proof that calculations
or real data are correct. Type checker choice and configuration will be made
later; no successful check is claimed for these lecture examples.

## What Annotations Do At Runtime

Runtime means the period when Python actually executes the code. Plain Python
does not enforce function annotations merely because they are present.
Calling `total_minutes([30, -20])` executes addition and produces 10 despite
the negative value; the integers fit the simple annotated type.

Passing text values such as `["30", "60"]` is inconsistent with the annotation.
Plain Python still attempts the function body; the shown `sum` operation then
raises a `TypeError` when it cannot add text to its initial integer total.
The arithmetic operation causes that error, not an annotation check at the
function boundary. Annotations also do not convert `"30"` into `30`.

The broader distinction is that runtime may allow an annotated mismatch if the
body can execute it. The existence of an annotation alone guarantees neither
rejection nor conversion of incorrect input.

## Valid Types And Valid Data

Our reservation contract requires positive integer durations in minutes. A
negative integer has a compatible numerical type but violates the allowed
value range. A list of integer hour durations also satisfies `list[int]` while
violating the required unit. Simple annotations do not supply or verify that
source metadata.

The SQL analogy is an integer column versus a constraint such as requiring
a value greater than zero. Choosing a numerical column type does not, by
itself, require a positive value. Likewise, an expected reservation ID type
does not establish uniqueness. A general DataFrame annotation also does not
establish all required column names, units, keys, or completeness rules.

Runtime validation checks the actual delivered data against its contract. It
can check structure, values, keys, and explicit unit metadata, then produce
the failure or warning behavior agreed for a violation. It cannot infer the
true unit merely because the numbers look plausible. Reliable source evidence
and business definitions remain necessary.

## A Runtime Value Check

Consider a separate small value rule: a room label must contain a non-whitespace
character. For this illustration, the input has already been checked to be a
Python string; this function demonstrates the next value check:

```python
def require_room_label(room: str) -> str:
    if room.strip() == "":
        raise ValueError("Room label must not be blank.")
    return room
```

`strip()` returns the string without leading and trailing whitespace. Comparing
that result with `""` detects an empty or whitespace-only label. It does not
modify the original string or silently normalize the returned label. A string
containing three spaces fits the `str` annotation but triggers this value check.

`raise` signals an exception, an event interrupting normal execution.
`ValueError` is the built-in exception conventionally used for an unacceptable
value of an otherwise appropriate type. On this branch, execution does not
reach the normal return. Exception handling will be taught in part 9.

This is one value rule, not a complete raw-input validator: it assumes the
input type was already established and does not establish that the room exists
in the room lookup. Keep the rule's actual guarantee narrower than the full
data contract. This demonstration does not provide the independent M02
exercise's duplicate-ID, wrong-unit, or negative-duration implementations.

## Combining The Safeguards

Annotations express the intended programming interface. Static checking looks
for type inconsistencies in the code it examines. Runtime validation checks
actual inputs against specified data requirements. Tests, covered in part 10,
check behavior on selected examples. Each contributes evidence with a defined
scope; none replaces the others or the source audit.

Validate external input at the boundary before relying on its internal contract.
Keep ordinary functions' expected inputs clear rather than duplicating the
entire source validation in every arithmetic helper. At meaningful boundaries,
preserve the guarantees needed by the next responsibility. A validator also
needs appropriate tests because the validation code can itself be wrong.

## Understanding Check

1. Consider this entire plain Python function, with no decorators, runtime
   checking framework, or additional validation:

   ```python
   def reservation_count() -> int:
       return "3"
   ```

   What inconsistency can a static type checker identify? Does Python itself
   reject the returned value solely because of `-> int` when this function runs?
2. A function expects a `list[int]` of durations in minutes. Two fictional source
   exports both contain integer durations, but one source documents minutes
   and the other documents hours. With only the simple `list[int]` annotation,
   can a type checker identify the unit mismatch? What source information and
   processing rule are needed before using those values together?

Explain conceptually; no execution, installation, or code implementation is
required. If a condition is unclear, clarify it before answering. These checks
do not establish independent M01/M02 readiness.

## References

Consulted on 2026-11-01. Examples are original teaching material; no project
dependency version is selected and no runtime/type-checker result is claimed.

- [Python type hints](https://docs.python.org/3/library/typing.html)
- [mypy getting started](https://mypy.readthedocs.io/en/stable/getting_started.html)
- [Python errors and exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python built-in exceptions](https://docs.python.org/3/library/exceptions.html#ValueError)
