__author__ = 'slyfocks'
from math import sqrt
#since the concealed square is 19 digits and starts with 1, integer must be 10 digits and must start with 1
#also, since the concealed square ends in a 0, integer must also end in 0
square_gen = (str(i**2) for i in range(1000000000,1400000000,10))
for i in square_gen:
    if (i[2] == '2' and i[4] == '3' and i[6] == '4' and i[8] == '5'
        and i[10] == '6' and i[12] == '7' and i[14] == '8' and i[16] == '9'):
        print(i)
answer = sqrt(1929374254627488900)
print(answer)