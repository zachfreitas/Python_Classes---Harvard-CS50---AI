

X = "X"
O = "O"
EMPTY = None

board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]



def isWinner(board, player):
    winCombinations = [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9],
                       [1, 5, 9],
                       [3, 5, 7],
                       [1, 4, 7],
                       [2, 5, 8],
                       [3, 6, 9]]
    return any(
        all(board[cell] == player for cell in line) 
        for line in winCombinations)
    


print(list(map(sum, zip([[6, 7, 2],
                         [1, 5, 9],
                         [8, 3, 4]], [[1, 1, 1],
                                      [0, 0, 0],
                                      [0, 0, 0]]))))
