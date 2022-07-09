from algorithms import MonteCarlo
from board import Game as TicTacToe


class Game:
	def __init__(self):
		self.tree = MonteCarlo()
		self.board = TicTacToe()

	def start(self):
		print(TicTacToe.compile(self.board))
		while True:
			self.board = self.board.make_move(self.board, self.get_player_move())
			print("\n" + TicTacToe.compile(self.board))
			if self.board.terminal:
				break
			self.board = self.get_monte_carlo_move()
			print("\n" + TicTacToe.compile(self.board))
			if self.board.terminal:
				break

		print()
		if TicTacToe.has_player_won(self.board.position) is not None:
			print(("O", "X")[TicTacToe.has_player_won(self.board.position)] + " won!")
		else:
			print("Tie game!")

	def get_player_move(self):
		move = input("Enter the row and column number: ")
		if ", " in move:
			row, col = map(int, move.split(", "))
		elif "," in move:
			row, col = map(int, move.split(","))
		else:
			def get_column():
				column = input("Enter the column number: ")
				if column.isnumeric():
					return int(column)
				print("Invalid input")
				return get_column()
			row, col = int(move), get_column()
		index = 3 * (row - 1) + (col - 1)
		if self.board.position[index] is not None:
			print("Invalid move")
			return self.get_player_move()
		return index

	def get_monte_carlo_move(self):
		for _ in range(5000):
			self.tree.rollout(self.board)
		return self.tree.choose(self.board)


if __name__ == "__main__":
	game = Game()
	game.start()
