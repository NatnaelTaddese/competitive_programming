x = input()
y = input()
z = input()

board = [x,y,z]

individual_win = set()
group_win = set()


for i in range(3): 
    # checking rows and columns for individual wins
    if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
        individual_win.add(board[i][0])
    if  board[0][i] == board[1][i] and board[1][i] == board[2][i]:
        individual_win.add(board[0][i])
    
    # checking rows and columns for group wins
    row = set()
    [row.add(board[i][j]) for j in range(3)]
    row = list(row)

    if len(row) == 2:
        group = "".join(sorted(row[0] + row[1]))
        group_win.add(group)

    column = set()
    [column.add(board[j][i]) for j in range(3)]
    column = list(column)

    if len(column) == 2:
        group = "".join(sorted(column[0] + column[1]))
        group_win.add(group)

#checking diagonals for indiviual win
if  board[0][0] == board[1][1] and board[1][1] == board[2][2]:
    individual_win.add(board[0][0])
if  board[0][2] == board[1][1] and board[1][1] == board[2][0]:
    individual_win.add(board[0][2])

print(len(individual_win))

#checking the first diagonal for group win
diagonal = set()
[diagonal.add(board[i][i]) for i in range(3)]
diagonal = list(diagonal)

if len(diagonal) == 2:
    group = "".join(sorted(diagonal[0] + diagonal[1]))
    group_win.add(group)

#checking the reversed diagonal for group win
diagonal_rev = set()
[diagonal_rev.add(board[i][2-i]) for i in range(3)]
diagonal_rev = list(diagonal_rev)

if len(diagonal_rev) == 2:
    group = "".join(sorted(diagonal_rev[0] + diagonal_rev[1]))
    group_win.add(group)

print(len(group_win))