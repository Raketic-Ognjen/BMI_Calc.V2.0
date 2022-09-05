#Task is to upgrade BMI Calculator. This is V2.0

#Greetings
print("Welcome to BMI Calculator")
#Inputs
height = float(input("enter your height in m: \n"))
weight = float(input("enter your weight in kg: \n"))
#Calculations
i = round(weight / height ** 2)
BMI_index = i


if BMI_index < 18.5:
    print(f"Your  BMI is {BMI_index}, you are underweight.")
elif BMI_index < 25:
    print(f"Your  BMI is {BMI_index}, you are normal weight.")
elif BMI_index < 30:
    print(f"Your  BMI is {BMI_index}, you are you are slightly overweight.")
elif BMI_index < 35:
    print(f"Your  BMI is {BMI_index}, you are obese.")
else:
    print(f"Your  BMI is {BMI_index}, you are clinically obese")
