__author__ = 'slyfocks'
from math import factorial
def digits(number):
    return [int(i) for i in str(number)]
#takes the sum of the factorials of each integer's digits up to an integer n
def sum_digit_factorials(n):
    return [sum([factorial(digit) for digit in digits(number)]) for number in range(n)]
#takes factorial sum array as input and returns only curious numbers
def are_curious(fact_sums):
    return [sums for index,sums in enumerate(fact_sums) if index == sums]
#the upper limit for a curious number is 9!*7 = 2540160
def solution():
    return sum(are_curious(sum_digit_factorials(2540260))[2:])
print(solution())
