def solution(age):
    answer=""
    
    age_list = list(map(str, str(age)))
    
    dic = {"0": "a", "1": "b", "2": "c", "3": "d", "4": "e", "5": "f", "6": "g", "7": "h", "8": "i", "9": "j"}

        
    for i in range(len(age_list)):
        answer += dic[age_list[i]]
        
    return answer