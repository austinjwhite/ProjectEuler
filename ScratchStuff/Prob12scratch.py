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

n = 0
count = 0
x = 0
itr = 0
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#
# countvsnum = np.array([[],[]])

countvsnum = np.array([[n,x]])
print(countvsnum.shape)
print(countvsnum)
# while count != 500:
while itr < 5000:
    #print("n",n)
    i = 1
    # if is_prime(n) == False:
    #     if n %2 == 0:
            #print("test",n)
    count = 0
    while i < n:

        if n % i == 0:
            count += 1
            #print("count",count)
            countvsnum = np.concatenate( ( [countvsnum, np.array([[n,count]]) ] ) , axis=0)
            if count == 500:
                print("this number has 500 factors",n)
        i += 1

    n += x
    x += 1
    itr += 1

pdFrame = pd.DataFrame((countvsnum), columns=['Num', 'Count'], dtype=np.int64)
pdFrame.to_csv("trianglenums2.csv")

# countvsnum = np.concatenate( ( countvsnum, [[n], [count]] ) , axis=0)
print(countvsnum)
