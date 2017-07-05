class bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        if self.miles != 0:
            self.miles -= 5
        return self
    def displayInfo(self):
        print "Price: {}, Max Speed: {}, Total Miles: {}".format(self.price, self.max_speed, self.miles)
        return self

bike1 = bike("$80", "25 mph")
bike2 = bike("$150", "70 mph")
bike3 = bike("$17", "34 mph")

print "-" * 50
bike1.ride().ride().ride().reverse().displayInfo()
print "-" * 50
bike2.ride().ride().reverse().reverse().displayInfo()
print "-" * 50
bike3.reverse().reverse().reverse().displayInfo()
print "-" * 50


