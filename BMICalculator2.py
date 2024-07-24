#This Calculator helps you know your BMI status 
bmi = float(input("What is your bmi indicator?\n"))
if bmi <= 18.5:
    print(f"With a bmi of {bmi}, you are underweight")
elif bmi > 18.5 and bmi < 25:

    print(f"With a bmi of {bmi}, you are normal weight")
elif bmi >= 25 and bmi < 30:
    print(f"With a bmi of {bmi}, you are overweight")
elif bmi >=30 and bmi < 35:
    print(f"With a bmi of {bmi}, you are obese")
elif bmi >= 35:
    print(f"With a bmi of {bmi}, you are clinically obese")
     
   