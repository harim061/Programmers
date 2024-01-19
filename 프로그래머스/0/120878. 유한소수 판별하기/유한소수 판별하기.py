import math

def solution(a, b):
    
    a, b = a // math.gcd(a,b) , b // math.gcd(a,b)
    
    
    for prime in [2,5]:
        while(b % prime ==0):
            b= b // prime
 
            
    if (b==1):
        return 1
    else:
        return 2