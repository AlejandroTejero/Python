pi = 3.1415

try:
	radius = float(input("Radius: "))
	if radius > 0:
		perimiter = 2 * pi * radius
		area = pi * (radius ** 2)
		print(f"Perimeter: {perimiter:.2f}")
		print(f"Area: {area:.2f}")
	else:
		print("Radius must be a positive float number")
except ValueError:
	print("Radius must be a float number")