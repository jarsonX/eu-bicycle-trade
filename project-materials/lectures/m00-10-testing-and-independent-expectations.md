# M00 Part 10 — Testing And Independent Expectations

This follows
[m00-09-errors-logging-and-network-boundaries.md](m00-09-errors-logging-and-network-boundaries.md).
It is theory using fictional reservations. Code examples refer to the simple
`total_minutes` and `require_room_label` functions from earlier lectures; no
application or independent-exercise implementation is supplied. The examples
were reviewed against official documentation, not executed. No package is
installed and no source call is made.

## Contents

- [A Test Makes An Expectation Checkable](#a-test-makes-an-expectation-checkable)
- [Unit And Integration Scope](#unit-and-integration-scope)
- [Independent Expected Results](#independent-expected-results)
- [Invalid Inputs And Edge Cases](#invalid-inputs-and-edge-cases)
- [Fixtures And Temporary Files](#fixtures-and-temporary-files)
- [Replacing The Network In Tests](#replacing-the-network-in-tests)
- [Regression And Test Limits](#regression-and-test-limits)
- [Understanding Check](#understanding-check)
- [References](#references)

## A Test Makes An Expectation Checkable

An automated test runs specified behavior under controlled conditions and checks
an explicit expectation. The expectation comes from the agreed requirement.
For example, our summing helper receives already validated integer minute
durations and should return their sum. The original helper returns zero for
an empty list; that does not imply unavailable source data can be replaced
with an empty list and treated as a verified zero-booking day.

pytest is a Python testing tool that finds and runs test functions and reports
failures. A simple illustrative test is:

```python
def test_total_minutes_adds_all_values():
    durations = [15, 30, 45]
    result = total_minutes(durations)
    assert result == 90
```

The test prepares the input, performs the action, and checks the outcome.
`assert` expresses a condition that must hold in the test; if it does not,
the test fails. The expected 90 is manually derived from the disclosed values,
not obtained from the function being tested. A result of 89 would fail even
if the function raised no exception. The `test_` naming convention helps pytest
discover tests; imports and file layout will be implemented during M01.
Assertions here are test checks, not a replacement for runtime input validation.

## Unit And Integration Scope

A unit test checks a small behavior with controlled dependencies. Testing
`total_minutes` directly with a list isolates addition from file access,
parsing, validation, and report writing. A failure is therefore relatively
easy to locate. The unit is not universally defined as exactly one function;
state what behavior and dependencies the test covers.

An integration test checks collaboration across real components. For our
fictional process, it can read a small actual CSV file, parse the fields,
validate them, calculate room totals, and inspect the output. It can reveal
a reader that drops a row, a wrong column mapping, or a coordinator that
reports success after a failed stage, even when individual arithmetic tests
pass. Such tests can be more costly and failures less localized; use focused
unit checks and a smaller set of meaningful integration scenarios together.

Offline integration is still integration: the local components can be real
while the external network transport is replaced. Declare the boundary so the
test's claim is clear. A unit test with dependencies replaced does not by itself
establish that all those dependencies cooperate in production.

## Independent Expected Results

The following is a poor correctness check for the deterministic helper:

```python
durations = [15, 30, 45]
expected = total_minutes(durations)
assert total_minutes(durations) == expected
```

If the function consistently omits the last duration, both calls can return
the same wrong result and the assertion passes. This does not establish the
required sum. Derive a small expected answer independently from the business
rule and document why it is right. Rewriting the same faulty algorithm in the
test can also reproduce its mistake; independent reasoning is more valuable
than merely using another line of code.

For the three complete reservation rows `(1, A, 15)`, `(2, A, 30)`, and
`(3, B, 45)` on fictional day D, the manually derived room totals are A = 45
and B = 45 minutes. An integration check can inspect those keys and measures,
not just whether an output file exists. Tests should target required behavior
rather than incidental helper names or an exact internal implementation.

## Invalid Inputs And Edge Cases

A happy-path case supplies ordinary valid input. An edge case concerns a boundary
or unusual but important condition, such as one reservation, an empty known
list, or a missing measure. Invalid data is also important to test, but the
expected response must follow the contract rather than an assumption that every
unusual case is an error.

Use the nonblank-label rule from part 8 as an example of checking an expected
failure. Assume `require_room_label` has already been defined as there:

```python
import pytest

def test_room_label_rejects_whitespace():
    with pytest.raises(ValueError):
        require_room_label("   ")
```

`with` establishes a managed block; here `pytest.raises(ValueError)` expects
that exception inside the block. If none is raised, the test fails. An
unexpected different exception also does not satisfy this check. This validates
one defined response, not every possible bad input or the whole report's status.

For process-level critical failures, also check the agreed externally visible
behavior: failure status, a useful diagnostic, and absence of a newly accepted
success output. A message alone does not prove correct control flow. Conversely,
a permitted optional-field warning should not accidentally prevent an otherwise
valid report. Avoid testing incidental message punctuation when the contract
only requires a meaningful explanation.

## Fixtures And Temporary Files

Test data describes a controlled scenario. A pytest fixture is a mechanism for
preparing and supplying data or resources to tests, with cleanup where needed.
It might return the same small reservation sample as a fresh object for each
test, or prepare an input file and a clean output location. In pytest, fixture
functions are marked with `@pytest.fixture`; a test requests one by its argument
name. The `@` notation is a decorator, which marks the function for that
framework behavior. Detailed fixture coding is deferred to hands-on work.

A fixture and a CSV sample are related but not interchangeable concepts: the
fixture can prepare or return the sample; the CSV is the data itself. Share
setup that has a clear reason, while keeping each test's assumptions visible.
Do not let one test silently depend on another having already created a file
or changed a shared list.

pytest's built-in `tmp_path` fixture supplies a distinct temporary directory
for each test. An integration test can create a small input CSV and generated
report there without overwriting a real snapshot or normal report. pytest
manages retention of these directories; immediate deletion after each test is
not guaranteed. Isolating paths does not automatically isolate global variables
or disable the network: control those dependencies separately.

## Replacing The Network In Tests

A test double is a controlled replacement for a dependency. We can replace
the source-transport function with behavior that returns a known response or
raises the same timeout exception the application expects. A lightweight fake
can simulate the source sufficiently for the scenario. pytest's `monkeypatch`
fixture can temporarily replace a referenced function or attribute, with its
changes undone after the test; dependencies can also be supplied explicitly.

Keep the behavior being tested real. To test a coordinator's timeout reaction,
replace the transport boundary, not the entire coordinator with a canned answer.
The real handling code then receives a predictable failure without waiting for
an actual remote outage. This permits checks of attempt limits, failure status,
and output eligibility with no live requests and no artificial long sleeps.

A fake must respect the dependency's relevant interface and failure behavior.
Passing offline tests does not verify the live source's current schema, access,
or availability. Live source audit and bounded acquisition verification are
separate activities, subject to the project's readiness and authorization rules.

## Regression And Test Limits

A regression is a change that breaks previously working behavior. Keeping a
test for a discovered defect helps detect its return after refactoring or a
dependency change. Update expectations when the agreed behavior actually changes,
not merely to make a failing implementation pass.

Repeatable tests control inputs, paths, time-dependent assumptions, and external
services. They should not require a particular test order or today's mutable
source export. A failure is evidence of a mismatch to investigate: the code,
the expectation, the setup, or even an ambiguous requirement can be wrong.
Passing tests establish only the behaviors and cases checked; they do not prove
all data, business interpretations, or real-source integrations correct.

## Understanding Check

1. A fictional day-D CSV has columns `reservation_id`, `room`, and
   `duration_minutes` and exactly these three records: `(1, A, 15)`,
   `(2, A, 30)`, `(3, B, 45)`. IDs are unique; durations are positive integer
   minutes; all data is complete. The required report includes every record
   and gives room-level totals. A direct unit test of the summing helper passes.
   After a reader change, the first CSV record is silently skipped, while the
   other components are unchanged. What additional test or tests would you
   design to detect this? Explain the real components, controlled input, and
   expected checks. A reasoned combination of test levels is welcome; no code
   is required.
2. A local acquisition coordinator is required to attempt a read at most twice
   and report failure without a new success artifact if both reads time out.
   How would you test this behavior offline, without waiting for a real source
   outage? Which dependency would you replace, and what behavior would you keep
   real? Describe the checks rather than implementing them.

Discuss the reasoning first. Any unclear assumptions can be resolved before
written feedback; extensions are evaluated on their actual scope and merit.

## References

Consulted on 2026-11-01. Examples are original teaching material. No tests,
fixtures, network doubles, or production implementation have been executed.

- [pytest getting started](https://docs.pytest.org/en/stable/getting-started.html)
- [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [pytest temporary paths](https://docs.pytest.org/en/stable/how-to/tmp_path.html)
- [pytest monkeypatch](https://docs.pytest.org/en/stable/how-to/monkeypatch.html)
