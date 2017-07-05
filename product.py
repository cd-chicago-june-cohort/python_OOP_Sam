class product(object):
    def __init__(self, name, price, brand, cost):
        self.name = name
        self.price = price
        self.brand = brand
        self.cost = cost
        self.status = "For Sale"
    def sell(self):
        self.status = "Sold"
        return self
    def add_tax(self, tax):
        self.price += (self.price * tax ) 
        return self
    def return_item(self, reason):
        if reason == "Defective":
            self.price = 0
            self.status = "Defective"
        if reason == "Returned in the box":
            self.status = "Like new"
        if reason == "Opened and returned":
            self.status = "Used"
            self.price *= .8
        return self
    def display_info(self):
        print "    {}\nPrice: ${} Cost: ${}\n    Brand: {}\n    Product Status: {}".format(self.name, self.price, self.cost, self.brand, self.status)


shirt = product("Purple Sweater", 685, "GUCCI", 410)
shirt.display_info()
