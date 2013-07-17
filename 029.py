__author__ = 'slyfocks'
from itertools import product
def answer():
    terms = list(product(range(2,101),range(2,101)))
#set removes duplicates of the results of the a,b pairs
    return len(set([a**b for (a,b) in terms]))
print(answer())
