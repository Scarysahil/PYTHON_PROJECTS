largerst = 0 

for i in range (5):
    number = int(input("Enter a number: "))

    if number > largerst:
        largerst = number

print("The largest number is:", largerst)
