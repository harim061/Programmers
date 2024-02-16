def solution(s, n):
    
    new_char =""
    
    for char in s:
        
        # 공백
        if(char == " "):
            new_char += " "
            
        else:
            nc = ord(char) + n
         
            # 원래 대문자인데 
            if(65 <= ord(char) and ord(char) <= 90) :
                
                # 아직 대문자임
                if(65 <= nc and nc <= 90):
                    new_char += chr(nc)
                    
                # 소문자됨
                elif (97 <= nc and nc <= 122):
                    new_char += chr(ord(char) - 26 +n)
                
                else:
                    new_char += chr(nc-26)
                
                
            # 원래 소문자임    
            else:
                # 아직 소문자
                if(97 <= nc and nc <= 122) :
                    new_char += chr(nc)
                
                # 소문자 범위 넘음
                else:
                    new_char += chr(nc-26)
          
    return new_char