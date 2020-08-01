#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
a = 3983
t = 0
n = 1
counteri = 0
for i in range(3, 900):

    k = (3 * n)
    n += 1
    if k < 999:
        t = t + k
        counteri += 1
        #print(k)
    #print(t)


#print("END OF 3's")
#print("")
print(counteri)
p = 0
m = 1
counterj = 0
for j in range(3, 900):

    l = (5 * m)
    m += 1
    if l < 999:
        p = p + l
        counterj += 1
        #print(l)

print(counterj)
r = 0
c = 1
counterz = 0
for z in range(3, 900):

    v = (15 * c)
    c += 1
    if v < 999:
        r = r + v
        counterz += 1
        #print(l)
    #print(p)
print(counterz)
print("a is:", a)
print("t is:", t)
print("p is:", p)
print("v is:", v)
print("a + t + p - v is:", (a + t + p - v))
