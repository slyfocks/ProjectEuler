__author__ = 'slyfocks'
import itertools
with open('names22.txt') as file:
    names = file.readlines()[0].strip('"').split('","')
names.sort()
letter_points = [[ord(char) - 64 for char in name] for name in names]
name_totals = [sum(points) for points in letter_points]
final_points = [points*(index+1) for index, points in enumerate(name_totals)]
total = sum(final_points)
print(total)
