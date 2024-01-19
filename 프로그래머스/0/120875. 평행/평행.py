def solution(dots):
    
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
 
    # 0-1 2-3
    gx1 = (x1-x2) / (y1-y2)
    gy1 = (x3-x4) / (y3-y4)
    
    # 0-2 1-3
    gx2 = (x1-x3) / (y1-y3)
    gy2 = (x2-x4) / (y2-y4)
    
    # 0-3 1-2
    gx3 = (x1-x4) / (y1-y4)
    gy3 = (x2-x3) / (y2-y3)
    
    
    if(gx1 == gy1 or gx2 == gy2 or gx3 == gy3):
        return 1 
    else: 
        return 0
    
    