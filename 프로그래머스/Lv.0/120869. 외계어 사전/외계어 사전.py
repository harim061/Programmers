def solution(spell, dic):
    
    res = False
    
    for word in dic:
        spell_copy = spell.copy()
        for char in word:
            if(char in spell_copy):
                spell_copy.remove(char)
                
            else:
                break
        
        else:
            if not spell_copy:
                res = True
                break
        
    
    if res==True :return 1 
    else: return 2
        