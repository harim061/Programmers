def solution(array, commands):

    ans = []
    array_copy = array
    
    for line in commands: 
        a,b,c = line
        
        # slice
        array1 = sorted(array[a-1:b])
        
        # find
        ans.append(array1[c-1])

        array = array_copy
    
    return ans