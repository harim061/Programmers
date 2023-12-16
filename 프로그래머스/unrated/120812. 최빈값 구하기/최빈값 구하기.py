def solution(array):
    
    max_value = max(array)
    cnt = [0 for i in range(max_value+1)]
    
    for i in range(len(array)):
            cnt[array[i]] += 1

    max_cnt = max(cnt)
    ind =(cnt.index(max(cnt)))

    if(cnt.count(max_cnt)>=2):
        return -1

    return ind