__author__ = 'slyfocks'
def digits(number):
    return [int(i) for i in str(number)]
def ispermutation(num1,num2):
    return (set(digits(num1)) & set(digits(num2))) == set(digits(num1)) and set(digits(num2))
#Max is 166666 because if x>166666 then 6*x > 1000000 which we cannot have
for i in range(100000,166667):
    if ispermutation(i,2*i) and ispermutation(i,3*i) and ispermutation(i,4*i) \
        and ispermutation(i,5*i) and ispermutation(i,6*i):
        print(i)
