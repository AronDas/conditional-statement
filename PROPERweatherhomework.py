weather = int(input("What is the weather today?:"))

if weather > 20:
    print("It seems to be hot today! wear light clothing.")
if weather < 0:
    print("it seems to be cold! wear heavy clothing.")
else:
    print("It seems a bit chilly, wear medium clothing.")
