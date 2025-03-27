class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def isAdult(self):
        return self.__age >= 18


xh = Person("xh", 18)
print(xh.isAdult())
