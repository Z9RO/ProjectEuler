# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 20:31:01 2017

@author: Z9RO
"""
import math

def isprime(a):
    if a%2 == 0:
        return False
    for i in range(3, 1+int(math.sqrt(a)), 2):
        if a%i == 0:
            return False
    return True

def main():
    num = 600851475143
    ans_list = []
    ans = False
    for i in range(3, int(math.sqrt(num)), 2):
        if num%i == 0:
            ans_list.insert(0, i)
            if isprime(int(num/i)):
                print(int(num/i))
                ans = True
                break
    
    if (not ans):
        for i in ans_list:
            if isprime(i):
                print(i)
                break
    
if __name__ == '__main__':
    main()