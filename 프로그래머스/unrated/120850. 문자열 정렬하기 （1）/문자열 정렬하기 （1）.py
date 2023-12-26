import re

def solution(my_string):
    
    answer = re.sub("[a-z]", "", my_string)
    ans = list(map(int,answer))
    ans.sort()
    
    return ans