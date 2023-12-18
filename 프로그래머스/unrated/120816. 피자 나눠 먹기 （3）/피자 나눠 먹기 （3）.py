def solution(slice, n):
    if n% slice != 0:
        return int(n/slice) +1
    else:
        return n/slice