import random
import datetime
first3prj = "PRJ-"
xter = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
random_alphabet_number = random.randint(0,35)
choose_alphabet = xter[random_alphabet_number]
today = datetime.date.today()
year = today.year
random_xter = ""
for i in range(5):
    choose_alphabet1 = random.choice(choose_alphabet)
    random_xter += choose_alphabet1

print(random_xter)