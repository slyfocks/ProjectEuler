__author__ = 'slyfocks'
def triangle(i):
    return i*(i+1)/2
def pentagon(i):
    return i*(3*i-1)/2
def hexagon(i):
    return i*(2*i-1)
#initialize past the first large number in all three categories
t,p,h = 286,166,144
#increase by 1 the index of whichever is the least until equality
while not triangle(t) == pentagon(p) == hexagon(h):
    if triangle(t) < pentagon(p):
        if triangle(t) < hexagon(h):
            t += 1
        else:
            h += 1
    elif pentagon(p) < hexagon(h):
        p += 1
    else:
        h +=1
print(triangle(t))