#Task is to upgrade BMI Calculator. This is V2.0

#Greetings
print("Welcome to BMI Calculator")
#Inputs
height = float(input("enter your height in m: \n"))
weight = float(input("enter your weight in kg: \n"))
#Calculations
BMI_index = float(weight) / float(height ** 2)
BMI_index_float = round(BMI_index, 2)

if BMI_index_float <= 18.5:
    print(f"Your  BMI is {BMI_index_float}, you are underweight.")
elif BMI_index_float <= 25:
    print(f"Your  BMI is {BMI_index_float}, you are normal weight.")
elif BMI_index_float <= 30:
    print(f"Your  BMI is {BMI_index_float}, you are you are slightly overweight.")
elif BMI_index_float <=35:
    print(f"Your  BMI is {BMI_index_float}, you are obese.")
else:
    print(f"Your  BMI is {BMI_index_float}, you are clinically obese.")