# Pipe

`pipe` is a simple implementation functional style function piping in Python.

```python3
>>> from pipe import Pipe
>>> from operator import add, sub, mul, truediv as div
>>> from functools import partial
>>> result = Pipe() | partial(add, 2, 3) | partial(mul, 10) | partial(div, 1250) | partial(sub, 45) | int
>>> print(result.value)
20
```
