
# Borhan Vishlaghi
# 04/23/2026
# Session 14 - Classes and Objects

# -----------------------------
# Problem 1
# -----------------------------

class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def display(self):
        print("Employee:", self.first_name, self.last_name)
        print("Salary:", self.salary)

    def compute_bonus(self, rate):
        bonus = self.salary * rate
        return bonus


# test
emp1 = Employee("John", "Smith", 50000)

emp1.display()

rate = float(input("Enter bonus rate (e.g., 0.10): "))
bonus = emp1.compute_bonus(rate)

print("Bonus:", bonus)

# -----------------------------
# Problem 2
# -----------------------------

class Student:

    def __init__(self, first_name, last_name, district_code, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code
        self.credits = credits

    def compute_tuition(self):

        if self.district_code.upper() == "I":
            tuition = self.credits * 250
        else:
            tuition = self.credits * 500

        return tuition

    def display(self):
        print("Student:", self.first_name, self.last_name)
        print("District Code:", self.district_code)
        print("Credits:", self.credits)


# test
student1 = Student("Ali", "Reza", "I", 12)

student1.display()

tuition = student1.compute_tuition()

print("Tuition Owed:", tuition)