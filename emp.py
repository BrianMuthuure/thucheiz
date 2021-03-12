
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)


emp_1 = Employee('Brian', 'Muthuure')


print(emp_1.email)
print(emp_1.fullname)
