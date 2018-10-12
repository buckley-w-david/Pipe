from functools import partial
import typing

__version__ = "0.2.0"


class __Singleton:
    """
    Single literally any value could be reasonably returned from an arbitrary
    function call, we create our own singleton object that signals the start of
    sequence of piped calls. This allows for the following pattern:

        >>> Pipe() | partial(func1, value1) | partial(func2, value2) | ...

    Instead of requiring the first function call to break the pattern, ie:

        >>> Pipe(func1(value1)) | partial(func2, value2) | ...
    """

    pass


empty = __Singleton()


class lpartial(partial):
    """
    Convenience partial function implementation for inserting additional arguments on the left
    instead of on the right as with the implementation in functools

        >>> from operator import sub
        >>> Pipe() | lpartial(sub, 2)(10)
        Pipe(8)

    """

    def __call__(self, *args, **keywords):
        if not args:
            raise TypeError("descriptor '__call__' of partial needs an argument")
        newkeywords = self.keywords.copy()
        newkeywords.update(keywords)
        return self.func(*args, *self.args, **newkeywords)


class Pipe:
    """
    """

    def __init__(self, value=empty):
        self.value = value

    def __or__(self, func: typing.Callable):
        if self.value is empty:
            return Pipe(func())
        else:
            return Pipe(func(self.value))

    def __repr__(self):
        return "Pipe(%s)" % repr(self.value)

    def __eq__(self, other):
        return isinstance(other, Pipe) and self.value == other.value
