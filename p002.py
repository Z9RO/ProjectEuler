# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 19:39:21 2017

@author: Z9RO
"""

def main():
    a, b, c =1, 2, 3
    sum_b = 0
    while b<4000000:
        sum_b = sum_b + b
        a, b, c= b+c, b+2*c, 2*b+3*c #a实际可忽略
    print(sum_b)

if __name__ == '__main__':
    main()