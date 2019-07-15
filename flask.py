from flask import Flask, Response, jsonify
from solver.TicTacToe.Tic import TicTacToe
from solver.GameManager import *
from solver.Solver import Solver

app = Flask(__name__)

@app.route('/tic/<num>')
def tic(num):
    game = TicTacToe(board=num)
    solver = Solver()
    if (len(num) != 9):
        return Response(status=404)
    print(game.toString())
    return jsonify({"move" : str(sum(solver.generateMove(game)))})
