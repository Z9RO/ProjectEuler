# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 09:42:00 2017

@author: Z9RO
"""

def clain(num):
    terms = 0
    while num != 1:
        if num%2 == 0:
            num = num//2
        else:
            num = num*3+1
        terms = terms+1
        
    return terms

def main():
    num = 2
    terms = 0
    while num < 1000000:
        terms_temp = clain(num)
        if terms < terms_temp:
            terms = terms_temp
            num_m = num
        num = num+1
    print(terms)
    print(num_m)
#另一种思路，从1开始， to be continued..
if __name__ == '__main__':
    main()