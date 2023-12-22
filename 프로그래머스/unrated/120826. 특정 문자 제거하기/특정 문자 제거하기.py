def solution(my_string, letter):
    
    my_string = list(my_string)
    
    for i in range(len(my_string)):
        if(my_string[i] == letter):
            my_string[i] = ""
            
    my_string = ''.join(str(s) for s in my_string)
    
    return my_string