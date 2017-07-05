class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel 
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()
    def display_all(self):
        print "    Price: ${}\n    Speed: {} mph\n    Fuel: {}\n    Mileage: {} mpg\n    Tax: {}".format(self.price, self.speed, self.fuel, self.mileage, self.tax)

print "-" * 50
car1 = car(2400, 90, "Full", 18)
print "-" * 50
car2 = car(250000, 240, "Full", 13)
print "-" * 50
car3 = car(5600, 110, "Empty", 24)
print "-" * 50
car4 = car(900, 70, "Empty", 22)
print "-" * 50
car5 = car(18000, 125, "Full", 36)
print "-" * 50
car6 = car(84000, 175, "Full", 27)
print "-" * 50