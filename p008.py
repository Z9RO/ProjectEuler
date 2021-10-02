# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 16:05:25 2017

@author: Z9RO
"""
import re

def max13(str1):
    m = 1
    i = 0
    num = []
    for j in str1:
        num.append(int(j))
    
    for num1 in num:
        if i<12:
            m = m*num1
        elif i == 12:
            m = m*num1
            temp = m
        else:
            temp = temp*num1//num[i-13]
            m = max(temp, m)
        i = i+1
    return m

       

def main():
    with open(r'C:\Users\Z9RO\Desktop\a.txt', 'rt') as f:
        a = f.read()
    a_n = re.sub('\n', '', a)
    a_0 = re.split('0', a_n)
    str0 = [i for i in a_0 if len(i)>=13]
    c = 0
    
    for i in str0:
        c =  max(max13(i), c)
                    
    print(c)

if __name__ == '__main__':
    main()