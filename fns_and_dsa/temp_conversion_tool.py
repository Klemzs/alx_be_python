FAHRENHEIT_TO_CELCIUS_FACTOR = 5/9
CELCIUS_TO_FAHRRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * FAHRENHEIT_TO_CELCIUS_FACTOR
    return celcius

def convert_to_fahrenheit(celcius):
    fahrenheit = (celcius * CELCIUS_TO_FAHRRENHEIT_FACTOR) + 32
    return fahrenheit

temp = input("Enter the temperature to convert: ")

try:
    temp = float(temp)
    unit = input("Is this temperature in Celcius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        print(f"{temp}°F is {convert_to_celcius(temp)}°C")
    elif unit == "C":
        print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
    else:
        print("Invalid temperature unit, 'C or 'F'")
    

except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
