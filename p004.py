# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 20:31:01 2017

@author: Z9RO
"""

def ispal(a):
    b = 0
    temp = a
    while a>0:
        b = b*10+a%10
        a = a//10
    if temp == b:
        return True
    else:
        return False

def main():
    alist = list({x*y for x in range(100,1000) for y in range(100,1000)})
    alist.sort(reverse=True)
    for i in alist:
        if ispal(i):
            print(i)
            break

if __name__ == '__main__':
    main()