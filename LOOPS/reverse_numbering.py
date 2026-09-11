reverse = 0 
a = int(input("Enter a number: "))
while a > 0:
    digit = a % 10
    reverse = (reverse * 10) + digit
    a = a // 10
print("The reverse of the number is:", reverse)