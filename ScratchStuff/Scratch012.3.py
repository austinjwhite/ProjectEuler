
import pandas as pd
import numpy as np
import math
from itertools import permutations


def tri(n):
    trinum = (n * (n+1) / 2)
    return trinum
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

np.set_printoptions(formatter={'all':'{:f}'.format})

for i in range(1000, 10000):

    allproducts = np.array([])
    lenprimes = len(primefac(tri(i)))
    #print(lenprimes, primefac(tri(i)))
    #print(tri(i))
    #print(primefac(tri(i)))
    while lenprimes > 0:
        perm = permutations(primefac(tri(i)), lenprimes - 1)

        #print("perm",list(perm))


        permlist = list(perm)
        permlistlen = (len(permlist) - 1)
        #print(permlist, permlistlen)
        #print(primefac(tri(i)))
        prodarray = np.array([])

        while permlistlen >= 0:
            #print(math.prod(permlist[permlistlen]))
            tempprod = math.prod(permlist[permlistlen])
            prodarray = np.append(prodarray, tempprod)

            permlistlen -= 1
        #print(prodarray)

        allproducts = np.append(allproducts, prodarray)
        lenprimes -= 1

    allproducts = np.unique(allproducts)
    allproducts = np.append(allproducts, tri(i))

    if len(allproducts) > 500:
        print("FOUND -->", tri(i))
    #print("all factors of---",tri(i),"----",allproducts)
#perm = permutations(primefac(tri(20)), 2)


#print(list(perm))
