__author__ = 'slyfocks'
with open('largesum13.txt') as file:
    numbers = file.readlines()
list = [int(number.strip()) for number in numbers]
answer = str(sum(list))[:10]
print(answer)