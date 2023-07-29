#Do same solution paying bills and selecting banker without using the choice function
import random

banker_names = input("Give me the names of the bankers having dinner \n")

names_list = banker_names.split(",")

len_names_list = len(names_list)

random_number = random.randint(0,len_names_list-1)

person = names_list[random_number]

print(person)