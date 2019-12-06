# Smallest multiple
#
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def smallestMultiple(start, end):
    limit = 1000000000
    total = start + end

    total = total - 1
    counter = 0
    number = 0

    for i in range(1, limit):
        for j in range(start, end+1):
            # print(str(i)+ " "+str(j))
            if i % j == 0:
                counter = counter + 1
                # print("counter: "+str(counter))
            else:
                counter = 0
                continue

        if counter == total:
            number = i
            break

    return number

print(smallestMultiple(1,20))
