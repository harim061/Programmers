def solution(score):
    
    ave = [sum(x)/2 for x in score]

    ave_sort = sorted(ave,reverse=True)

    
    return [ave_sort.index(i)+1 for i in ave] 