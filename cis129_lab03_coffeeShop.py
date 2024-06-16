#Program to print the receipt of someone's coffee shop order
#Prompt the user to enter how many coffess they bought
#Prompt the user to enter how many matchas they bought 
#Prompt the user to enter how many muffins they bought 
#Prompt the user to enter how many bagels they bought 
#Python to calculate cost of coffees, matchas, muffins, and bagels
#Program to print subtotal of ordered items
#Python to calculate tax and subtotal of order
#Program to print total cost based on above 

print("***************************************\n")
print("My Coffee and Muffin Shop")

#prompt user to input coffees, collected as integer
coffee=int(input("Number of coffees bought?\n")) 

#prompt user to input matchas, collected as integer
matchas=int(input("Number of matchas bought?\n")) 

#prompt user to input muffins, collected as integer
muffins=int(input("Number of muffins bought?\n")) 

#prompt user to input bagels, collected as integer
bagels=int(input("Number of bagels bought?\n")) 

print("***************************************\n\n")
print("***************************************\n")
print("My Coffee Shop Receipt")

#calculate cost of coffee as float 
coffee_cost=float(5*coffee) 

#calculate cost of matchas as float 
matcha_cost=float(5*matchas)  

#calculate cost of muffins as float 
muffin_cost=float(4*muffins)  

#calculate cost of bagels as float 
bagel_cost=float(3*bagels)  

#print coffee subtotal to 2 decimal places
print(coffee, "Coffee at $5 each: $", "{0:.2f}".format(coffee_cost)) 

#print matcha subtotal to 2 decimal places
print(matchas, "Matchas at $5 each: $", "{0:.2f}".format(matcha_cost))

#print muffin subtotal to 2 decimal places
print(muffins, "Muffins at $4 each: $", "{0:.2f}".format(muffin_cost))

#print bagel subtotal to 2 decimal places
print(bagels, "Bagels at $3 each: $", "{0:.2f}".format(bagel_cost))

#calculate subtotal of items as float 
subtotal=float(coffee_cost+matcha_cost+muffin_cost+bagel_cost) 

#formula for 6% tax
tax=0.06*subtotal 

#print the tax to 2 decimal places
print("6% tax: $", "{0:.2f}".format(tax))

print("---------")

#calculate total cost of muffins, coffee, and tax
total=subtotal+tax

#print the total cost to 2 decimal places
print("Total: $", "{0:.2f}\n".format(total)) 
print("Thank you! Please come back soon!") 
print("***************************************")
