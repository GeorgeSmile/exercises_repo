## created a class named vehicle using the class keyword with no attributes or methods.
## contains attributes for max_speed and colour
## contains methods to change the speed and colour attributes
# class vehicle:
#     def __init__(self, name, speed, colour):
#         self.name = name
#         self.speed = speed
#         self.colour = colour
    
#     def get_name(self):
#         return self.name
    
#     def get_speed(self):
#         return self.speed

#     def get_colour(self):
#         return self.colour

#     def set_speed(self, speed):
#         self.speed = speed
    
#     def set_colour(self, colour):
#         self.colour = colour

# v = vehicle("Mustang", 120, "Black")
# v.set_speed(80)
# v.set_colour("Red")
# print(v.get_name())
# print(v.get_speed())
# print(v.get_colour())


## Creates a sublass 'bus' and inherits all the variables from the vehicles class 
# class vehicle:
#     def __init__(self, name, speed, colour):
#         self.name = name
#         self.speed = speed
#         self.colour = colour

#     def show(self):
#         print(f"This vehicle is a {self.name}, with speed {self.speed} and is the colour {self.colour}")

# class bus(vehicle):
#     def speak(self):
#         print("London Bus")

# b = bus("Bus", 60, "Red")
# b.speak()
# b.show()

## super class is vehicle which can haev subclasses added. e.g. bus is added and adds a colour attribute to be shown
class vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        

    def show(self):
        print(f"This vehicle is a {self.name}, with speed {self.speed} and is the colour {self.colour}")

class bus(vehicle):
    def __init__(self, name, speed, colour):
        super().__init__(name, speed) # refers to the super class, the one it is inheriting from
        self.colour = colour
    def show(self):
        print(f"This vehicle is a {self.name}, with speed {self.speed} and is the colour {self.colour}")

b = bus("bus", 60, "Red")
b.show()