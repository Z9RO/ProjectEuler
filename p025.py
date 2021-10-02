# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 13:49:28 2017

@author: Z9RO
"""
import math

def main():
    a, b =1, 1
    i = 2
    while math.log(a+1, 10) < 999:
        a, b = a+b, a
        i = i+1
        
    print(i)
    
if __name__ == '__main__':
    main()
