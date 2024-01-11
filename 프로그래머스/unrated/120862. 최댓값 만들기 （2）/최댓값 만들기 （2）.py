def solution(numbers):
    
    sort_num = sorted(set(numbers),reverse=True)
    
    abs_num = [abs(n) for n in numbers]
    
    max_num = max(abs_num)
    
    if(len(sort_num)==1):
        return sort_num[0] **2
    
    elif(numbers[abs_num.index(max_num)] <0 and sort_num[-2]<0):
        return numbers[abs_num.index(max_num)] * sort_num[-2]
        
    elif (numbers[abs_num.index(max_num)] <0 and sort_num[-2]>=0):
        return sort_num[0] * sort_num[1]
    
    else:
        return sort_num[0] * sort_num[1]