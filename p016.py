# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 10:07:13 2017

@author: Z9RO
"""

def main():
    num = 2**1000
    sum_n =0
    while num>0:
        sum_n = sum_n+num%10
        num = num//10
    print(sum_n)

if __name__ == '__main__':
    main()