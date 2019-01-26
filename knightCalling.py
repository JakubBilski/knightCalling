from math import *
x = sqrt(3+sqrt(5))/2
y = sqrt(3-sqrt(5))/2
A = (-4*x*x+6)/(2*y*y-2*x*x)
B = (2)/(2*x*y*y-2*x*x*x)
C = (4*y*y-6)/(2*y*y-2*x*x)
D = (-2)/(2*y*y*y-2*x*x*y)

def howManyFrom46(n):
    if n%2==0:
        return (B/(x**(n+1)) + D/(y**(n+1)))/4
    return (A/(x**(n+1)) + C/(y**(n+1)))/4
def howManyFrom82(n):
    if n==0:
        return 1
    if n==1:
        return 2
    return howManyFrom46(n) - howManyFrom46(n-2)
def howManyFrom1379(n):
    return howManyFrom46(n-1)+howManyFrom82(n-1)
def howManyFrom0(n):
    if n==0:
        return 1
    return 2*howManyFrom46(n-1)
def howManyFrom5(n):
    if n==0:
        return 1
    return 0

print(howManyFrom46(1))
print(howManyFrom82(1))
print(howManyFrom1379(1))
print(howManyFrom0(1))

print(howManyFrom46(3))
print(howManyFrom82(3))
print(howManyFrom1379(3))
print(howManyFrom0(3))

print(howManyFrom46(100))
print(howManyFrom82(100))
print(howManyFrom1379(100))
print(howManyFrom0(100))
