#
# Largest palindrome product
# Problem 4
# #
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalin(n):
    rev = ''
    i = len(str(n))-1

    while i>-1:
         rev += str(n)[i]
         i = i - 1

    return str(n) == rev



def largestPalindromeNumber():
 number = 0
 max_palin = 0
 for i in range(100,999,1):
    for j in range(1000):
        number = i*j

        if(isPalin(number) and number > max_palin):
          max_palin = number


 return max_palin



print(largestPalindromeNumber())

