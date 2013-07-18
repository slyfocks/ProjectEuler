__author__ = 'slyfocks'
from itertools import permutations
def digits(number):
    return [int(i) for i in str(number)]
pair_digit_sums = []
for pair in permutations(range(100),2):
    pair_digit_sums.append(sum(digits(pair[0]**pair[1])))
print(max(pair_digit_sums))
