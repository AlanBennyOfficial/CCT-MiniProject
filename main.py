from flask import Flask, render_template, jsonify, request
from browser import document, alert

app = Flask(__name__)

currentPlayer = 'X'
board = [['', '', ''], ['', '', ''], ['', '', '']]
gameOver = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/make_move', methods=['POST'])
def make_move():
    global currentPlayer, board, gameOver
    if gameOver:
        return jsonify({'status': 'game over'})

    row = request.json['row']
    col = request.json['col']

    if board[row][col] != '':
        return jsonify({'status': 'cell already filled'})

    board[row][col] = currentPlayer

    if check_winner():
        highlight_winner()
        gameOver = True
        return jsonify({'status': 'win', 'winner': currentPlayer})

    currentPlayer = 'O' if currentPlayer == 'X' else 'X'
    return jsonify({'status': 'continue', 'currentPlayer': currentPlayer})

@app.route('/reset_game', methods=['POST'])
def reset_game():
    global currentPlayer, board, gameOver
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    gameOver = False
    currentPlayer = 'X'
    return jsonify({'status': 'reset'})

def check_winner():
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] and board[i][0] == board[i][1] == board[i][2]:
            return True
        if board[0][i] and board[0][i] == board[1][i] == board[2][i]:
            return True

    if board[0][0] and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

def highlight_winner():
    # Highlight the winning line by checking each possibility
    for i in range(3):
        if board[i][0] != '' and board[i][0] == board[i][1] == board[i][2]:
            document[f"cell-{i}-0"].classList.add('winner')
            document[f"cell-{i}-1"].classList.add('winner')
            document[f"cell-{i}-2"].classList.add('winner')
            return
        if board[0][i] != '' and board[0][i] == board[1][i] == board[2][i]:
            document[f"cell-0-{i}"].classList.add('winner')
            document[f"cell-1-{i}"].classList.add('winner')
            document[f"cell-2-{i}"].classList.add('winner')
            return
    if board[0][0] != '' and board[0][0] == board[1][1] == board[2][2]:
        document["cell-0-0"].classList.add('winner')
        document["cell-1-1"].classList.add('winner')
        document["cell-2-2"].classList.add('winner')
        return
    if board[0][2] != '' and board[0][2] == board[1][1] == board[2][0]:
        document["cell-0-2"].classList.add('winner')
        document["cell-1-1"].classList.add('winner')
        document["cell-2-0"].classList.add('winner')
        return

def main():
    for cell in document.select('.cell'):
        cell.bind("click", make_move)
    document.select_one("button").bind("click", reset_game)

main()

if __name__ == '__main__':
    app.run(debug=True)