
#output shows the remainder - notice that certain values reoccour such as 360, 720, 1080 etc

# var = (720720 % 1080)
# print(var)
# print(720720 / (1080))
# var = (22 % 4)
# print(var)
# print(22 / 4)

# from random import *
# def is_prime(n): #boolean function to test if n is prime
#   if n == 2 or n == 3: return True
#   if n < 2 or n%2 == 0: return False
#   if n < 9: return True
#   if n%3 == 0: return False
#   r = int(n**0.5)
#   # since all primes > 3 are of the form 6n ± 1
#   # start with f=5 (which is prime)
#   # and test f, f+2 for being prime
#   # then loop by 6.
#   f = 5
#   while f <= r:
#     #print('\t',f)
#     if n % f == 0: return False
#     if n % (f+2) == 0: return False
#     f += 6
#   return True
#
# randomint = 0
# prime = 6857
#
# if is_prime(prime) == True:
#     print(prime / prime**2)
#     print(prime +1 / (prime**2 + 1))
#     print(randint(6000, 7000) + 1 / (randint(6000, 7000)**2 + 1))


# x = 17
# n = 720720
# if (n % x) == 0:
#     print("it is",n)
#     print(n % x)
# else:
#     print(n % x, n / x)


#-----------------original math that found the pattern----------------#


# 10! = 3628800
#
# 3628800 / 2520 = 1440
# 3628800 = 1440 * 2520
#
# 3628800 / 10 / 9 / 8 / 7 * 2 = 1440
#
# 3628800 / 1440 = 2520
#
# 20! = 2432902008176640000


#---------------------------------------------------------------#





# 20! / 20 / 19 / 18 / 17 * 2 = 41845579776000
#
# 2432902008176640000 / 41845579776000 = 58140

# 1 2 3 4 5 6 7 8 9      10 11 12 13 14 15 16 17 18 19 20
#
# ..10 ..20 ..30 ..40 ..50 ..60 ..70 ..80 ..90

# 10 factorial
# form = (3628800 / 10 / 9 / 8 / 7) * 2
#
# testnum = 3628800 / form
# num = 10
# print (testnum)
#
# for i in range (0, 10):
#     remainder = testnum / num
#     print(remainder, num)
#     num -= 1
#
#
# print( "")


#------------------------formula explained----------------------------------#


# 20! = 2432902008176640000
# (2432902008176640000 / 20 / 19 / 18 / 17 / 16 / 15 / 14 / 13 / 12 / 11) = 3628800 <--- this also happens to be 10!
# 3628800 * 2880 = 10450944000 #2880 is the multiplier
# 2432902008176640000 / 10450944000 = -----> 232792560 <-------
#
# i found the above formula by testing each divisor (20 / 19 / 18...) one after the other and checking
# the remainder of each digit 20 through 1 to verify that 3628800 is divisible by each with the code below.



#--------------------------------------------------------------------------#




# def math(tester):
#     num = 20
#     for i in range (0, 20):
#         remainder = tester / num
#         print(remainder, num)
#         num -= 1



def mathy(tester, NUMBER):

    num = NUMBER

    total = 0
    while num > 0 and (tester % num) == 0:
        remainder = tester / num
        num -= 1
        total += 1
        if total == NUMBER:
            #print("")
            print(remainder, num)
            print("number to try", testnum)
            # print("multiplier:", multiplier)

NUMBER = 20 #number to test the factorial of
multiplier = 999999
import math
fact = math.factorial(NUMBER)
print(fact)
augfact = math.factorial((NUMBER / 2))
while(multiplier > 999):
    testnum = fact / (augfact * multiplier)

    #print(testnum)

    if (testnum % 2) != 0:
        # print("")
        #print("number to try", testnum)
        # print("multiplier:", multiplier)
        mathy(testnum, NUMBER)

    multiplier -= 1








# import math
#
#
#
#
#
# def calc(n):
#     if (n % 2) != 0: return False
#
#     boundnum = 0
#     total = 0
#     for i in range(0, 20):
#         boundnum += 1
#
#         if (n % boundnum) == 0:
#             total += 1
#             print(n, "Num to test")
#             print("test", boundnum)
#             # print(n % boundnum, "the remainder")
#             print(total, "hits")
#         else: return False
#         if total == 20: return True
#
#
#     return False
#
#
# # def calc(n):
# #     if (n % 2) != 0: return False
# #     bool = bound(n)
# #     if bool == True: return True
# #
# #     return False
# x = 2432902008176630000
# while calc(x) == False:
#     x += 10
# print("smallest int is:",x)
