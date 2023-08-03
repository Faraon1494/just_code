import random
import math

def begin7(R):
    L = 2*math.pi*R
    S = math.pi*(R**2)
    return L,S

def begin8(a,b):
    avg = (a + b)/2
    return avg

def begin9(a,b):
    if a >= 0 and b >= 0:
        geo_avg = math.sqrt(a * b)
    return geo_avg

def begin10(a,b):
    if a != 0 and b != 0:
        summ = a + b
        diff = a - b
        prod = a * b
        div = a / b
    return summ, diff, prod, div

def begin11(a,b):
    if a != 0 and b != 0:
        summ = a + b
        diff = a - b
        prod = a * b
        mod = math.fabs(a / b)
    return summ, diff, prod, mod

def begin12(a,b):
    c = math.sqrt((a**2) + (b**2))
    P = a - b + c
    return c, P

def begin14(L):
    R = L/(math.pi*2)
    S = math.pi*math.pow(R,2)
    return R, S

def begin15(S):
    D = math.sqrt((4*S)/math.pi)
    L = math.pi*D
    return L, D
