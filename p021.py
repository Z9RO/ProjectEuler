# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 11:51:33 2017

@author: Z9RO
"""

import math

def div_sum(num):
    sqrt_n = math.sqrt(num)
    sqrt_nf = math.floor(sqrt_n)
    divs_sum = 2
    if (math.ceil(sqrt_n) == sqrt_nf) and (num%sqrt_nf == 0):
        divs_sum = divs_sum+sqrt_nf
    for i in range(2,math.floor(sqrt_n)):
        if num%i == 0:
            divs_sum = divs_sum+i
    return divs_sum
    

def main():
    
    print(num)

if __name__ == '__main__':
    main()