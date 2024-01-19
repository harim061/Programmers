def solution(id_pw, db):
    
    id, pw = id_pw
    
    for re_db in db:
        d_id, d_pw = re_db
        
        if(id == d_id):
            if(pw == d_pw):
                return 'login'
            else:
                return "wrong pw"
            
    else:
        return 'fail'
        
    