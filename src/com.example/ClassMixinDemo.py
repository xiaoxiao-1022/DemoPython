class Vehicle(object):
    pass


class PlaneMixin(object):
    def fly(self):
        print("I am flying")


class Airplane(object, PlaneMixin):
    pass
