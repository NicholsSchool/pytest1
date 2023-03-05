import sys

# check if two arguments are provided in command line
if len(sys.argv) != 3:
    print("Please provide two numbers as arguments.")
    exit()

# get the two numbers from command line arguments
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

# calculate the sum of the two numbers
sum = num1 + num2

# print the result to console
print("The sum of", num1, "and", num2, "is", sum)