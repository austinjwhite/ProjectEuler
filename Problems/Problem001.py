#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#variables for counting mulitples of 3
t = 0 #total for set of 3s
n = 1 #nth root

while n in range(1, 1000): #iterator

    k = (3 * n) #function k^n where n is multiples of 3
    n += 1
    if k < 1000: #ensures that we dont add values outside of 1000 to the total
        t = t + k

#variables for counting mulitples of 5
p = 0 #total for set of 5s
m = 1 #nth root

while m in range(1, 1000): #iterator

    l = (5 * m) #function l^m where m is multiples of 5
    m += 1
    if l < 1000: #ensures that we dont add values outside of 1000 to the total
        p = p + l

#variables for counting mulitples of 15
r = 0 #total for set of 15s
c = 1 #nth root

while c in range(1, 67): #iterator

    v = (15 * c) #function v^c where c is multiples of 15
    c += 1
    if v < 1000: #ensures that we dont add values outside of 1000 to the total
        r = r + v

print("t + p - r is:", (t + p - r)) #we substract r because the set of 15
                                    #multiples contains solutions from both the
                                    #set of 3 and 5, so we must remove one of
                                    #the duplicate sets (either 3 or 5)
#OUTPUT:
#t + p - v is: 233168
#[Finished in 0.144s]
