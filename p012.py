# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 09:15:49 2017

@author: Z9RO
"""
import math

def divisor(num):
    sqrt_n = math.sqrt(num)
    sqrt_nf = math.floor(sqrt_n)
    divs_num = 2
    if (math.ceil(sqrt_n) == sqrt_nf) and (num%sqrt_nf == 0):
        divs_num = divs_num+1
    for i in range(2,math.floor(sqrt_n)):
        if num%i == 0:
            divs_num = divs_num+2
    return divs_num
    

def main():
    n = 10
    
    while True:
        num = n*(n+1)//2
        if divisor(num) > 500:
            break
        n = n+1
    print(num)

if __name__ == '__main__':
    main()