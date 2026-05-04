
# Borhan Vishlaghi
# 05/01/2026
# Session 15 Assignment - Employee Class and Object

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay, bonus_rate):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@email.com"
        self.pay = pay
        self.bonus_rate = bonus_rate

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def calculate_bonus(self):
        bonus_amount = self.pay * self.bonus_rate
        return bonus_amount

    def total_compensation(self):
        total_amount = self.pay + self.calculate_bonus()
        return total_amount


emp_1 = Employee("Corey", "Schafer", 50000, 0.10)
emp_2 = Employee("Test", "Employee", 60000, 0.15)

print("Employee 1:")
print("Full Name:", emp_1.fullname())
print("Email:", emp_1.email)
print("Salary:", emp_1.pay)
print("Bonus Rate:", emp_1.bonus_rate)
print("Bonus Amount:", emp_1.calculate_bonus())
print("Total Compensation:", emp_1.total_compensation())

print()

print("Employee 2:")
print("Full Name:", emp_2.fullname())
print("Email:", emp_2.email)
print("Salary:", emp_2.pay)
print("Bonus Rate:", emp_2.bonus_rate)
print("Bonus Amount:", emp_2.calculate_bonus())
print("Total Compensation:", emp_2.total_compensation())