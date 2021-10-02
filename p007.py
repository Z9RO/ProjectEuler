# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:12:17 2017

@author: Z9RO
"""
import math

def isprime(a):
    if a==1:
        return False
    elif a<4:
        return True
    elif a%2 == 0:
        return False
    elif a<9:
        return True
    elif a%3==0:
        return False
    
    for i in range(5, 1+math.floor(math.sqrt(a)), 6):
        if a%i == 0 or a%(i+2) == 0:
            return False
    return True
    

def main():
    i = 2
    a = 3
    while i < 10001:
        a = a+2
        if isprime(a):
            i = i+1
    
    print(a)
    

if __name__ == '__main__':
    main()