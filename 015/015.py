__author__ = 'slyfocks'
import numpy as np


#gives number of ways to traverse an n x m grid
#the easy mathish way would be to simply do 40 choose 20
def lattice_paths(n, m):
    #initialize matrix
    lattice = np.zeros((n+2, m+2))
    lattice[0][0], lattice[0][1], lattice[1][0] = 1, 1, 1
    for x in range(1, n+2):
        for y in range(1, m+2):
            lattice[x][y] = lattice[x-1][y] + lattice[x][y-1]
    return lattice[n+1][m]
print(lattice_paths(20, 20))
