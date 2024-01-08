def solution(n):
    num = 0
    n = str(n)
    
    for i in range(len(n)):
        num += int(n[i])
        
    return num