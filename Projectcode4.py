# Random Numbers + Random Digits Generation
import secrets
import string
import datetime

# Function that take lenght is parameter
def generate_random_string(length):
    # Generate random digits and number
    alphabet = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))

first3prj = "CUS-"
today = datetime.date.today()
year = today.year
project_code = first3prj + generate_random_string(5) + "-" + str(year)
print(project_code)