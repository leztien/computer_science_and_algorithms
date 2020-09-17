"""
Edit Distance Algorithms
"""

import numpy as np


def edit_distance(str1, str2):
    """Tabular Edit Distance"""
    m,n = len(str1), len(str2)
    table = np.zeros(shape=(m+1, n+1), dtype=np.uint8)
    
    table[0] = range(n+1)
    table[:,0] = range(m+1)
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                table[i,j] = table[i-1, j-1]
            else:
                table[i,j] = 1 + min(table[i-1, j-1], table[i-1, j], table[i, j-1])
    return table[-1,-1]




def edit_distance_recursive(str1, str2):
    """Recursive Edit Distance (with memoization)"""
    recursive_counter = 0
    cache = dict()
    
    def recurse(m,n):
        #counter
        nonlocal recursive_counter
        recursive_counter += 1
        
        #return form cache (comment the next line out and compare the number of recursions)
        if (m,n) in cache: return cache[(m,n)]  
        
        #base cases
        if m==0: return n
        elif n==0: return m
        
        #if last letters are the same
        elif str1[m-1] == str2[n-1]:
            ans = recurse(m-1, n-1)
        
        #if last letters are different 
        else:
            sub_cost = recurse(m-1, n-1)
            del_cost = recurse(m-1, n)
            ins_cost = recurse(m, n-1)
            ans = 1 + min(sub_cost, del_cost, ins_cost)
        
        #update the cache
        cache[(m,n)] = ans
        return ans
    
    #print out the number of recursions
    result = recurse(len(str1), len(str2))
    print("number of recursions", recursive_counter)
    return result

###############################################################################
# Test the two algorithms


str1 = "abcdef"
str2 = "XabcXfedX"


d = edit_distance(str1, str2)
print(d)

d = edit_distance_recursive(str1, str2)
print(d)
