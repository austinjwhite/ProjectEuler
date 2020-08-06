
#output shows how many digits are in the remainder - notice that certain values reoccour such as 360, 720, 1080 etc

# var = (720720 % 1080*3)
# print(var)
# print(720720 / (1080*3))
# var = (22 % 4)
# print(var)
# print(22 / 4)
#
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
x = 17
n = 720720
if (n % x) == 0:
    print("it is",n)
    print(n % x)
else:
    print(n % x)










1 2 3 4 5 6 7 8 9      10 11 12 13 14 15 16 17 18 19 20

..10 ..20 ..30 ..40 ..50 ..60 ..70 ..80 ..90
