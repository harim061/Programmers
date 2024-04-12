def solution(N, stages):
    
    stage_count = [0] * (N+2)
    
    for stage in stages:
        stage_count[stage] +=1
        
    
    players = len(stages)
    rates = []
    
    for i in range(1,N+1): # N=5 > 1~5까지 
        if players > 0:
            current_p = stage_count[i] # 현재 stage 몇 명
            failure_rate = current_p / players # 실패율
            rates.append((failure_rate,i)) # 저장
            players -= current_p # player 수 삭제 
        
        else:
            rates.append((0,i))
    
    # 실패율 내림차순, 스테이지 오름차순
    rates.sort(key=lambda x: (-x[0],x[1]))
    
    
    return [stage for _, stage in rates]
    