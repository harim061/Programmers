import math

def solution(n):
    
    sq = math.sqrt(n)
    
    if(n % sq == 0):
        return 1
    else: return 2