__author__ = 'slyfocks'
from math import sqrt
def primes(n):
    sieve = [True]*(n+1)
    sieve[0],sieve[1] = False,False
    for i in range(2, int(sqrt(n))+1):
        if sieve[i]:
            m = int(n/i) - i
            sieve[i*i: n+1:i] = [False]*(m+1)
    return [i for i in range(n) if sieve[i]]
def combination_list(n):
    #sum has to be less than 1000000 and prime so it must be in primes(1000000)
    for j in range(len(primes(n)),1,-1):
        comb_list = [sum(primes(n)[i:j+i]) for i in range(len(primes(n))-j)
                     if sum(primes(n)[i:j+i]) in primes(1000000)]
        #only print if list is not empty, then break since we only care about the max
        if comb_list:
            print(comb_list)
            break
#since sum(primes(4000)) is slightly greater than 1 million, we can't have a list longer than 4000
print(combination_list(4000))