def solution(hp):
    
    # 장군 5 / 병정 3 / 일개미 1
    # 23 = 장군 4 * 5 + 병정 1 * 3
    # 24 = 장군 4 병정 1 일개미 1 
    cnt = 0
    
    cnt += int(hp/ 5)
 
    cnt += int(hp%5/3)
    
    cnt += int(hp %5%3/1)
    
    
    return cnt