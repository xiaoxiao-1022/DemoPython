# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print('Eating')
#
#     @staticmethod
#     def sleep():
#         print('Sleep')
#
#     @classmethod
#     def jump(cls):
#         print('Jump')
#
#
# dog = Animal('Bob');
# dog.eat()
# dog.sleep()
# dog.jump()


class Demo:
    def __init__(self):
        self.name = 1
        self._names = 11
        self.__age = 111


demo1 = Demo()
print(demo1.name)
print(demo1._names)
print(demo1._Demo__age)
print(dir(demo1))
