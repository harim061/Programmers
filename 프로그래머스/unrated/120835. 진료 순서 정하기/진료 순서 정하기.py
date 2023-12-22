def solution(emergency):
    
    m = 0
    ans  =[0 for i in range(len(emergency))]
    
    for i in range(len(emergency)):
        ind = emergency.index(max(emergency))
        ans[ind] = i+1
        emergency[ind] = 0
    
    return ans
            