def solution(n, numlist):
    ans=[]
    for i in range(len(numlist)):   
        
        if numlist[i] % n == 0:
            ans.append(numlist[i])
            
    return ans