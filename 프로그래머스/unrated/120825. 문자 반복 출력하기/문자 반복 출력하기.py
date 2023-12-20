def solution(my_string, n):
    
    ans=''
    for i in range(len(my_string)):
            ans += (my_string[i]*n)
    
    return ans