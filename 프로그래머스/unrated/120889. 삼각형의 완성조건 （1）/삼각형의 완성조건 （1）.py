def solution(sides):
    
    max_num = max(sides)
    sides.remove(max(sides))
    
    return 2  if (max_num >= sum(sides)) else 1
    