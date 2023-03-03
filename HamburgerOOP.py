# Description:
# Authors: Mac Hartsell, Tobin Whitworth

# Mac Code


# Tobinfdsdsdfsd Code
Queue = []
Dictionary = []

# Teilani Code
import random
​
# Create an Order class
# Create a constructor that defines an instance variable called burger_count
# Create a method called randomBurgers that returns a number between 1 and 20
# The constructor should call the randomBurgers() method and assign the return value to the burger_count instance variable
​
​
class Order:
    def __init__ (self):
        self.burger_count = self.randomBurgers()  
​
    def randomBurgers(self):
       return random.randint(1,20)
    
# Create a Person class
# Create a constructor that defines an instance variable called customer_name
# Create a method called randomName() that contains a list of 9 names:
#         asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
​
# This method randomly returns one of the 9 names when called
# The Person constructor should call the randomName() method and assign the return value (a random name) to the customer_name instance variable
    
class Person:
    def __init__(self):
        self.customer_name = self.randomName()
​
    def randomName(self):
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(asCustomers)

# Kimball Code
