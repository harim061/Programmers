import math 

def solution(num, total):

    x= ((total / (num/2)) - (num-1)) /2 
    

    return [int(x+i) for i in range(num)]
        