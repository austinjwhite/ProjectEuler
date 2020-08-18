# The sum of the squares of the first ten natural numbers is,

#                 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,

#              (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the
# first ten natural numbers and the square of the sum is

#                     3025 - 385 = 2640

# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum

ans = 0
x = 0
y = 0
z = 0
for i in range(0, 100):
    x += 1
    y = x**2
    z = z + y
print("sum of the squares:",z)

a = 0
b = 0
for i in range(0, 100):
    a += 1
    b = b + a
b = b**2
print("square of the sums",b)
ans = b - z
print("2nd minus 1st:",ans)
