def solution(n):
    
    result3 = ""
    
    # 앞뒤 반전 (3진법)
    while(n > 0):
        result3 += str(n%3)
        n = n//3
    
    result10 = 0
    
    # n(3진법)
    result3 = result3[::-1]
    
    # 10진법으로 표현
    for i in range(len(result3)):
        n = int(result3[i])
        
        # 자리 위치만큼 *3 
        for num in range(1,i+1):
            n *= 3
            
        result10 += n
        
    return result10 
        
    