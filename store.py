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
        return self

class store(object):
    def __init__(self, name, owner, location, products):
        self.name = name
        self.owner = owner
        self.location = location
        self.products = products
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    def remove_product(self, product_name):
        self.products.append(product_name)
        return self
    def inventory(self):
        for product in self.products:
            print "    Product: {}, {}\n    Price: ${}\n    Status: {}\n-----------------".format(product.brand, product.name, product.price, product.status)
        return self


shirt = product("Purple Sweater", 685, "GUCCI", 410)
pants = product("Light-wash jeans", 145, "7 Jeans", 130)
purse = product("Nude Cross-body", 1470, "Prada", 1350)

saks = store("Sak's Fifth Avenue", "Sam Zoeller", "555 5th Avenue, New York, New York", [shirt, pants, purse])
saks.inventory()