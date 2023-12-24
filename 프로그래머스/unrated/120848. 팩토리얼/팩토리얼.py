import math

def solution(n):
    
    ans,i=1,1
    
    while(ans <=n):
        ans *= i
        i += 1
        
    return i-2
        