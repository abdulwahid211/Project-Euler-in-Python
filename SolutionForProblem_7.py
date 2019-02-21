# 10001st prime
# Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?



def isPrime(n):

    run = True
    limit = int(n/2)
    x = 2
    while(x<=limit and run):
        reminder = n%x

        if reminder ==0:
           run = False

        x +=1

    return run



def PrimeNumbers(n):
    count = 1
    prime_count = 2
    prime_number = 0
    while (count <= n):

      # when Prime Number is true
        if isPrime(prime_count):
            prime_number = prime_count
            print(str(count)+" = "+str(prime_count))
            prime_count += 1
            count += 1
      # when Prime Number is false
        if isPrime(prime_count) is False:
                while isPrime(prime_count) is False:
                      prime_count += 1

    return prime_number

print(PrimeNumbers(10001))



