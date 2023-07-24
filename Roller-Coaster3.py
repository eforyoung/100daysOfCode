height =int(input("What is your height? \n"))


ticket_cost = 0

if height > 120:
    age = int(input("What is your age? \n"))
    if age < 12:
        ticket_cost = 5
    elif age >= 12 and age <=18:
        ticket_cost = 7
    elif age > 18 and age < 45:
        ticket_cost = 12
    elif age >= 45 and age <= 55:
        ticket_cost = 0
    elif age > 55:
        ticket_cost = 12
    want_photos = input("Do you want photos? \n")
    if want_photos == "Y":
        ticket_cost += 3
    else:
        ticket_cost += 0

    print(f"The total bill is ${ticket_cost}")
else:
    print("You need to grow some more inches")
