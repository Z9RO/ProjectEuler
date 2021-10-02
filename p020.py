# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 11:42:52 2017

@author: Z9RO
"""
import math

def main():
    num = math.factorial(100)
    num = num//(100**12) 
    sum_n = 0
    while num>0:
        sum_n = sum_n+num%10
        num = num//10
    print(sum_n)

if __name__ == '__main__':
    main()