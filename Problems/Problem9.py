#     A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
#                                   a^2 + b^2 = c^2
#                       For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
#       There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#                              Find the product abc.


a = 0
b = 0
c = 334
def checkfunc(a, b, c):
    if (a**2 + b**2 ==c**2) and a + b + c == 1000:
        return True
    return False
while checkfunc(a,b,c) == False:
    a += 1
    if a == 1000:
        b += 1
        a = 0
        if b == 1000:
            c += 1
            b = 0
print("a:", a,"b:", b,"c:", c, "solution:" , (a*b*c))
