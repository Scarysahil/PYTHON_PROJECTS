number = int(input("enter a number: "))

reverse = 0 

while number >0 :
    last_digit = number % 10
    reverse = reverse * 10 + last_digit
    number = number // 10 

print("The reverse of the number is", reverse)



