import typing

__version__ = '0.1.0'

"""
Single literally any value could be reasonably returned from an arbitrary
function call, we create our own singleton object that signals the start of
sequence of piped calls. This allows for the following pattern:

    > Pipe() | partial(func1, value1) | partial(func2, value2) | ...

Instead of requiring the first function call to break the pattern, ie:

    > Pipe(func1(value1)) | partial(func2, value2) | ...
"""
class __Singleton:
    pass
empty = __Singleton()

"""
"""
class Pipe:
    def __init__(self, value=empty):
        self.value = value

    def __or__(self, func: typing.Callable):
        if self.value is empty:
            return Pipe(func())
        else:
            return Pipe(func(self.value))

    def __repr__(self):
        return 'Pipe(%s)' % repr(self.value)
