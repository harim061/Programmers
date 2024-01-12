def solution(polynomial):

    x = 0
    num  = 0
    for term in polynomial.replace(" ","").split('+'):
        
        if 'x' in term:
            if(len(term) !=1):
                x += int(term[:-1])
            else:
                x += 1
            
        else:
            num += int(term)
      
    # x만 있을 때
    if ( num == 0):
        # x 계수가 1일 때
        if(x == 1): return "x"
        else:
            return str(x) + "x"
     
    # 상수만 존재
    elif (x == 0):
        return str(num)
    
    # 둘다 존재
    else:
        # x 계수가 1일 때
        if(x == 1): return "x +" + ' ' + str(num)
        else:
            return str(x) +"x +" +' ' + str(num)
            