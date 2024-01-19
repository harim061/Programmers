def solution(numlist, n):
    
    length = [(abs(n-x), -x) for x in numlist]

    # 거리와 숫자를 기준으로 정렬
    len_sort = sorted(length)

    # 정렬된 순서에 따라 원래 numlist에서 해당 값 선택
    result = [-x for _, x in len_sort]

    return result
