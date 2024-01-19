def solution(my_string):
    ans = 0
    num = []
    
    for i in my_string:
        if(i.isnumeric()):
            num.append(i)
            
        elif(i.isnumeric()==False and len(num) != 0):
            ans += int("".join(num))
            num = []
    
    if (num):
        ans += int("".join(num))
        
    return ans
