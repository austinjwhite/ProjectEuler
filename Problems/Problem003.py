# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


def is_prime(n): #boolean function to test if n is prime
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


n = 600851475143 #what is the largest prime factor of this integer?
divisor = 2 #iterates the divisor of n to find which numbers divide without remainder
count = 0

while is_prime(n) == False: #loop until the number becomes prime
    count += 1

    if(n % divisor) == 0:   #if it has no remainder
        n /= divisor        #divide by the current divisor
    else:
        divisor += 1        #if it does have a remainder, that mean that we hit
                            #a non-factor, so we bump up the divisor to check again

print(n)
print("iterations to reach largest prime:", count)
