# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def bound(n):
    boundnum = 1
    total = 0
    for i in range(0, 25):
        boundnum += 1

        if (n % boundnum) == 0:
            total += 1
            print(n, "Num to test")
            # print(boundnum, "integer to test it with")
            # print(n % boundnum, "the remainder")
            print(total, "hits")
        else: return False
        if total == 19: return True


    return False


def calc(n):
    if (n % 2) != 0: return False
    if bound(n) == True: return True

    return False
x = 10
while calc(x) == False:
    x += 1

print("smallest int is:",x)
