# class Person:
#     def __init__(self, name):
#         self.name = name
#     def speck(self):
#         print("Hello " + self.name + "!")
#
# class Student(Person):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def speck(self):
#         print("Hello child" + self.name + "!")
#
# xh = Student(name="xh")
# xh.speck()

# class D:pass
# class C(D):pass
#
# class B(C):
#     def show(self):
#         print("i am B")
#
# class G:pass
# class F(G):pass
#
# class E(F):
#     def show(self):
#         print("i am E")
#
#
# class A(B, E):pass
#
#
# a = A()
# a.show()


class A(object):
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.__mro__)
