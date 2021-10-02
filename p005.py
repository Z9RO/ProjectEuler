# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 21:47:57 2017

@author: Z9RO
"""

def eu(a, b):
    while b!=0:
        a, b = b, a%b
    return a

def main():
    ans = 20
    for i in range(19,1,-1):
        ans = ans*int(i/eu(ans, i))
    print(ans)

if __name__ == '__main__':
    main()