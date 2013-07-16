__author__ = 'slyfocks'
#i^i for 1,2,...,999,1000
powers = [i**i for i in range(1,1001)]
#Sum and convert to string so last ten digits can be sliced
last_ten_digits = str(sum(powers))[-10:]
print(last_ten_digits)