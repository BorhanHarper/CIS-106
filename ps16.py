
# Borhan Vishlaghi
# 05/03/2026
# Session 16 Assignment

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def long_term_bonus(self):
        return 0


# Manager Class (inherits Employee)
class Manager(Employee):
    def long_term_bonus(self):
        return self.salary * 0.40


# Executive Class (inherits Manager)
class Executive(Manager):

    def executive_bonus(self):
        return self.salary * 2.0   # 200%

    def long_term_bonus(self):
        return self.salary * 0.50   # override


# Test objects
m1 = Manager("Mahsa", 50000)
e1 = Executive("Shirin", 80000)

print("Manager Bonus:", m1.long_term_bonus())
print("Executive Bonus:", e1.executive_bonus())
print("Executive Long Term Bonus:", e1.long_term_bonus())

class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price

    def discount_price(self):
        return self.sticker_price * 0.90


# Sport Class
class Sport(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.options_total = 0

    def sport_wheels(self, option):
        if option == "Y":
            self.options_total += 1000

    def sport_engine(self, option):
        if option == "Y":
            self.options_total += 3000

    def sport_interior(self, option):
        if option == "Y":
            self.options_total += 2000

    def price_with_options(self):
        return self.discount_price() + self.options_total


# Luxury Class
class Luxury(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.options_total = 0

    def gps(self, option):
        if option == "Y":
            self.options_total += 5000

    def self_driving(self, option):
        if option == "Y":
            self.options_total += 10000

    def price_with_options(self):
        return self.discount_price() + self.options_total


# Test Sport
car1 = Sport("BMW", "M3", 60000)
car1.sport_wheels("Y")
car1.sport_engine("Y")
car1.sport_interior("N")

print("Sport Car Price:", car1.price_with_options())


# Test Luxury
car2 = Luxury("Tesla", "Model S", 80000)
car2.gps("Y")
car2.self_driving("Y")

print("Luxury Car Price:", car2.price_with_options())