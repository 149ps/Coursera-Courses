""" 
Karatsuba Algorithm for multiplying to numbers using Divide and Conquer Algorithm
"""
"""
x = 5678
y = 1234


so, 
a = 56 i.e. 5678/100, b = 78 i.e 5678%100

c = 12 i.e. 1234/100, d = 34 i.e. 1234%100
"""

def karatsuba(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        n = max(len(str(x)),len(str(y)))
        nb = n//2
        a = x // (10**(nb))
        b = x % (10**(nb))
        c = y // (10**(nb))
        d = y % (10**(nb))
        ac = karatsuba(a,c)
        bd =  karatsuba(b,d)
        gauss_trick = karatsuba(a+b,c+d) - ac - bd
        return ac * 10**(nb*2) + gauss_trick * 10**(nb) + bd
print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))
