# Draw a 3x3 Board
# Choose symbols
# Select who starts first
  # Obviously Player1
# Place symbols alternatively until the board fills
  # Choose position
  # Flip player
# Check win or Tie
  #Check Rows
  #Check Columns
  #Check Diagonals 
# If won:
  # Check who wins


# Interested_in_Playing=True
winner=None
no_winner = True
current_player=None

board=[]
for i in range(9):
  board.append('-')

def display_board():
  print(board[0]+' | '+board[1]+' | '+board[2])
  print(board[3]+' | '+board[4]+' | '+board[5])
  print(board[6]+' | '+board[7]+' | '+board[8])

def player_turn(current_player):
  #Since index runs from 0-8
  position=int(input("Choose a position from 1-9:"))
  #If invalid input is given
  valid=False
  while not valid:
    if position not in range(1,10):
      position=input("Invalid input. Enter a number between 1-9:")
    position=int(position)-1
    #If position is already filled
    if board[position]=='-':
      valid=True
    else:
      print("That position is already occupied")
     

  board[position]=current_player
  display_board()


def check_end_status():
  global no_winner
  if check_win():
    no_winner=False
  elif check_tie():
    no_winner=False

def check_win():
  global winner
  if ((check_rows() or check_cols() or check_diagonals())==Player1_Symbol):
    winner=Player1_Symbol
    return True
  elif ((check_rows() or check_cols() or check_diagonals())==Player2_Symbol):
    winner=Player2_Symbol
    return True
  

def check_rows():
  for i in range(0,9,3):
    if (board[i]==board[i+1]==board[i+2]==Player1_Symbol):
      return Player1_Symbol
    if (board[i]==board[i+1]==board[i+2]==Player2_Symbol):
      return Player2_Symbol 

def check_cols():
  for i in range(0,3):
    if (board[i]==board[i+3]==board[i+6]==Player1_Symbol):
      return Player1_Symbol
    if (board[i]==board[i+3]==board[i+6]==Player2_Symbol):
      return Player2_Symbol 

def check_diagonals():
  if (board[0]==board[4]==board[8]==Player1_Symbol):
    return Player1_Symbol
  elif (board[0]==board[4]==board[8]==Player2_Symbol):
    return Player2_Symbol
  elif (board[2]==board[4]==board[6]==Player1_Symbol):
    return Player1_Symbol
  elif (board[2]==board[4]==board[6]==Player2_Symbol):
    return Player2_Symbol


def check_tie():
  global winner  
  if '-' not in board:
    winner=None
    return True


def flip_player():
  global current_player
  global Player1_Symbol
  global Player2_Symbol
  if current_player == Player1_Symbol:
    current_player = Player2_Symbol
    print("\nPlayer 2's turn")
  elif current_player == Player2_Symbol:
    current_player = Player1_Symbol
    print("\nPlayer 1's turn")


def choose_symbol():
  global Player1_Symbol
  global Player2_Symbol
  global current_player
  Player1_Symbol=input("Player 1 - Choose a symbol:")
  Player2_Symbol=input("Player 2 - Choose a symbol:")
  current_player=Player1_Symbol
  print("\nPlayer 1's turn")


def start_game():
  display_board() #Display the board
  choose_symbol() #Choose the symbol to play with
  while no_winner:
    player_turn(current_player) #Handle a single turn
    flip_player() #Flips the players turn
    check_end_status() #Check if the match ended
  if winner == Player1_Symbol:
    print("Player 1 wins")
  elif winner == Player2_Symbol:
    print("Player 2 wins")
  elif winner == None:
    print("The match is tied")

start_game()
