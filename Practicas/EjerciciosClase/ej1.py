try:
	n1 = int(input("N1: "))
	n2 = int(input("N2: "))
	result = n1 + n2
	print(result)
except ValueError:
	print("You must enter integer numbers")