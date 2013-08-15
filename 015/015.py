__author__ = 'slyfocks'


#gives number of ways to traverse an n x m grid
def lattice_paths(n, m):
    #initialize matrix
    lattice = [[0 for x in range(n)] for y in range(m)]
    lattice[0][0], lattice[0][1], lattice[1][0] = 1, 1, 1
    for x in range(1, n):
        for y in range(1, m):
            lattice[x][y] = lattice[x-1][y] + lattice[x][y-1]
    return lattice[n-1][m-1]
print(lattice_paths(20, 20))
