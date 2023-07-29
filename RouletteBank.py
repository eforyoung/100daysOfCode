#Choose the banker to pay the bill 
import random
names_string = input("Give me the name of the bankers \n")
names = names_string.split(",")
chosen_name = random.choice(names)
print(chosen_name)