# Function Syntax And Type Annotations

Requested support for
[m01-07-first-function.md](../exercises/tasks/m01-07-first-function.md).
The learner asked for a model of a different function and required argument
and return annotations. The example formats text using a boolean option;
it does not aggregate or filter reservation records.

## A Different Function

Assume `name` is a nonempty string and `formal` is a boolean, `True` or `False`.
The function returns a greeting string.

```python
def make_greeting(name: str, formal: bool) -> str:
    if formal:
        greeting = f"Good morning, {name}."
    else:
        greeting = f"Hi, {name}!"
    return greeting
```

Example calls and their manually derived results:

```python
print(make_greeting("Jan", True))   # Good morning, Jan.
print(make_greeting("Jan", False))  # Hi, Jan!
```

## Read The Syntax

`def` introduces a function definition. `make_greeting` is the function name.
`name` and `formal` are parameters; the actual values are supplied at a call.
`name: str` declares text input, and `formal: bool` declares boolean input.
`-> str` declares a string result; it does not produce the result itself.

The colon starts an indented code block. Indentation marks which statements
belong to the function and which belong to the `if` or `else` branch. `if formal`
selects the first branch when the boolean is true; otherwise `else` is used.

An f-string begins with `f`; braces insert a value into the surrounding text.
`greeting` is a local variable holding the selected text. `return greeting`
returns that value to the caller and ends this call. The outer `print` in the
example displays the returned string; printing is not part of the function.

Python does not automatically enforce these type annotations at runtime.
They communicate a contract and can be checked by editor/static-analysis tools;
they do not replace validation of actual values or business constraints.

## Type Notation For The Current Exercise

For the current first attempt, the required argument/result annotations are:

| Item | Accepted baseline annotation | Meaning |
| --- | --- | --- |
| `reservations` argument | `list[dict[str, int | str]]` | A list of dictionaries with string keys and integer-or-string values. |
| `room` argument | `str` | The requested room identifier as text. |
| Result | `int` | Total minutes as an integer, including zero. |

Read the nested annotation from the inside out: `int` is an integer, `str` is
text, and `int | str` permits either. `dict[key_type, value_type]` describes the
keys and values of one dictionary. `list[element_type]` describes the containing
list. No imports are required for these built-in types in Python 3.15.

This is a deliberately broad introductory annotation: it does not associate
particular keys with particular value types. The disclosed data contract still
establishes that `duration_minutes` is an integer and `room` is text. More precise
record typing can be introduced later. A passing static type-checker run is not
required for this first attempt; do not add casts or runtime checks merely to
compensate for this broad annotation. Equivalent, more precise annotations may
be discussed if the learner proposes them.

The learner still writes the reservation function and derives its expected
results. This example supplies syntax support, not the calculation algorithm.
The greeting outputs were reasoned through, not executed as learner evidence.

Source: [Python type annotations](https://docs.python.org/3/library/typing.html).
