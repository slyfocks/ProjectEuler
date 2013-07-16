__author__ = 'slyfocks'
def palindromes(n):
    bin_palindromes = [number for number in range(n)
                        if str(bin(number)).lstrip('0b') == str(bin(number))[::-1].rstrip('b0')] #reverse
    palindromes = [number for number in bin_palindromes if str(number) == str(number)[::-1]]
    return palindromes
answer = sum(palindromes(1000000))
print(answer)