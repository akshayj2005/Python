#to create custom module user defined


def add(x,y):
    return x+y
def subtract(x,y):
    return x-y

#write python code to define class create its objects and access the properties in methods of the objects
class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print(self.make)
        print(self.year)
        print(self.model)

my_car = car("toyota", "carolla", 2005)
my_car.display_info()


