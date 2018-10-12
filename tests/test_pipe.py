from operator import mul, add, sub, truediv as div
from functools import partial
from pipe import Pipe
from pipe import __version__

from hypothesis import given
from hypothesis.strategies import floats, integers


def test_version():
    assert __version__ == '0.1.0'


def piped_arithmatic(x, y):
    return Pipe() | partial(add, x, y) | partial(mul, x) | partial(sub, y)

def normal_arithmatic(x, y):
    return (y-(x*(x + y)))


@given(integers(), integers())
def test_arithmatic_int(x, y):
    assert piped_arithmatic(x, y).value == normal_arithmatic(x, y)

@given(floats(allow_nan=False, allow_infinity=False), floats(allow_nan=False, allow_infinity=False))
def test_arithmatic_float(x, y):
    assert piped_arithmatic(x, y).value == normal_arithmatic(x, y)

@given(integers(), floats(allow_nan=False, allow_infinity=False))
def test_arithmatic_mixed(x, y):
    assert piped_arithmatic(x, y).value == normal_arithmatic(x, y)
