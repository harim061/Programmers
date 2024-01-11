def solution(keyinput, board):
    # x , y, -x, -y
    
    now = [0,0]
    line=[int(board[0]/2), int(board[1]/2), -int(board[0]/2),-int(board[1]/2)]
    
    for i in keyinput:
        if i == 'up' and line[1] > now[1]:
            now[1] += 1
        elif i == 'down' and line[3] < now[1]:
            now[1] -= 1
        elif i == 'left' and line[2] < now[0]:
            now[0] -= 1
        elif i == 'right' and line[0] > now[0]:
            now[0] += 1
            
    return now