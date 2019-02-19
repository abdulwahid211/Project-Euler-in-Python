#
# Largest prime factor
# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


number = 600851475143

def largestPrimeFactor(n):
 num_max =0;
 for x in range(2,n):
     if(n%x==0 ):
         n = n/x
         if(x>num_max):
            num_max =x
     if (int(n) == 1):
       break

 return  num_max

print(largestPrimeFactor(number))
