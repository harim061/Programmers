def solution(before, after):
    
    for char in before:
        if(char in after):
            after = after.replace(char,"",1)
    
    if(after ==""):
        return 1
    
    else :return 0