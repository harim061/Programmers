def solution(new_id):
    
    # 1
    new_id = new_id.lower()
    
    # 2
    ok_str = 'abcdefghijklmnopqrstuvwxyz1234567890-_.'
    new_id = ''.join(c for c in new_id if c in ok_str)
    
    # 3
    result = []
    for c in new_id:
        if not (result and result[-1] == c and c=='.') :
            result.append(c)
    new_id = ''.join(result)
    
    # 4
#     if (id_3[0] == '.'):
#         if(id_3[-1]=='.'):
#             id_4 = id_3[1:-1]
        
#         else:
#             id_4 = id_3[1:]
#     else:
#         if(id_3[-1]=='.'):
#             id_4 = id_3[0:-1]
#         else:
#             id_4 = id_3

    new_id = new_id.strip('.')
    
    # 5
    new_id = new_id if new_id else "a"
     
    
    # 6
    new_id = new_id[:15].strip('.')
  
        
    # 7
    if(len(new_id)<= 2):
        while(len(new_id) !=3):
            new_id += new_id[-1]
 
            
    return new_id 
    
    