#This program gives an alternative solution to the PIZZA ORDER problem
size = input("What is the size of the PIZZA you are ordering \n")
add_pepperoni = input("Do you need PEPPERONI added? \n")
extra_cheese = input("Do you need extra_cheese added? \n")

bill = 0
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if add_pepperoni == "N":
    bill += 0

if extra_cheese == "Y":
    bill += 1

print(f"The bill is ${bill}")