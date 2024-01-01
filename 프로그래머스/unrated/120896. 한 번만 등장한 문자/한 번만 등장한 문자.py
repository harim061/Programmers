from collections import Counter

def solution(s):
    
    count_dict = Counter(s)

    return ''.join(sorted(char for char, count in count_dict.items() if count == 1))
