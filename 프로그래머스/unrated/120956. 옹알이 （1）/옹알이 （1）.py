def solution(babbling):
    
    cnt = 0
    
    for i in range(len(babbling)):
        babbling[i] = babbling[i].replace("aya",".")
        babbling[i] = babbling[i].replace("ye",".")
        babbling[i] = babbling[i].replace("woo",".")
        babbling[i] = babbling[i].replace("ma",".")
        babbling[i] = babbling[i].replace(".","")
        
        if(babbling[i] ==''):
            cnt += 1
            
    return cnt
    