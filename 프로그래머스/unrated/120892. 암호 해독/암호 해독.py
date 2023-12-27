def solution(cipher, code):
    

    ans = [cipher[m] for m in range(len(cipher)) if (m +1)% code == 0]
        
    return "".join(ans)