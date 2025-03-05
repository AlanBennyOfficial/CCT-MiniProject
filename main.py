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

'''
from browser import document, alert

# Tournament variables
playerXName = "Player X"
playerOName = "Player O"
winsX = 0
winsO = 0
maxGames = 1

# Game variables
currentPlayer = 'X'
board = [['', '', ''], ['', '', ''], ['', '', '']]
gameOver = False

def updateScoreboard():
    scoreboard = document["scoreboard"]
    scoreboard.textContent = f"{playerXName}: {winsX} wins | {playerOName}: {winsO} wins"

def startGame(ev):
    global playerXName, playerOName, maxGames, winsX, winsO
    ev.preventDefault()
    # Get player names and number of games; fallback to defaults if empty
    playerXName = document["playerX"].value.strip() or "Player X"
    playerOName = document["playerO"].value.strip() or "Player O"
    try:
        maxGames = int(document["maxGames"].value)
    except ValueError:
        maxGames = 1
    winsX = 0
    winsO = 0
    updateScoreboard()
    # Hide setup form so players cannot change mid-tournament
    document["setup"].style.display = "none"
    reset_board()

def reset_board():
    global currentPlayer, board, gameOver
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    gameOver = False
    currentPlayer = 'X'
    for cell in document.select('.cell'):
        cell.html = ''
        cell.classList.remove('winner')

def make_move(ev):
    global currentPlayer, gameOver, winsX, winsO
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
        if currentPlayer == 'X':
            winsX += 1
        else:
            winsO += 1
        updateScoreboard()
        alert(f"{currentPlayer} Wins!")
        gameOver = True
        # Check if tournament is over
        if (winsX + winsO) >= maxGames:
            alert(f"Tournament over!\nFinal Score:\n{playerXName}: {winsX}\n{playerOName}: {winsO}")
        return

    currentPlayer = 'O' if currentPlayer == 'X' else 'X'

def reset_game(ev):
    reset_board()
    # Allow play only if tournament is not over
    if (winsX + winsO) >= maxGames:
        alert("Tournament already ended!")
    
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
            document[f"cell-from browser import document, alert

# Tournament variables
playerXName = "Player X"
playerOName = "Player O"
winsX = 0
winsO = 0
maxGames = 1

# Game variables
currentPlayer = 'X'
board = [['', '', ''], ['', '', ''], ['', '', '']]
gameOver = False

def updateScoreboard():
    scoreboard = document["scoreboard"]
    scoreboard.textContent = f"{playerXName}: {winsX} wins | {playerOName}: {winsO} wins"

def startGame(ev):
    global playerXName, playerOName, maxGames, winsX, winsO
    ev.preventDefault()
    # Get player names and number of games; fallback to defaults if empty
    playerXName = document["playerX"].value.strip() or "Player X"
    playerOName = document["playerO"].value.strip() or "Player O"
    try:
        maxGames = int(document["maxGames"].value)
    except ValueError:
        maxGames = 1
    winsX = 0
    winsO = 0
    updateScoreboard()
    # Hide setup form so players cannot change mid-tournament
    document["setup"].style.display = "none"
    reset_board()

def reset_board():
    global currentPlayer, board, gameOver
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    gameOver = False
    currentPlayer = 'X'
    for cell in document.select('.cell'):
        cell.html = ''
        cell.classList.remove('winner')

def make_move(ev):
    global currentPlayer, gameOver, winsX, winsO
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
        if currentPlayer == 'X':
            winsX += 1
        else:
            winsO += 1
        updateScoreboard()
        alert(f"{currentPlayer} Wins!")
        gameOver = True
        # Check if tournament is over
        if (winsX + winsO) >= maxGames:
            alert(f"Tournament over!\nFinal Score:\n{playerXName}: {winsX}\n{playerOName}: {winsO}")
        return

    currentPlayer = 'O' if currentPlayer == 'X' else 'X'

def reset_game(ev):
    reset_board()
    # Allow play only if tournament is not over
    if (winsX + winsO) >= maxGames:
        alert("Tournament already ended!")
    
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
            document[f"cell-
'''