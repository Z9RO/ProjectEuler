# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:06:03 2017

@author: Z9RO
"""
#1
a = [x for x in range(1, 101)]
a1 = [x**2 for x in a]
sum1 = sum(a1)
sum2 = sum(a)**2
print(sum2-sum1)
#2
n = 100
sum_1 = n*(n+1)*(2*n+1)/6
sum_2 = ((1+n)*n/2)**2
print(sum_2-sum_1)