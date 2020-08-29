#

import pandas as pd
import numpy as np




#def is_prime(n): #boolean function to test if n is prime
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
# n = 0
# count = 0
# x = 0
# itr = 0
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# #
# # countvsnum = np.array([[],[]])
#
# countvsnum = np.array([[n,x]])
# print(countvsnum.shape)
# print(countvsnum)
# # while count != 500:
# while itr < 5000:
#     #print("n",n)
#     i = 1
#     # if is_prime(n) == False:
#     #     if n %2 == 0:
#             #print("test",n)
#     count = 0
#     while i < n:
#
#         if n % i == 0:
#             count += 1
#             #print("count",count)
#             countvsnum = np.concatenate( ( [countvsnum, np.array([[n,count]]) ] ) , axis=0)
#             if count == 500:
#                 print("this number has 500 factors",n)
#         i += 1
#
#     n += x
#     x += 1
#     itr += 1
#
# pdFrame = pd.DataFrame((countvsnum), columns=['Num', 'Count'], dtype=np.int64)
# pdFrame.to_csv("trianglenums2.csv")
#
# # countvsnum = np.concatenate( ( countvsnum, [[n], [count]] ) , axis=0)
# print(countvsnum)













import pandas as pd
import numpy as np

num = 99991
def primefac(n):
    product = -999
    factors = np.array([])
    oddtest = 3
    while n > 1:
        # print(oddtest, n, factors, n % oddtest, "n/odd",n / oddtest)
        if n % 2 == 0:
            if n == 2:
                return factors
            n = n / 2
            n = int(n)
            factors = np.append(factors, 2)
        else:
            if n % oddtest == 0:
                # print(oddtest, n**2)
                factors = np.append(factors, oddtest)
                # print("appended", oddtest)
                n = n / oddtest
                n = int(n)
                oddtest == 3
                # print("reset oddtest", oddtest)
                if n == oddtest:
                    # print('n = oddtest, appending and returning')
                    factors = np.append(factors, oddtest)
                    return factors
            else:
                oddtest += 2
    return factors

      #--------MATH----------#
    #print(factors)
def math(n):
    l = 0
    m = 0
    allfact = np.array([])
    n = np.unique(n)
    print(n)
    bigvars = 0
    for i in range(0, len(n)):
        bigvars = bigvars + (int(n[l]) * int(n[i]))
        allfact = np.append(allfact, bigvars)

    q = 0
    z = 0
    while q < len(n):
        print((q,z))
        print((n[q], n[z]), (n[q] * n[z]))
        if int(int(n[q]) * int(n[z])) <= num/2:

            if( n[q] % n[z] != 0) and ( n[z] % n[q] != 0):
            # if( n[q] != (n[z]**2) ) and (n[z] != n[q]**2) and (n[q] != n[z]) and q != z:
                print("appending:", int(n[q]) * int(n[z]) )
                allfact = np.append(allfact, int(n[q]) * int(n[z]))

        z += 1

        if z == len(n):
            z = z * 0

            q += 1
    allfact = np.append(allfact, n)

    return allfact

#-------------END FUNC-----------#

np.set_printoptions(formatter={'all':'{:f}'.format})

def findpowers(n):
    itr = 0
    i = 0
    powerapp = np.array([])

    unique, counts = np.unique(n, return_counts=True)
    print("unique",unique, len(unique))
    print("counts",counts,len(counts))
    powerapp = np.append(powerapp, n)
    while i < len(unique):

        #powerapp = np.append(powerapp, n)
        indecies = counts[i]
        while indecies > 1:
            powerapp = np.append(powerapp, (unique[i])**indecies)
            print(unique[i], indecies,(unique[i])**indecies)
            indecies -= 1
            print(indecies)
        i += 1
    return powerapp

done = np.array([num, 1])
done = np.append(done, math(findpowers(primefac(num))))
#print(done)

done = np.unique(done)
# print(len(np.unique(done)))
print(done)
#print(done)
# print("array is", primefac(num))
# print(len(primefac(num)))
# facarray = primefac(num)

# for i in range(0,facarray.size()):
#     product
