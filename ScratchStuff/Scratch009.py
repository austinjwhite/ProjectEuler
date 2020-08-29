#
# foundnum = 1337
#
#
# a = 0
# b = 1
# c = 333
# numset = []
#
# for i in range(0, 800):
#     a = 0
#     b = 333
#     print(a, b , c)
#     while a >= 0 and a < b or c > b and c < 1000 and b > 0 and b < 1000:
#         if a <= (c / 2):
#             a += 1
#             b -= 1
#         else: break;
#         print(a, b , c)
#         if a + b + c == 1000 and a != 0 and b != 0 and c != 0 and a != b:
#             print("found",a, b, c)
#
#             numset.append(str(a) +","+ str(b) +","+ str(c) + ", asq + bsq= "+ str(a**2 + b**2) + ",csq ="+ str(c**2))
#             if (a**2 + b**2 == c**2):
#                 print("a:",a,"b:",b,"c",c)
#                 foundnum = a * b * c
#                 print("solution",foundnum)
#
#     #print(a, b , c)
#     c += 1
# print("solution",foundnum)
# print(numset)

#
#
# a2 + b2 = c2
#
# a + b + c = 1000



a = 0
b = 0
c = 334
itr = 0
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



    itr += 1
    #print("Checking...", a ,b ,c)
print("a:", a,"b:", b,"c:", c, "solution:" , (a*b*c))
