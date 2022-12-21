# Initialize the board
board = [[Empty for _ in range(3)] for _ in range(3)]

# Initialize the players
player1 = 'X'
player2 = 'O'

# Initialize the current player
current_player = player1

# Game loop
while True:
  # Print the current board
  print(f'{board[0][0]} | {board[0][1]} | {board[0][2]}')
  print('---------')
  print(f'{board[1][0]} | {board[1][1]} | {board[1][2]}')
  print('---------')
  print(f'{board[2][0]} | {board[2][1]} | {board[2][2]}')
  
  # Prompt the player for their move
  row = int(input(f'{current_player}, enter row: '))
  col = int(input(f'{current_player}, enter column: '))
  
  # Make the move
  board[row][col] = current_player
  
  # Check for a win or a draw
  if (board[0][0] == current_player and board[0][1] == current_player and board[0][2] == current_player) or \
     (board[1][0] == current_player and board[1][1] == current_player and board[1][2] == current_player) or \
     (board[2][0] == current_player and board[2][1] == current_player and board[2][2] == current_player) or \
     (board[0][0] == current_player and board[1][0] == current_player and board[2][0] == current_player) or \
     (board[0][1] == current_player and board[1][1] == current_player and board[2][1] == current_player) or \
     (board[0][2] == current_player and board[1][2] == current_player and board[2][2] == current_player) or \
     (board[0][0] == current_player and board[1][1] == current_player and board[2][2] == current_player) or \
     (board[0][2] == current_player and board[1][1] == current_player and board[2][0] == current_player):
    print(f'{current_player} wins!')
    break
  elif ' ' not in [board[i][j] for i in range(3) for j in range(3)]:
    print('Draw!')
