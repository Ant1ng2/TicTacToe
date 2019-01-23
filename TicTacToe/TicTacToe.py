from copy import copy, deepcopy
import sys
sys.path.append('..')

from Game import *
import Solver
from GameManager import *

class TicTacToe(Game):

    def __init__(self, size=3, board=None, turn="X", count=0):
        if board == None:
            self.board = []
            for i in range(size):
                self.board += [[" " for _ in range(size)]]
        else:
            self.board = board
        self.len = len(self.board)
        self.turn = turn
        self.count = count

    def addPiece(self, x, y):
        if self.getPiece(x, y) == " ":
            self.count += 1
            self.board[x][y] = self.turn
            if self.turn == "X":
                self.turn = "O"
            else:
                self.turn = "X"

    def getPiece(self, x, y):
        if x >= 0 and x < self.len and y >= 0 and y < self.len:
            return self.board[x][y]
        return " "

    def getTurn(self):
        return self.turn

    def getFirstPlayer(self):
        return "X"

    def getSecondPlayer(self):
        return "O"

    def generateMoves(self):
        moves = []

        for i in range(self.len * self.len):
            if self.getPiece(i % self.len, i // self.len) == " ":
                moves += [[i % self.len, i // self.len]]
        return moves

    def doMove(self, move):
        if self.count >= self.len * self.len:
            return self
        if move in self.generateMoves():
            game = TicTacToe(self.len, deepcopy(self.board), self.turn, self.count)
            game.addPiece(move[0], move[1])
        return game

    def primitive(self):
        for i in range(self.len * self.len):
            piece = self.getPiece(i % self.len, i // self.len)
            if piece != " ":
                for j in [(1, 0), (0, 1), (1, -1), (1, 1)]:
                    lineLen = 0
                    for k in range(-(self.len - 1), (self.len)):
                        if self.getPiece(i % self.len + k * j[0], i // self.len + k * j[1]) == piece:
                            lineLen += 1
                        else:
                            lineLen = 0
                        if lineLen >= self.len:
                            if piece != self.turn:
                                return Value.LOSE
                            if piece == self.turn:
                                return Value.WIN

        if self.count >= self.len * self.len:
            return Value.TIE
        else:
            return Value.UNDECIDED

    def toString(self):
        return self.serialize()

    def serialize(self):
        string = ""

        for i in range(self.len * self.len):
            if i % self.len == 0:
                string += "\n"
            string += self.getPiece(i % self.len, i // self.len)
        return string

    def moveFromInput(self, prompt):
        print(prompt)
        return [int(x.strip()) for x in input().split(',')]

game = TicTacToe(4)
solver = Solver.Solver()
gameManager = GameManager(game, solver)
gameManager.play()
