# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 09:59:21 2017

@author: Z9RO
"""
import math

def main():
    n = 20
    ans = math.factorial(2*n)//((math.factorial(n))**2)
    print(ans)

if __name__ == '__main__':
    main()