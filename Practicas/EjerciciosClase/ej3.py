try:
    fahrenheit = float(input("Fahrenheit Grades: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"Celsius Grades: {celsius}")
except ValueError:
    print("Radius must be a float number")