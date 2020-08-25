# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

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


multiplier = 999999 #we increment down from a large number to find the smallest testnum

while(multiplier > 999):
    testnum = 2432902008176640000 / ((3628800) * multiplier) #this formula is y = (20!)/((10!) * x)
    if (testnum % 2) == 0:                                   #where y is the number to test, x is the multiplier
        math(testnum)                                        #see Prob5ScratchStuff for more details
    multiplier -= 1
