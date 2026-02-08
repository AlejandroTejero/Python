import sys

for i in range(1, len(sys.argv)):
    try:
        print(int(sys.argv[i]))
    except ValueError:
        print("NaN")