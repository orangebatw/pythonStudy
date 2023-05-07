def isWin():
  winner=whoWin()
  print (winner)
  if(winner == '_') :
    print ("No one Win")
#  else:
#    print (winner +" Win")


def whoWin():
  #row
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
  #column
  for j in range(3):
    if board[0][j] == board[1][j] == board[2][j]:
            return board[0][j] 
  #cross
  for x in range(0, 2):
      if board[x][0] == board[1][1] == board[2-x][2]:
        return board[x][0]       
  return '_'

board=[
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["o", "o", "o"]
]

whow=isWin()
print(whow)