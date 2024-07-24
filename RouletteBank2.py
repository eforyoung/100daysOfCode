#Do same solution paying bills and selecting banker without using the choice function
import random

us_states_order_union = ["Delaware","Pennsylvania","New Jersey","Georgia","Connecticut","Massachusetts","Maryland","South Carolina","New Hampshire","Virginia","New York","North Carolina","Rhode Island","Vermont","Kentucky","Tennessee","Ohio","Louisiana","Indiana","Mississippi","Illinois","Alabama","Maine","Missouri","Arkansas","Michigan","Florida","Texas","Iowa","Wisconsin","California","Minnesota","Oregon","Kansas","West Virginia","Nevada","Nebraska","Colorado","North Dakota","South Dakota","Montana","Washington","Idaho","Wyoming","Utah","Oklahoma","New Mexico","Arizona","Alaska","Hawaii"]

banker_names = input("Give me the names of the bankers having dinner \n")

names_list = banker_names.split(",")

len_names_list = len(names_list)

random_number = random.randint(0,len_names_list-1)

person = names_list[random_number]

print(person)