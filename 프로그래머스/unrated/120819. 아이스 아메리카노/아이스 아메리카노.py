def solution(money):
    ans = [0,0]
    
    while(1):
        if(money >= 5500):
            money -= 5500
            ans[0] += 1
        else:
            ans[1] = money
            break
        
    return ans