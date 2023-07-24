"""
Take both of your names or people\'s names and check how many times 
the letters in the word TRUE occurs
And check for the number of times the letters in the word LOVE occur
Then combine these numbers to make a two digit number
If the combined number is less than 10 or greater than 90 then write the message
Your score is x,and you go together like milk and honey
For a score between 40 and 50 the message should be
Your score is y, you are alright together
otherwise, the message will just be the score
Your score is Z
"""
name = input("What are your names \n")

lower_case_name = name.lower()
first_number_ls = str(lower_case_name.count("t") + lower_case_name.count("r") + lower_case_name.count("u") + lower_case_name.count("e"))
second_number_ls = str(lower_case_name.count("l") + lower_case_name.count("o") + lower_case_name.count("v") + lower_case_name.count("e"))

score = int(first_number_ls + second_number_ls)

if score <= 10 or score >= 90:
    print(f"Your score is {score},and you go together like milk and honey")
elif score >=40 and score <= 50:
    print(f"Your score is {score}, you are alright toghether")
else:
    print(f"Your score is {score}")