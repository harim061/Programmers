def solution(my_string):
    
    ans=""
    for i in range(len(my_string)):
        if my_string[i] not in ans:
            ans+=my_string[i]
            
    return ans