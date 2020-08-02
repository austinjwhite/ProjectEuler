#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#variables for counting mulitples of 3
a = 3983
t = 0
n = 1
counteri = 0
while n in range(1, 1000):

    k = (3 * n)
    n += 1
    if k <= 990:
        t = t + k
        counteri += 1

#variables for counting mulitples of 5
#print(counteri)
p = 0
m = 1
counterj = 0
while m in range(1, 1000):

    l = (5 * m)
    m += 1
    if l <= 990:
        p = p + l
        counterj += 1



#variables for counting mulitples of 15
#print(counterj)
r = 0
c = 1
counterz = 0

while c in range(1, 67):

    v = (15 * c)
    c += 1
    if v <= 990:
        r = r + v
        counterz += 1
        #print(l)
    #print(p)
#print(counterz)
#print("a is:", a)
#print("t is:", t)
#print("p is:", p)
#print("r is:", r)
print("a + t + p - v is:", (a + t + p - r))
