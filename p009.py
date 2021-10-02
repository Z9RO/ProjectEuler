# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 16:45:40 2017

@author: Z9RO
"""

def main():
    k = 1000
    for a in range(1,500):
        if ((500-a)*k)%(k-a) == 0:
            break
    b = (500-a)*k//(k-a)
    c = int((a**2+b**2)**(1/2))
    print(a, b, c)
    print(a*b*c)
    return ''

if __name__ == '__main__':
    main()