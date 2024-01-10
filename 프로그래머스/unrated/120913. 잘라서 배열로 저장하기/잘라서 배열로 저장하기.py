import math

def solution(my_str, n):
    
    ans =[]
    for i in range(math.ceil(len(my_str)/n)):
        ans.append(my_str[:n])
        my_str = my_str[n:]
    
    return ans