def solution(my_string):
    
    new=""
    
    for c in my_string:
        if(c.isupper()):
            new += c.lower()
        else:
            new += c.upper()
            
    return "".join(new)
            