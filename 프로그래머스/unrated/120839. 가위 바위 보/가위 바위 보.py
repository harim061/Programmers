def solution(rsp):
    # rsp : win
    win = {'2':'0','0':'5','5':'2'}
    
    return ''.join([win[r] for r in rsp])

