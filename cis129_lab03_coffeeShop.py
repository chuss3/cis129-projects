#Program to print the receipt of someone's coffee shop order
#Prompt the user to enter how many coffess they bought
#Prompt the user to enter how many muffins they bought 
#Python to calculate cost of coffees and muffins
#Program to print subtotal of coffees and muffins
#Python to calculate tax and subtotal of order
#Program to print total cost based on above 

print("***************************************\n")
print("My Coffee and Muffin Shop")

#prompt user to input coffees, collected as integer
coffee=int(input("Number of coffees bought?\n")) 

#prompt user to input muffins, collected as integer
muffins=int(input("Number of muffins bought?\n")) 

print("***************************************\n\n")
print("***************************************\n")
print("My Coffee and Muffin Shop Receipt")

#calculate cost of coffee as float 
coffee_cost=float(5*coffee) 

#calculate cost of muffins as float 
muffin_cost=float(4*muffins)  

#print coffee subtotal to 2 decimal places
print(coffee, "Coffee at $5 each: $", "{0:.2f}".format(coffee_cost)) 

#print muffin subtotal to 2 decimal places
print(muffins, "Muffins at $4 each: $", "{0:.2f}".format(muffin_cost))

#calculate subtotal of muffins and coffee as float 
subtotal=float(coffee_cost+muffin_cost) 

#formula for 6% tax
tax=0.06*subtotal 

#print the tax to 2 decimal places
print("6% tax: $", "{0:.2f}".format(tax))

print("---------")

#calculate total cost of muffins, coffee, and tax
total=coffee_cost+muffin_cost+tax

#print the total cost to 2 decimal places
print("Total: $", "{0:.2f}".format(total)) 
print("***************************************")
