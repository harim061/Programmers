def solution(num_list):
    num= []

    for i in range(1,len(num_list)+1):
        num.append(num_list[-i])
        
    return num