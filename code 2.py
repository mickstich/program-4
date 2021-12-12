class Vehicle():
    def __init__(self,wheels, colour):
        self.wheels=wheels
        self.colour = colour
    def get_wheels(self):
        return self.wheels
    def set_wheels(self,value):
        self.wheels=value
    def get_colour(self):
        return self.colour
    def set_colour(self,value):
        self.colour=value
    def details(self):
        print(" 1. wheels {0} colour {1} ".format(self.wheels,self.colour))

class bus(Vehicle):
    def __init__(self, colour, wheels):
        super().__init__(wheels,colour)

    def details(self):
        print(" 2. speed {0} colour {1}".format ( self.wheels,self.colour))

obj2= bus('Black',100)

obj2.details()
obj2.set_wheels(6)
print(obj2.get_wheels())

