from browser import document, alert, window

currentPlayer = 'X'
board = [['', '', ''], ['', '', ''], ['', '', '']]
gameOver = False

# Global Tournament variables
winsX = 0
winsO = 0
gamesPlayed = 0

def update_scoreboard():
    # Update player names (without appending the score)
    document["scoreXName"].textContent = window.name1
    document["scoreOName"].textContent = window.name2
    # Update live score display in the scoreboard container
    document.select("span.score-home")[0].textContent = str(winsX)
    document.select("span.score-away")[0].textContent = str(winsO)

def make_move(ev):
    global currentPlayer, gameOver, winsX, winsO, gamesPlayed
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
        alert(f"{currentPlayer} wins this round!")
        if currentPlayer == 'X':
            winsX += 1
        else:
            winsO += 1
        gamesPlayed += 1
        update_scoreboard()
        if gamesPlayed >= window.totalGames:
            if winsX > winsO:
                alert(f"Tournament Over! {window.name1} wins the tournament!")
            elif winsO > winsX:
                alert(f"Tournament Over! {window.name2} wins the tournament!")
            else:
                alert("Tournament Over! It's a tie!")
            gameOver = True
        else:
            gameOver = True
            # Clear board for next round after 2 seconds delay
            window.setTimeout(reset_round, 2000)
        return

    currentPlayer = 'O' if currentPlayer == 'X' else 'X'

# New function to clear the board for the next round
def reset_round():
    global currentPlayer, board, gameOver
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    gameOver = False
    currentPlayer = 'X'
    for cell in document.select('.cell'):
        cell.html = ''
        cell.classList.remove('winner')

def reset_game(ev=None):  # Allow reset_game to be called without an event
    global currentPlayer, board, gameOver, winsX, winsO, gamesPlayed
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    gameOver = False
    currentPlayer = 'X'
    winsX = 0
    winsO = 0
    gamesPlayed = 0
    for cell in document.select('.cell'):
        cell.html = ''
        cell.classList.remove('winner')
    update_scoreboard()
    # Go back to setup screen
    document.getElementById("mainGameScreen").style.display = "none"
    document.getElementById("playerSetupScreen").style.display = "block"

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
            document[f"cell-{i}-0"].classList.add("winner")
            document[f"cell-{i}-1"].classList.add("winner")
            document[f"cell-{i}-2"].classList.add("winner")
            return
        if board[0][i] and board[0][i] == board[1][i] == board[2][i]:
            document[f"cell-0-{i}"].classList.add("winner")
            document[f"cell-1-{i}"].classList.add("winner")
            document[f"cell-2-{i}"].classList.add("winner")
            return
    if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
        document["cell-0-0"].classList.add("winner")
        document["cell-1-1"].classList.add("winner")
        document["cell-2-2"].classList.add("winner")
        return
    if board[0][2] and board[0][2] == board[1][1] == board[2][0]:
        document["cell-0-2"].classList.add("winner")
        document["cell-1-1"].classList.add("winner")
        document["cell-2-0"].classList.add("winner")
        return

def main():
    for cell in document.select('.cell'):
        cell.bind("click", make_move)
    # Bind reset using the button's id (ensure the reset button has id="resetBtn")
    document["resetBtn"].bind("click", reset_game)

main()

