# difference between classmethod and staticmethod
# thanks to Corey Schafer for tutorials

class Employee:

    nums_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'  # This violates S.O.L.I.D single responsibility principle
        Employee.nums_of_emps += 1

    def fullname(self):
        return('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod  # Does the same as "The chunk of code" bellow
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod  # Does the same as "The chunk of code" bellow
    def from_string_static(emp_str):
        first, last, pay = emp_str.split('-')
        return (first, last, pay)

    # static method
    @staticmethod
    def is_workday(day):
        if day.weekday() in [5, 6]: return False
        return True

emp_1 = Employee('Corey', 'Schafer', 50000)
print(emp_1.fullname())
emp_2 = Employee('Test', 'Tester', 60000)
print(emp_2.fullname())

# Employee.set_raise_amt(1.05) # Its the same as -> Employee.raise_amt = 1.05
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_1.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# Chunk of code =========================
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steave-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)
print(new_emp_1.pay)

new_emp_2 = Employee.from_string(emp_str_1)
print('classmethod used:', new_emp_1.email)
print(new_emp_1.pay)
# =======================================

#static method
import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))

new_emp_2 = Employee.from_string_static(emp_str_1)
print('staticmetod used:',new_emp_1.email)
print(new_emp_1.pay)