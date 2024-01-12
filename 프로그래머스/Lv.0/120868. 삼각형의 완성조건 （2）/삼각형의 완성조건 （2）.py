def solution(sides):
    max_s = max(sides)

    return (sides[0] + sides[1] - max_s -1) +( max_s - abs(sides[0] - sides[1]) )
    