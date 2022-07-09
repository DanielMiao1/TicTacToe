"""
Main board/game logic
"""


class Game:
	def __init__(self, position=(None,) * 9, turn=True, winner=None, terminal=False):
		self.position, self.turn, self.winner, self.terminal = position, turn, winner, terminal

	@staticmethod
	def has_player_won(position):
		# re-arrange board into 2d list of rows
		rows = [[]]
		for i in position:
			if len(rows[-1]) == 3:
				rows.append([i])
			else:
				rows[-1].append(i)

		# diagonal wins
		if rows[0][0] == rows[1][1] == rows[2][2] and rows[0][0] is not None:
			return rows[0][0]
		elif rows[0][2] == rows[1][1] == rows[2][0] and rows[0][2] is not None:
			return rows[0][2]
		# horizontal win
		for i in range(3):
			if rows[i][0] == rows[i][1] == rows[i][2] and rows[i][0] is not None:
				return rows[i][0]
		# vertical win
		for i in range(3):
			if rows[0][i] == rows[1][i] == rows[2][i] and rows[0][i] is not None:
				return rows[0][i]
		return None

	@staticmethod
	def make_move(board, index):
		position = board.position[:index] + (board.turn,) + board.position[index + 1:]
		turn = not board.turn
		winner = Game.has_player_won(position)
		is_terminal = (winner is not None) or not any(v is None for v in position)
		return Game(position, turn, winner, is_terminal)

	@staticmethod
	def compile(board):
		rows = [[]]
		for i in board.position:
			if len(rows[-1]) == 3:
				rows.append([(lambda x: {None: " ", True: "X", False: "O"}[x])(i)])
			else:
				rows[-1].append((lambda x: {None: " ", True: "X", False: "O"}[x])(i))
		return "\n--+---+--\n".join([" | ".join(i) for i in rows])
