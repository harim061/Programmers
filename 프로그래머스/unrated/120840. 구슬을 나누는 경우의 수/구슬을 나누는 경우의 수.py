def solution(balls, share):
    
    n,m,nm = 1,1,1
    
    for i in range(1,balls):
        n *= i+1
    
    for i in range(share):
        m *= i+1
        
    for i in range(balls-share):
        nm *= i+1
       
    return n/(m*nm)