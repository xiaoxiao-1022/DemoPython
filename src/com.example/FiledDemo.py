import numbers


class Field:
    pass


class IntField(Field):
    def __init__(self, name):
        self.name = name
        self.type = None

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Number):
            raise ValueError("Only numbers are accepted")
        self._value = value


class strField(Field):
    def __init__(self, name):
        self.name = name
        self.type = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Only strings are accepted")
        self._value = value
