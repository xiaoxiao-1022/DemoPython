class Student:
    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        if 0 <= age <= 18:
            self._age = age
        else:
            raise ValueError("Age must be between 0 and 18")


s = Student()
s.age = 4

print(s._age)
