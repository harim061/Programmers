def solution(order):
    ord = str(order)
    cnt = ord.count("3") + ord.count("6") + ord.count("9")
    return cnt
