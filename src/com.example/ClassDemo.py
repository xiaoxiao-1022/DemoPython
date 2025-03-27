class Animal:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("I am a " + self.name + "!")


print("__name__ 的值为: " + __name__)
animal = Animal("Bob")
animal.run()
Animal.run(animal)
