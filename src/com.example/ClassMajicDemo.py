import time


class Slate:
    def __init__(self, value):
        self.value = value
        self.last_change = time.asctime()
        self.history = {}

    def change(self, new_value):
        self.history[self.last_change] = new_value
        self.value = new_value
        self.last_change = time.asctime()

    def print_change(self):
        print("changeLog for Slate object")
        for k, v in self.history.items():
            print("%s\t %s" % (k, v))

    def __getstate__(self):
        return self.value

    def __setstate__(self):
        self.history = state
        self.value, self.last_change = None, None


slate = Slate(111)
slate.change(2222)

slate.print_change()
