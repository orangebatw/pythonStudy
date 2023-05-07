board=[]
for i in range(3):
    board.append(['_','_','_'])
game=True
name1=True
n=len(board)
while name1:
    player1=input("Enter the name that you would like to play as player 1(max 10 characters): ")
    if len(player1)>10:
        print("invalid name")
    else:
        name1=False
name2=True
while name2:
    player2=input("Enter the name that you would like to play as player 2(max 10 characters): ")
    if len(player2)>10:
        print("invalid name")
    if player2==player1:
        print("cannot be the same name")
    else:
        name2=False
while game:
    move1=(int(input(player1+' pick a row on the board to put an X(1-3): ')))
    x=move1-1
    move2=(int(input(player1+' pick a column on the board to put an X(1-3): ')))
    y=move2-1
    movetotal=board[x][y]
    if board[x][y]=='_':
        board[x][y]='X'
    else:
        print("INVALID MOVE, TURN SKIPPED")
    for i in range(n):
        for j in range(n):
            if board[i][j]!=movetotal:
                break
    print (board)   
    move3=(int(input(player2+' pick a row on the board to put an O(1-3): ')))
    z=move3-1
    move4=(int(input(player2+' pick a column on the board to put an O(1-3): ')))
    v=move4-1
    movetotal2=board[z][v]
    if board[z][v]!='X':
        board[z][v]=='O'
    else:
        print ("INVALID MOVE, TURN SKIPPED")
    for i in range(n):
        for j in range(n):
            if board[i][j]!=movetotal2:
                break
    print (board)
    