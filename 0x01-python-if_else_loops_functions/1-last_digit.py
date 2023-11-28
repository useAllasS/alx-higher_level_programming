#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
# Calculate the last digit of the number
last_digit = number % 10

# Generate the output string
output = "Last digit of {} is {}".format(n, last_digit)

# Check the conditions and append the appropriate string
if last_digit > 5:
    output += " and is greater than 5"
elif last_digit == 0:
    output += " and is 0"
else:
    output += " and is less than 6 and not 0"

# Print the output string
print(output)
