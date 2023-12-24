def solution(num_list, n):
    
    return [[num_list[i+(j*n)] for i in range(n)] for j in range(int(len(num_list)/n))]
    

        