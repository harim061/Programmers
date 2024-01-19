def solution(lines):
    
    count_dict = {}

    for line in lines:
      
        x,y = line
        
        for j in range(0,y-x,1):
            
            if x+j in count_dict:
                count_dict[x+j] += 1
            else:
                count_dict[x+j] = 1
            
    return sum ( 1 for count in count_dict.values() if count >= 2)

        