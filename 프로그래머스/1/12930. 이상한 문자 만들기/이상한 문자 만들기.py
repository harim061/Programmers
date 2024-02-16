def solution(s):
    words = s.split(' ')
    result = []
    
    for word in words:
        new_word = ''
        for c in range(len(word)):
            if(c % 2 == 0):
                new_word += word[c].upper()
            else:
                new_word += word[c].lower()
                
        result.append(new_word)
                
    return(' '.join(result))
   