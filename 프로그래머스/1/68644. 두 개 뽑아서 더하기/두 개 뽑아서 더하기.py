import numpy as np

def solution(numbers):
    ans = []
    
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            ans.append(numbers[i] + numbers[j])
    
    ans = np.unique(ans)
    
    
    return ans.tolist()