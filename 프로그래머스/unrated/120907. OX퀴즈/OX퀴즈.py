def solution(quiz):
    res = []
    
    for i in range(len(quiz)):
        ev, ans = quiz[i].split('=')
        
        if eval(ev) == int(ans):
            res.append("O")
        else:
            res.append("X")
            
    return res
            