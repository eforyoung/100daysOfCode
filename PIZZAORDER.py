#This is a Pizza Order Software
size = input("What is the size of the PIZZA you want to order \n")
add_pepperoni = input("Do we add Pepperoni in your PIZZA \n")
extra_cheese = input("Do we add extra Cheese in your PIZZA \n")
if size == "S":
    bill = 15
if size == "S" and add_pepperoni == "Y" and extra_cheese == "Y":
    bill += 3
    print(f"My bill is ${bill}")
elif size == "S" and add_pepperoni == "N" and extra_cheese == "Y":
    bill += 1
    print(f"My bill is ${bill}")
elif size == "S" and add_pepperoni == "Y" and extra_cheese == "N":
    bill += 2
    print(f"My bill is ${bill}")
elif size == "S" and add_pepperoni == "N" and extra_cheese == "N":
    bill += 0
    print(f"My bill is ${bill}")
if size == "M":
    bill = 20
if size == "M" and add_pepperoni == "Y" and extra_cheese == "Y":
    bill += 4
    print(f"My bill is ${bill}")
elif size == "M" and add_pepperoni == "N" and extra_cheese == "Y":
    bill += 1
    print(f"My bill is ${bill}")
elif size == "M" and add_pepperoni == "Y" and extra_cheese == "N":
    bill += 3
    print(f"My bill is ${bill}")
elif size == "M" and add_pepperoni == "N" and extra_cheese == "N":
    bill += 0
    print(f"My bill is ${bill}")
if size == "L":
    bill = 25
if size == "L" and add_pepperoni == "Y" and extra_cheese == "Y":
    bill += 4
    print(f"My bill is ${bill}")
elif size == "L" and add_pepperoni == "N" and extra_cheese == "Y":
    bill += 1
    print(f"My bill is ${bill}")
elif size == "L" and add_pepperoni == "Y" and extra_cheese == "N":
    bill += 3
    print(f"My bill is ${bill}")
elif size == "L" and add_pepperoni == "N" and extra_cheese == "N":
    bill += 0
    print(f"My bill is ${bill}")



    