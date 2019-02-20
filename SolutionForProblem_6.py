#
# Smallest multiple
# Problem 5
# #
# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def SquaresOfSum(n):
    sum =0;
    for i in range(1,n+1):
        sum = sum + i


    sum = sum**2

    return sum


def SumOfSquares(n):
    sum =0;
    for i in range(1,n+1):
        sum = sum + (i**2)

    return sum


print(SquaresOfSum(100) - SumOfSquares(100))