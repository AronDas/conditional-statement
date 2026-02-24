medical_value = input("did you have a medical cause? Y/N")

if medical_value == "Y":
    print("You are allowed.")
else:
    attendance = int(input("Please enter your attendance score"))
    if attendance >= 75:
        print("You are allowed in the test")
    else:
        print("You are not allowed in the test.")