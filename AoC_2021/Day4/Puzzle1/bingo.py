def load_balls():
    balls = open("balls.txt")
    ball = next(balls).split(",")
    return ball

def load_boards():
    board_num = 0
    board = []
    board.append([])
    boards = open("boards.txt")
    i = 0
   
    while True:
        try:
            line = next(boards)
            if line == "\n":
                board.append([])
                board_num = board_num + 1
                i = 0
            else:
                board[board_num].append(line.split())
        except:
            break
    return board

def play():
    balls = load_balls()
    boards = load_boards()
    for ball in balls:
        for board in boards:
            for line in board:
                if ball in line:
                    ind = line.index(ball)
                    line[ind] = "X"
                    col = [board[0][ind],board[1][ind],board[2][ind],board[3][ind],board[4][ind]]
                    print("found one " + ball)
                    if bingo(line):
                        return score(board) * int(ball)
                    elif bingo(col):
                        return score(board) * int(ball)
                else:
                    print("no match " + ball)


def bingo(line):
    for v in line:
        if v != "X":
            return False
    return True

def score(board):
    tot = 0
    for line in board:
        for v in line:
            if v != "X":
                tot = tot + int(v)
    return tot

print(play())