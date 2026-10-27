def celisus_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius_temp = int(input("Enter temperature in Celsius: "))
# celsius_temp = 25
fahrenheit_temp = celisus_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")
