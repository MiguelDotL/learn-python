# my_list = [9,1,8,2,7,3,6,4,7,5]
#
# my_list.sort() # returns None
#
# sorted(my_list)
# sorted(my_list, reverse=True)
#
#
# my_tup = (9,1,8,2,7,3,6,4,7,5)
#


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, ${:,})'.format(self.name, self.age, self.salary)


emp_1 = Employee('Sagan', 37, 1000000000)
emp_2 = Employee('Jones', 28, 3000000)
emp_3 = Employee('Wu', 28, 8000000)


employees = [emp_1, emp_2, emp_3]


# sorting functions
def sort_emp_name(emp):
    return emp.name
def sort_emp_age(emp):
    return emp.age
def sort_emp_sal(emp):
    return emp.salary


s_employees = sorted(employees, key=sort_emp_name, reverse=False)

print(s_employees)
