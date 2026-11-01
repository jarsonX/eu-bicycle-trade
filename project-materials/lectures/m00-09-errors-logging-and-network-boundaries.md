# M00 Part 9 — Errors, Logging, And Network Boundaries

This follows
[m00-08-type-hints-and-runtime-validation.md](m00-08-type-hints-and-runtime-validation.md).
It remains theory with fictional reservations. Code is illustrative and was
reviewed against documentation, not executed. Requests is discussed as an
example, not selected or installed as a project dependency. No source requests
are made and no acquisition or pipeline component is implemented.

## Contents

- [Failure, Warning, And Contract](#failure-warning-and-contract)
- [Exceptions And Handling](#exceptions-and-handling)
- [Logs And Control Flow](#logs-and-control-flow)
- [The Network Boundary](#the-network-boundary)
- [Timeouts And Bounded Retries](#timeouts-and-bounded-retries)
- [Understanding Check](#understanding-check)
- [References](#references)

## Failure, Warning, And Contract

A failure means the requested operation cannot meet its requirements. A warning
records a condition under which an explicitly permitted result can still be
produced. Severity follows the contract rather than whether an exception is
technically easy to suppress.

For this lecture, require complete, validated reservation data before reporting
an exact full-day total. A required blank room label prevents that result. In
a separate optional-field rule, an absent descriptive note is permitted but
must be recorded as a warning; it does not affect duration calculations. These
are explicit example policies, not universal rules about every missing value.

A syntax error prevents code from being parsed correctly. An exception signals
a problem encountered during execution, such as a missing input file, failed
conversion, or an explicit validation rejection. A logical error can instead
produce a plausible but wrong result without raising any exception, as in the
duplicated-join sums from part 6.

## Exceptions And Handling

`raise` signals an exception. `try` surrounds an operation whose failures we
intend to handle. A matching `except` receives a particular exception and
allows an appropriate response. If a matching handler finishes normally,
execution can continue after the block; catching an exception does not
automatically mark the whole run as failed.

For the straight-line snippet in the understanding check, the final print does
execute. Do not generalize this to "only stopping the entire program can skip
a later print": inside a function, returning early can skip later statements
in that function while the caller and rest of the program continue.

Using the previous part's `require_room_label`, which raises `ValueError` for
an empty or whitespace-only string:

```python
try:
    room = require_room_label("   ")
except ValueError as error:
    print(f"Validation failed: {error}")
    raise
```

`as error` binds the caught exception so the message can use it. The `f` prefix
formats the value inside braces into a string. The bare `raise` re-raises the
current exception, leaving this handler's normal path. A higher-level caller
can handle it; if it reaches the top unhandled, execution fails. This fragment
reports a failure rather than silently allowing later success output.

Handle failures at a level able to decide what to do, usually the coordinator
for a complete analysis. A narrow validator need not decide the wording of an
entire report. Catch specific expected exceptions. Broadly catching everything
and continuing can conceal programming defects as well as expected input
failures. A deliberate top-level failure handler may catch broadly to report
an unexpected failure, but must still preserve failure status and diagnostics.

An empty dataset, a zero total, or an older snapshot is not an automatic
replacement for unavailable required input. A fallback must be an explicit
policy preserving the requested meaning. For a command-line process, success
normally uses exit status zero, and failure a nonzero status, so automated
callers can distinguish them. Preserve earlier valid reports without presenting
them as results of a failed current run; do not publish a new success artifact
or a success message after critical failure.

An explicit "data unavailable" diagnostic is compatible with a failed full
report. An accepted partial analytical report is a separate allowed mode that
requires an agreed scope, quality labels, and calculation eligibility rules.
Practical difficulty does not itself authorize that mode when the stated
contract requires complete data and forbids fallback.

## Logs And Control Flow

Logging records events during execution. A useful record identifies the stage,
snapshot or run, event severity, relevant counts, and a concise reason. This
helps diagnose a failure without replaying the run from memory. It complements
the source manifest rather than replacing preserved input or validation.

Python's standard `logging` module provides severity levels:

| Level | Example role |
| --- | --- |
| `DEBUG` | Detailed diagnostic context |
| `INFO` | A stage started or completed, with counts |
| `WARNING` | A permitted limitation that must remain visible |
| `ERROR` | An operation could not complete as required |
| `CRITICAL` | A severe failure affecting continued operation |

For a small standalone demonstration, configuration and a log call can look like:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Validated %d reservations", 3)
```

`basicConfig` supplies basic logging configuration; `getLogger` obtains a logger,
and `__name__` identifies the current module. `%d` is a placeholder for the
integer supplied to the log call. In a real application, configure logging at
the entry point rather than separately in every helper module. Without suitable
configuration, some lower-severity messages may not appear; Python's default
threshold is `WARNING`.

`logger.error(...)` records an error-level event but does not itself raise an
exception or stop execution. Likewise, printing an error message does not
change process success status. Actual failure behavior requires control flow
such as propagating an exception and an appropriate top-level response.

Keep logs useful and proportionate: counts and stage identifiers rather than
complete source responses. Do not include credentials, reusable authenticated
links, or sensitive input values. Do not disable certificate verification to
make a failing source connection appear to work.

## The Network Boundary

A boundary separates our controlled local processing from an external system.
A source call can fail because connection cannot be established, a response
does not arrive in time, access is refused, the server fails, or the received
content is not the expected dataset. Distinguish these from domain validation
failures in data that was successfully downloaded.

Successful transport alone does not establish correct content: an error page
is not a reservation table. Check response status, expected format and parsing,
then the data contract. Acquisition preserves a new identified valid snapshot;
calculation from an existing snapshot does not need a fresh source call.
Keep older snapshots intact and do not disguise a failed fetch as a valid empty
new snapshot. Fake source responses in tests will be introduced in part 10.

## Timeouts And Bounded Retries

A timeout limits a defined waiting operation so the process does not wait
indefinitely. Know the client's exact semantics. In Requests, an illustrative
`timeout=(3, 10)` configures connection and read waiting limits, respectively,
in seconds. The read limit concerns waiting for received data, not a guaranteed
ten-second deadline for the entire download. Multiple network stages and
attempts can make the overall elapsed time longer.

A retry repeats an attempt. Bounded retries can help with transient failures
for safe read operations, but need a finite attempt/time budget and waits
between attempts rather than a tight infinite loop. Repeating an access-denied
request or a deterministic invalid data calculation does not fix its cause.
When a required acquisition still fails after the allowed attempts, retain
failure status instead of inventing input. Real write operations also require
reasoning about whether a previous attempt already had an effect before retrying;
this lesson uses read-only acquisition scenarios.

For diagnosis, record the run identifier, requested source scope/day, operation
stage, attempt count, configured limits, actual elapsed time, and exception
type/message, with sensitive values excluded. A network timeout is the known
symptom in this example; the learner is not expected to infer an undisclosed
root cause. Connection versus read timeout can narrow the investigation.
A Requests network timeout does not directly measure time spent in local
calculations before the request; slow remote processing can contribute to
waiting for a response. Client logs alone may not establish why a remote server
is slow; source-side monitoring or additional evidence may be required.

## Understanding Check

1. The contract requires a nonblank room label before a successful report.
   Assume `require_room_label("   ")` raises `ValueError` as in part 8,
   logging is configured, and no other failures occur:

   ```python
   try:
       room = require_room_label("   ")
   except ValueError:
       logger.error("Invalid room label")

   print("Report completed successfully")
   ```

   Will the final `print` execute? Does the error-level log satisfy the
   contract's failure requirement? Explain what is wrong with the control flow.
2. A new full-day report requires a complete snapshot for fictional day D.
   Downloading it fails on both allowed read attempts because of timeouts.
   No valid snapshot for D is available, and the rules do not permit a fallback.
   A proposal is to use an empty table and report a total of zero with success
   status. Is that valid? Describe the appropriate failure behavior and which
   diagnostic fields should be recorded in logs. You are not asked to identify
   a root cause from the timeout symptom alone.

Answer conceptually. No live source calls, code execution, or implementation
are required; all constraints needed for the answers are stated above.

## References

Consulted on 2026-11-01. Examples are original fictional teaching material.
No runtime, network, or logging output is claimed to have been executed.

- [Python errors and exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python logging HOWTO](https://docs.python.org/3/howto/logging.html)
- [Requests quickstart: timeouts and errors](https://requests.readthedocs.io/en/latest/user/quickstart/#timeouts)
- [Requests advanced usage: timeouts](https://requests.readthedocs.io/en/latest/user/advanced/#timeouts)
