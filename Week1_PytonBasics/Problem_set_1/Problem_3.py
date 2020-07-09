# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:28:33 2020

@author: pedri
"""


temp = ''
foo = ''
s = 'azcbobobegghakl'
s+='a'
for n in range(len(s)-1):
    if s[n]<=s[n+1]:
        temp += s[n]
    else:
        temp +=  s[n]
        if len(temp)>len(foo):
            foo = temp
            temp = ''
        else: temp = ''
s = s[:-1]            
print(foo)


    
