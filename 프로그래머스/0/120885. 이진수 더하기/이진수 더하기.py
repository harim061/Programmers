def solution(bin1, bin2):
    
    a = int(bin1,2)
    b = int(bin2,2)
    
    res = bin(a+b)
    
    return res[2:]