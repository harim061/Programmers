def solution(nums):
    
    s = len(nums)
    cnt = 0

    for i in range(s):
        for j in range(i+1,s):
            for k in range(j+1,s):
                
                num = nums[i]+nums[j]+nums[k]
                
                # 1
                if (num == 1):
                    break
                
                # 2부터
                else:
                    d = 2
                    is_prime = True
                    
                    while(d<num):
                        
                        if(num % d != 0):
                            d+=1
                            
                        else:
                            is_prime = False
                            break
                        
                if(is_prime ==True):
                    cnt += 1
    return cnt

                
