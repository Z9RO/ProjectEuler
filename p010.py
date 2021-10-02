# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 09:04:38 2017

@author: Z9RO
"""

import math

def isprime(a):
    if a==1:
        return False
    elif a<4:
        return True
    elif a%2 == 0:
        return False
    elif a<9:
        return True
    elif a%3==0:
        return False
    
    for i in range(5, 1+math.floor(math.sqrt(a)), 6):
        if a%i == 0 or a%(i+2) == 0:
            return False
    return True

def main():
    num = 11 
    sum_p = 17
    k = True  #指标，用于确定下一个num+4or+2
    while num < 2000000:
        if isprime(num):
            sum_p = sum_p + num
        if k:
            num = num+2
        else:
            num = num+4
    print(sum_p)
    return ''

#另一种思路：边运行边生成一个质数表，isprime只需要除以质数表中的内容, to be continue...

if __name__ == '__main__':
    main()