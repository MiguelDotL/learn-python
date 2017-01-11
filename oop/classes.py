import datetime

class Employee():

    # class variables
    raise_amount = 1.04
    employee_count = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = ('{}.{}@company.com').format(self.first, self.last)

        Employee.employee_count += 1

    def full_name(self):
        # return'{} {}'.format(self.first, self.last)
        return'{first} {last}'.format(**self.__dict__)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


    @classmethod
    def set_raise_amt(cls, amt):
        cls.raise_amount = amt

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


print(Employee.employee_count)
emp_1 = Employee('Miguel', 'Lozano', 55000)
emp_2 = Employee('Test', 'User', 60000)

my_date = datetime.date(2017, 1, 11)

print(Employee.is_workday(my_date))

# # print(emp_1.__dict__)
# print(emp_1.full_name())
# print(emp_1.email)
#
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
#
#
# print(Employee.employee_count)
# # print(Employee.raise_amount)
# # print(emp_1.raise_amount)
# # emp_1.raise_amount = 2
# print(emp_1.raise_amount)
# Employee.set_raise_amt(2.0)
# print(emp_1.raise_amount)
# # print(emp_2.raise_amount)
#
#
# print(emp_2.full_name())
# print(emp_2.email)
