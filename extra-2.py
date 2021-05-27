import random
import math
from typing import Counter
import numpy as np
from scipy.integrate import quad
import time
from sympy import *

def cal_integral(fun,a,b,M,n):
    counter_neg = 0
    counter_pos = 0
    for i in range(0,n):
        x = random.uniform(a,b)
        y = random.uniform(0,M)
        if fun(x) < 0:
            value = max(0,-fun(x))
            if y < value :
                counter_neg+=1
        else :
            value = max(0, fun(x))
            if y < value :
                counter_pos+=1

    result = (counter_pos/n)*(b-a)*M - (counter_neg/n)*(b-a)*M

    return result

def main():
    fun=lambda x: (1/(sqrt(2*pi))) * E ** -(x*x)/2
    a=-6
    b=6
    M=1
    x=int(input("Enter order of magnitude: "))
    n=10**x
    time_start=time.time()
    print(cal_integral(fun,a,b,M,n))
    print(quad(fun, a, b))
    time_end=time.time()
    print('totally cost',time_end-time_start,'s')
main()

