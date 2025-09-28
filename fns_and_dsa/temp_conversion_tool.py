FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

temp = input("Enter the temperature to convert: ")

try:
    temp = float(temp)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        print(f"{temp}°F is {convert_to_celsius(temp)}°C")
    elif unit == "C":
        print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
    else:
        print("Invalid temperature unit, 'C or 'F'")
    

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
