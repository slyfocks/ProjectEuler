import math

factorial = math.factorial(100)
digit_total = 0
for digit in str(factorial):
    digit_total += int(digit)
print(digit_total)
