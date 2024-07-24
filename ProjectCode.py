import random
import datetime

first3prj = "PRJ-"
Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
random_alphabet_number = random.randint(0,25)
choose_alphabet = Alphabet[random_alphabet_number]
numbers_choose = random.randint(0,9)
today = datetime.date.today()
year = today.year
middig5 = choose_alphabet + choose_alphabet + str(numbers_choose) + choose_alphabet + str(numbers_choose) + "-"
project_code = first3prj + middig5 + str(year)
print(project_code)
