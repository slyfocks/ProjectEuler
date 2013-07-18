__author__ = 'slyfocks'
import math
#take advantage of symmetry of combinatorial function
def n_r_matrix(n):
    return [(i,j) for i in range(23,n+1) for j in range(2,math.floor(i/2)+1)]
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
def combination_list(list):
    return [nCr(n,r) for (n,r) in list if nCr(n,r)>1000000]
#subtract 39 because (24,12),(26,13),(28,14)...get counted twice when they only be counted once
print(2*(len(combination_list(n_r_matrix(100))))-39)