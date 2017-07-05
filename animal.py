class animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "{} Health: {}".format(self.name, self.health)
        return self
class dog(animal):
    def __init__(self):
        super(dog, self).__init__("Dog", 150)
    def pet(self):
        self.health += 5
        return self
class dragon(animal):
    def __init__(self):
        super(dragon, self).__init__("Dragon", 170)
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(dragon, self).display_health()
        print "I am a dragon"
    

emerald = dragon() 
spot = dog()
tiger = animal("Tiger", 100)

emerald.display_health()
spot.display_health()
tiger.display_health()

emerald.fly().fly().display_health()
spot.walk().walk().walk().run().run().pet().pet().pet().pet().display_health()
tiger.run().run().display_health()