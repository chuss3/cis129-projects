# Christiana Huss
# CIS 129
# Module 7 Lab
# 06/29/2024

# Program to calculate revenue from a theater with multiple sections 

# Define constants for sections A, B, & C's names, prices, and number of seats 
# sections_data as an array of tuples to store constants for each section 
# total_revenue to store total revenue garnered in all sections 
# define get_valid_number function to validate inputs with while loop
# for loops to 
    # display available seats and prices in each section
    # get input from user for tickets sold in each section; append section to add revenue and tickets sold to sections_data 
    # display tickets sold and revenue in each section 
# print total revenue 

# Declare section name constants 
SECTION_A_NAME = 'A'
SECTION_B_NAME = 'B'
SECTION_C_NAME = 'C'

# Declare cost of tickets in each section
SECTION_A_PRICE = 20
SECTION_B_PRICE = 15
SECTION_C_PRICE = 10

# Declare number of available seats in each section
SECTION_A_SEATS = 300
SECTION_B_SEATS = 500
SECTION_C_SEATS = 200

# list of tuples for each section 
sections_data = (
    ['A', SECTION_A_PRICE, SECTION_A_SEATS], 
    ['B', SECTION_B_PRICE, SECTION_B_SEATS],
    ['C', SECTION_C_PRICE, SECTION_C_SEATS])
    # add section D here if necessary 

# initialize variable for total revenue 
total_revenue = 0 

# define function to validate inputs 
def get_valid_number(msg, min_value, max_value): 
    new_value = int(input(msg)) # get integer input so new_value can compare to min_value and max_value 

    while new_value < min_value or new_value > max_value: # validate input by checking for invalid entries 
        print("Invalid entry. Please try again.")  
        new_value = int(input(msg)) # user to re-enter

    return new_value # return new_value once valid input is received 

# print welcome message to user
print("Welcome to the theater!")  

# for loop to display seats and prices per section 
for section in sections_data: 
    print(f"Tickets cost ${section[1]} in Section {section[0]}. There are {section[2]} seats in this Section.")

# iterate through sections in sections_data; can easily add a section D, E, F, etc. to "sections_data" declared above 
for section in sections_data:
    message = "Enter the number of tickets sold in section " + section[0] 
    tickets_sold = get_valid_number(message, 0, section[2]) # call get_valid_number function 
    section.append(tickets_sold) # append number of tickets sold in each section to each tuple in sections_data 
    section.append(tickets_sold*section[1]) # append revenue for each section to each tuple in sections_data 
    total_revenue += tickets_sold * section[1] # cumulate running total revenue 
    print(f"Subtotal: ${total_revenue}.") # print sub-total after each user input 

# for loop to display total tickets sold and revenue per section 
for section in sections_data:
    print(f"You sold {section[3]} seats in Section {section[0]}. Your revenue for Section {section[0]} is ${section[4]}.")

# output total gross revenue
print(f"Your total revenue is ${total_revenue}.")
    
