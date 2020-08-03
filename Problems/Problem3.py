# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# n = 13195
def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n ± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6.
  f = 5
  while f <= r:
    #print('\t',f)
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True
#
#
# while is_prime(n) == False:
#
#     #if counter < 50:
#         if is_prime(n) == True:
#             print(n)
#         n += 1

# def intAssign(div):
#
#     return null



n = 600851475143
divisor = 2
while is_prime(n) == False:
    if(n % divisor) == 0:
        n /= divisor

        #intAssign(divisor)
    else:
        divisor += 1
        #print("divisor +1")
    print(n)
    #print("while loops")

# if (n % 2) == 0:
#     n /= 2
# elif(n % 3) == 0:
#     n /= 3
# elif(n % 4) == 0:
#     n /= 4
