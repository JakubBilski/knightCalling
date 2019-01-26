from math import *

def A(x,y):
    return (2*x*x*x-3*x-1)/(2*x*y*y-2*x*x*x)
def B(x,y):
    return (2*x*x*x-3*x+1)/(2*x*y*y-2*x*x*x)
def C(x,y):
    return -(2*y*y*y-3*y-1)/(2*y*y*y-2*x*x*y)
def D(x,y):
    return -(2*y*y*y-3*y+1)/(2*y*y*y-2*x*x*y)
x = sqrt(3+sqrt(5))/2
y = sqrt(3-sqrt(5))/2
def howManyFrom46(n):
    return ((-A(x,y) + (-1)**n*B(x,y))/(x**(n+1)) + (-C(x,y) + (-1)**n*D(x,y))/(y**(n+1)))/4
def howManyFrom82(n):
    if n==0:
        return 1
    if n==1:
        return 3
    return howManyFrom46(n) - howManyFrom46(n-2)
def howManyFrom1379(n):
    return howManyFrom46(n-1)+howManyFrom82(n+1)
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
