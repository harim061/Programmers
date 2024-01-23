def solution(common):
    
    # 등차수열
    if (common[1] - common[0] == common[-1] - common[-2]):
        return common[-1] + (common[1]-common[0])
    
    # 등비수열
    else:
        return  common[-1] * (common[1]/common[0])
