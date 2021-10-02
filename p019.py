# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 11:02:28 2017

@author: Z9RO
"""

def main():
    days = {1:31,3:31,5:31,7:31,8:31,10:31,12:31,
            4:30,6:30,9:30,11:30,2:28}
    zhou = 3
    num = 0
    
    for years in range(1901, 2001):
        if years%4==0:  #2000 is a leap year,so don't care 100 or 400
            leap = 1
        else:
            leap = 0
        for mouths in range(1,13):
            day = days[mouths]
            if mouths == 2:
                day = day+leap
            if zhou == 0:
                num = num+1
            zhou = (zhou +day)%7
        
    print(num)
    

if __name__ == '__main__':
    main()