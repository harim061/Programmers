def solution(A, B):
    
    if(A==B):
        return 0
    
    cnt = 0
    
    for i in A:
       
        A = A[-1] + A[:-1]
       
        if(A!=B):
            cnt += 1  
            
        else:
            cnt +=1
            break

    
    if(cnt==len(A)):
        return -1
    else: 
        return (cnt)