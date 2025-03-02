from browser import document, alert

currentPlayer = 'X'
board = [['', '', ''], ['', '', ''], ['', '', '']]
gameOver = False

def make_move(ev):
    global currentPlayer, gameOver
    if gameOver:
        return
    cell = ev.target
    parts = cell.id.split('-')
    row = int(parts[1])
    col = int(parts[2])
    if board[row][col] != '':
        return
    board[row][col] = currentPlayer
    cell.html = currentPlayer

    if check_winner():
        highlight_winner()
        alert(f"{currentPlayer} Wins!")
        gameOver = True
        return

    currentPlayer = 'O' if currentPlayer == 'X' else 'X'

def reset_game(ev):
    global currentPlayer, board, gameOver
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    gameOver = False
    currentPlayer = 'X'
    for cell in document.select('.cell'):
        cell.html = ''
        cell.classList.remove('winner')

def check_winner():
    # Check rows and columns
    for i in range(3):
        if board[i][0] and board[i][0] == board[i][1] == board[i][2]:
            return True
        if board[0][i] and board[0][i] == board[1][i] == board[2][i]:
            return True
    # Check diagonals
    if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] and board[0][2] == board[1][1] == board[2][0]:
        return True
    return False

def highlight_winner():
    # Highlight the winning line by checking each possibility
    for i in range(3):
        if board[i][0] and board[i][0] == board[i][1] == board[i][2]:
            document[f"cell-{i}-0"].classList.add('winner')
            document[f"cell-{i}-1"].classList.add('winner')
            document[f"cell-{i}-2"].classList.add('winner')
            return
        if board[0][i] and board[0][i] == board[1][i] == board[2][i]:
            document[f"cell-0-{i}"].classList.add('winner')
            document[f"cell-1-{i}"].classList.add('winner')
            document[f"cell-2-{i}"].classList.add('winner')
            return
    if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
        document["cell-0-0"].classList.add('winner')
        document["cell-1-1"].classList.add('winner')
        document["cell-2-2"].classList.add('winner')
        return
    if board[0][2] and board[0][2] == board[1][1] == board[2][0]:
        document["cell-0-2"].classList.add('winner')
        document["cell-1-1"].classList.add('winner')
        document["cell-2-0"].classList.add('winner')
        return

def main():
    for cell in document.select('.cell'):
        cell.bind("click", make_move)
    document.select_one("button").bind("click", reset_game)

main()