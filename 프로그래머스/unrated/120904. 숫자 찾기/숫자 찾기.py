def solution(num, k):
    num_str = str(num)
    k = str(k)
    
    if k in num_str:
        return num_str.index(k) +1
    
    else:return -1