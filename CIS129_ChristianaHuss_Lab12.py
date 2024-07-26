# Christiana Huss
# CIS 129
# Module 12 Lab
# 07/25/2024

# Create a class to input and output pet information 
# Define a new class "pet" that holds name, type, and age input by user
# "pet" will also have 3 methods to display name, type, and age
# create new object "animal" of class "pet"
# call "pet" methods to print name, type, and age of "animal" 

# new class to store pet information 
class pet:
    # constructor to initilaize objects of class pet input by user
    def __init__(self):
        self.set_name = input("Please enter your pet's name: ")
        self.set_type = input("Please enter what type of pet it is: ")
        self.set_age = int(input("Please enter your pet's age (in years): "))

    # method to display pet's name
    def get_name(self):
        print("Your pet's name is:", self.set_name)

    # method to display pet's type
    def get_type(self):
        print("Your pet is a:", self.set_type)

    # method to display pet's age
    def get_age(self):
        print("Your pet's age is:", self.set_age)

# create new object of type pet
animal = pet()

# display animal object attributes using class methods defined above
animal.get_name()
animal.get_type()
animal.get_age()