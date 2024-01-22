def solution(chicken):

    coupons = chicken
    res = 0
    
    while(coupons>=10):
        
        # 10장 묶음 쿠폰으로 시키기
        service = coupons // 10
        res += service
        
        # 사용한 쿠폰 수만큼 빼고, 서비스 치킨으로 받은 쿠폰 추가
        coupons = coupons - (service * 10) + service 
       
      
    return res 

