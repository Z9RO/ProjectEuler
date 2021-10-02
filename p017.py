# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 10:12:13 2017

@author: Z9RO
"""

def shiwei(num, l_n):
    letter = 0
    if num in l_n.keys():
        letter = l_n[num]
    else:
        letter = l_n[num%10]+l_n[num//10*10]
    return letter

def main():
    letters =  11
    l_n = {1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,
           16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,100:7,
           0:0}
    
#    for n1 in range(1, 21):
#        letters = letters+l_n[n1]
    
#    for n2 in range(21, 101):
#        letters = letters+shiwei(n2, l_n)
    
    for n in range(1, 1000):
        if n%100==0:
            letters = letters+l_n[n//100]+l_n[100]
        else:
            letters = letters+l_n[n//100]+shiwei(n%100, l_n)
            if n > 100:
                letters = letters+3+l_n[100]
    
    print(letters)
    
if __name__ == '__main__':
    main()