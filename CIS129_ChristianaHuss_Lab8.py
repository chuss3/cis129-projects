# Christiana Huss
# CIS 129
# Module 8 Lab
# 06/29/2024

# Program to check whether a phrase is a palindrome or not

# Message to user to prompt string input 
# Define is_palindrome to test input 
    # convert input to lowercase letters
    # create empty stack
    # append stack with elements of input
    # pop elements of input 
    # test popped elements against appended elements to see if they're equal, return T/F
# Output message to user based on boolean logic above 

# Message to user 
print("We are going to check if the phrase you enter is a palindrome or not.")

# User to input their phrase 
phrase = str(input("Please enter the phrase you'd like to check: "))

# Define function to test if phrase is a palindrome 
def is_palindrome(x):
    x = [element.lower() for element in x] # convert elements of phrase to lowercase 
    stack = [] # create empty stack to store elements of phrase 
    
    for char in x: 
        stack.append(char) # append elements of phrase to stack 

    # Test print stack was assigned correclty, with lowercase:
    # print(f"{stack}")
             
    for char in x:
        if char != stack.pop(): # pop elements of stack, test if they are equal to char in phrase
            return False # if not equal, return false 

    return True # else return true 

if is_palindrome(phrase) == False:
    print(f"{phrase} is not a palindrome.") # message to user if is_palindrome is false 
else:
    print(f"{phrase} is a palindrome.") # message to user if is_palindrome is true 
