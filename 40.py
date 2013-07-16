__author__ = 'slyfocks'
def make_number(num_xs):
    number = []
    i = 1
    while i <= num_xs:
        number.append(str(i))
        i+=1
    return ''.join(number)
def get_answer():
    answer = 1 # initialization
    for i in range(7):
        answer *= int(make_number(1000000)[10**i-1])
    return answer
print(get_answer())
