__author__ = 'slyfocks'
from math import floor
#1,3,5,7,9,13,17,21,25,31,37,43,49,...on diagonal
#sum for the diagonals of an n x n spiral
def spiral(n):
    #floor function used to replicate pattern of increasing increases
    diag_nums = [(2*i+1+(2*i)*floor((i-1)/4)-4*(floor((i-1)/4))**2-4*(floor((i-1)/4))) for i in range(0,n)]
    return sum(diag_nums)
#1001x1001 matrix has 2001 diagonal numbers,
print(spiral(2001))
