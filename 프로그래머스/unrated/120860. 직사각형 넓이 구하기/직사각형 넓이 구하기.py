import math

def solution(dots):
    
    w = max(dots[0][0], dots[1][0],dots[2][0],dots[3][0]) - min(dots[0][0], dots[1][0],dots[2][0],dots[3][0])
    
    h = max(dots[0][1], dots[1][1],dots[2][1],dots[3][1]) - min(dots[0][1], dots[1][1],dots[2][1],dots[3][1])
    
    return w*h
    
