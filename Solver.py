from TicTacToe import *

class Solver():

	def __init__(self):
		self.memory = {}

	def resetMemory(self):
		self.memory.clear()

	def solveWeakWithoutMemory(self, game):
		primitive = game.primitive()
		if primitive != "Undecided":
			return primitive
		for move in game.generateMoves():
			newTicTacToe = game.doMove(move)
			if self.solve(newTicTacToe) == "Lose":
				return "Win" # Not necessarily traverse all subtree
		return "Lose"

	# this one will end when it finds the next instance as Win
	def solve(self, game):
		serialized = game.serialize()
		if serialized in self.memory:
			return self.memory[serialized]
		primitive = game.primitive()
		if primitive != "Undecided":
			self.memory[serialized] = primitive
			return primitive
		tieFlag = False
		for move in game.generateMoves():
			newTicTacToe = game.doMove(move)
			if self.solve(newTicTacToe) == "Lose":
				self.memory[serialized] = "Win"
				return "Win" # Not necessarily traverse all subtree
			if self.solve(newTicTacToe) == "Tie":
				tieFlag = True
		if tieFlag:
			self.memory[serialized] = "Tie"
			return "Tie"
		self.memory[serialized] = "Lose"
		return "Lose"

	# this one will traverse all subtree
	def solveTraverse(self, game):
		winFlag = False
		tieFlag = False
		serialized = game.serialize()

		if serialized in self.memory:
			return self.memory[serialized]
		primitive = game.primitive()

		if primitive != "Undecided":
			self.memory[serialized] = primitive
			return primitive

		for move in game.generateMoves():
			newTicTacToe = game.doMove(move)
			if self.solve(newTicTacToe) == "Lose":
				winFlag = True
			if self.solve(newTicTacToe) == "Tie":
				tieFlag = True

		if not winFlag: # There does not exist a losing child
			if tieFlag: # There exists a tie
				self.memory[serialized] = "Tie"
				return "Tie"
			else: # There is no tie
				self.memory[serialized] = "Lose"
				return "Lose"

		self.memory[serialized] = "Win"
		return "Win"

	def generateMove(self, game):
		tieMove = game.generateMoves()[0]
		for move in game.generateMoves():
			newGame = game.doMove(move)
			if self.memory[newGame.serialize()] == "Lose":
				return move
			if self.memory[newGame.serialize()] == "Tie":
				tieMove = move
		return tieMove

solver = Solver()
game = TicTacToe(3)
print(solver.solveTraverse(game))

memory = []
for game, value in solver.memory.items():
	memory.append((game, value))

#memory.sort(key=lambda item: int(item[0].split()[0]), reverse=True)
#for item in memory:
#	print(item[0], item[1])
