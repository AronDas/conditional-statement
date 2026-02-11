height = float(input("Please enter your height here:"))

weight = float(input("Please enter your weight here:"))

BMI = weight / (height/100)**2

print("Your BMI is", BMI)

if BMI <= 18.4:
    print("You are severley underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are overweight.")
else:
    print ("You are severley obese")