from TicTacToe import *
import Solver

class GameManger:

    def __init__(self, game, solver=None):
        self.game = game
        self.solver = solver
        if solver:
            self.solver.solveTraverse(self.game)

    def play(self):
        while self.game.primitive() == "Undecided":
            print("Solver: " + self.solver.solve(self.game))
            print("Primitive: " + self.game.primitive())
            print(self.game.getTurn(), "'s turn")
            print(self.game.serialize())
            if self.game.getTurn() == "X" or not self.solver:
                print("Enter Piece: ")
                move = [int(x.strip()) for x in input().split(',')]
                if move not in self.game.generateMoves():
                    print("Not a valid move, try again")
                else:
                    self.game = self.game.doMove(move)
            else:
                self.game = self.game.doMove(self.solver.generateMove(self.game))
            print("----------------------------")
        print("Solver: " + self.solver.solve(self.game))
        print("Primitive: " + self.game.primitive())
        print(self.game.serialize())
        print("Game Over")

game = TicTacToe()
solver = Solver.Solver()
gameManager = GameManger(game, solver)
gameManager.play()
