# The sum of the squares of the first ten natural numbers is,

#                 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,

#              (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the
# first ten natural numbers and the square of the sum is

#                     3025 - 385 = 2640

# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum

import math

fact = math.factorial(20)
print(fact)

def math(tester): #function that tests whether a number is divisible by 1, 2, ... 20
    num = 20
    total = 0
    while num > 0 and (tester % num) == 0: #test each number through 20, and make sure it has no remainder
        remainder = tester / num
        num -= 1
        total += 1
        if total == 20: #if a remainder is found, dont include it in the final print statement
            print("number divisible by 1 - 20:", testnum)
            print("multiplier:", multiplier)


multiplier = 99999999 #we increment down from a large number to find the smallest testnum
range = 20

while(multiplier > 999):
    testnum =  fact / ((3628800) * multiplier) #this formula is y = (20!)/((10!) * x)
    if (testnum % 2) == 0:                                   #where y is the number to test, x is the multiplier
        math(testnum)                                        #see Prob5ScratchStuff for more details
    multiplier -= 1
