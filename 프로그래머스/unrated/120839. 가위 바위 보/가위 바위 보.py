def solution(rsp):
    # rsp : win
    win = {'2':'0','0':'5','5':'2'}
    ans = []
    
    for i in range(len(rsp)):
        ans.append(win[rsp[i]])
        
    
    return ''.join(ans)