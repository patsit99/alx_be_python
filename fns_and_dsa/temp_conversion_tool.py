# Conversion formulas
def convert_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Ask the user for temperature type
question = input("Enter a temperature type (celsius or fahrenheit): ").strip().lower()

if question == "celsius":
    celsius_value = float(input("How many degrees Celsius? "))
    fahrenheit_value = convert_to_fahrenheit(celsius_value)
    print(f"{celsius_value}°C is {fahrenheit_value:.2f}°F")

elif question == "fahrenheit":
    fahrenheit_value = float(input("How many degrees Fahrenheit? "))
    celsius_value = convert_to_celsius(fahrenheit_value)
    print(f"{fahrenheit_value}°F is {celsius_value:.2f}°C")

else:
    print("Invalid temperature type. Please enter 'celsius' or 'fahrenheit'.")
