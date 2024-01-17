def solution(board):
    bomb = []
    n = len(board)
    total = n*n
    unsafe = set()

    for i in range(n):
        for j in range(n):
            if(board[i][j] == 1):
                
                for x in range(max(0, i - 1), min(n, i + 2)):
                    for y in range(max(0, j - 1), min(n, j + 2)):
                        unsafe.add((x, y))
                        

    return n*n - len(unsafe) 