from collections.abc import Iterable


class Array:
    mylist = [0, 1, 2]
    index = 0

    def _iter_(self):
        return self

    def _next_(self):
        if self.index <= len(self.mylist) - 1:
            value = self.mylist[self.index]
            self.index += 1
            return value
        raise StopIteration


my_itertor = iter(Array())
print(isinstance(my_itertor, Iterable))
print(next(my_itertor))
print(next(my_itertor))
print(next(my_itertor))
print(next(my_itertor))
