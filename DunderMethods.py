""" object"""


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person({self.name})"

    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid argument")
        self.name = self.name*x

    def __call__(self, y):
        print("called this function", y)


p = Person("Tim")
p(4)
print(p)