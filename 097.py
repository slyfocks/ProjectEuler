__author__ = 'slyfocks'
#Found that the last seven digits of 2^x repeat themselves every 62500 iterations
#([(index,str(2**i)[-6:]) for index,i in enumerate(range(20000)) if str(2**i)[-5:] == '440128'])
remainder = 7830457 % 62500
answer = str(2**remainder*28433 + 1)[-10:]
print(answer)
