def solution(common):
    
    # 공차수열
    if (common[1] - common[0] == common[-1] - common[-2]):
        return common[-1] + (common[1]-common[0])
    
    # 공비수열
    else:
        return  common[-1] * (common[1]/common[0])