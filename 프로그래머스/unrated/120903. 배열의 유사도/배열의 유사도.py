def solution(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        if(s1[i] in s2):
            cnt += 1
        
    return cnt