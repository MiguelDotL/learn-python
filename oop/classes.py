class Employee():

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = ('{}.{}@company.com').format(self.first, self.last)

    def full_name(self):
        return'{} {}'.format(self.first, self.last)

emp_1 = Employee('Miguel', 'Lozano', 55000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.full_name())
print(emp_1.email)
print(emp_2.full_name())
print(emp_2.email)
