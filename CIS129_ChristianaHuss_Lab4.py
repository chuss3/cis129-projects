# Module 4 Lab-4
# Christiana Huss
# 06/16/2024

# Program calculates the amount of store and employee bonuses
# based on monthly sales using if-elif-else statements 

# Step 1
# declare local variables
monthlySales = 0  # monthly sales amount
storeAmount = 0  # store bonus amount
empAmount = 0  # employee bonus amount
salesIncrease = 0  # percent of sales increase
prompt1 = "Please enter your monthly sales in dollars: " 
prompt2 = "Please enter the percent of sales increase in decimal format: " 

# Step 2
# This code gets the monthly sales
monthlySales = float(input(prompt1))

# Step 3
# This code determines the storeAmount bonus
if monthlySales >= 110000:
	storeAmount = 6000
elif monthlySales >= 100000:
        storeAmount = 5000
elif monthlySales >= 90000:
        storeAmount = 4000
elif monthlySales >= 80000:
        storeAmount = 3000
else: 
        storeAmount = 0  

# Step 4
# This code gets the percent of increase in sales
salesIncrease = float(input(prompt2))
salesIncrease = salesIncrease / 100

# Step 5 
#This code determines the empAmount bonus
if salesIncrease >= .05:
	empAmount = 75
elif salesIncrease >= .04:
	empAmount = 50
elif salesIncrease >= .03:
	empAmount = 40
else:
	empAmount = 0

# Step 6
# This code prints the bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)

if (storeAmount == 6000 ) and (empAmount == 75):
	print('Congrats! You have reached the highest bonus amounts possible!')
