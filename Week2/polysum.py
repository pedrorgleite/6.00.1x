# -*- coding: utf-8 -*-
"""
This file has 
- the area of a polygon
- the perimeter of a polygon 
- and the polysum that is the sum of the area and the perimeter squared
"""
def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    all_values = aDict.values()
    myDict = {}
    for value in all_values :
        if value in myDict:
            myDict[value] += 1
        else:
            myDict[value] = 1
    result = []
    for key in myDict:
        if myDict[key] ==1:
            result.append(get_key(key,aDict))
    final = []
    final = sorted(result)
    return final

def get_key(val,aDict): 
    for key, value in aDict.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"
  