# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

x = 999
y = 999
xy = 0
#output = 0
largest = "Empty"


def flip(x):
    return x[::-1]
def palindrome(num):
    newnum = str(num)
    if flip(newnum) == newnum:
        return True
    return False

while y > 0:
        if (x > 0):

            xy = x * y
            palindrome(xy)
            if palindrome(xy) == True and int(xy) > 900000:
               print("The palindrome is", str(xy) + "!")

            x -= 1

        else:
            x = 999
            y -= 1


#993 * 913 = 906609




    #
    # for i in range(0, 1000):
    #     xy = x * y
    #     palindrome(xy)
    #     x -= 1
    #     print(xy)
    #
    #     if palindrome(xy) == True:
    #         print(largest)
    #


# test function below

# test = 9000001000009
#
#
# if palindrome(test) == True:
#     print("The palindrome is", str(test) + "!")
# else:
#     print("not a palindrome")
