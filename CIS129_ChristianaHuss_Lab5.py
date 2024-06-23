# Module 5 Lab
# Christiana Huss
# 06/22/2024

# Program calculates the number of bottles collected each day
# accumulates daily to weekly total of bottle collection
# calculates total payout based on this figure 

# Step 1
# declare local variables
today_bottles = 0  # number of bottles returned on a day 
total_bottles = 0 # accumulated bottle values over a week
total_payout = 0 # calculated value of total_bottles*0.10
counter = 1 # for loop control variable 
keep_going = "y" # while loop control 

# Step 2 & 3
while keep_going == "y": 
    
    total_bottles = 0 # reset totalBottles to 0 at beginning of each for loop
    total_payout = 0 # resest totalPayout to 0 at beginning of each for loop 
    
    for counter in range (1, 8):
        today_bottles = int(input("Enter number of bottles for day #{}: ".format(counter))) # user to input daily bottle values
        total_bottles += today_bottles # total_bottles is sum of all today_bottles 
        total_payout = total_bottles*0.10 # total payout is .10 cents per bottle
        counter += 1 # increase counter by one each step 

    print() # print break line 
    print("The total number of bottles collected is {}".format(total_bottles)) # display total_bottles
    print("The total paid out is ${: .1f}".format(total_payout)) # display total_payout

    print() # print break line 
    print("Do you want to enter another week's worth of data?")
    keep_going = str(input("(Enter y or n): ")) # user input to stop or continue while loop

    print() # print break line 