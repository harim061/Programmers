def solution(n):
    
    res = 0
    
    for i in range(n):
        
        res +=1
        
        while (res % 3 == 0) or ('3' in str(res)):
            res +=1 
    
    return res