__author__ = 'slyfocks'
def digits(number):
    return [int(i) for i in str(number)]
#takes the sum of the fifth power of each integer's digits up to an integer n
def sum_digit_factorials(n):
    return [sum([digit**5 for digit in digits(number)]) for number in range(n)]
#only returns numbers that equal the sum of the fifth powers of their digits
def are_digit_fifth_powers(power_sums):
    return [sums for index,sums in enumerate(power_sums) if index == sums]
#9^5*6 = 354294 is the upper bound for possible fifth power sum digits
def solution():
    return sum(are_digit_fifth_powers(sum_digit_factorials(354294))[2:]) #0 and 1 be gone!
print(solution())