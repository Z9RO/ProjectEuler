# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 12:58:05 2017

@author: Z9RO
"""
import re

def num(a_str):
    a_num = 0
    for i in a_str:
        a_num = a_num + ord(i)-64
    return a_num

def main():
    with open(r'C:\Users\Z9RO\Desktop\p022_names.txt', 'rt') as f:
        a = f.read()
    b = re.findall('\w+', a) 
    b.sort()
    sum_b = 0
    for i in b:
        sum_b = sum_b + num(i)*(b.index(i)+1)
    print(sum_b)
    return ''

if __name__ == '__main__':
    main()