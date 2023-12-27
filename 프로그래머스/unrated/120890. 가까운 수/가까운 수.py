def solution(array, n):
    
    array.sort()
    result = [abs(x - n) for x in array ]  
    
    return array[result.index(min(result))]