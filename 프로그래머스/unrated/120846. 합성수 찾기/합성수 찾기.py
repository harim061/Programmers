def solution(n):
    
    cnt = 0
    
    for i in range(3,n+1,1):
        for j in range(2,i,1):
            if( i % j ==0):
                cnt += 1
                break
    

    return cnt