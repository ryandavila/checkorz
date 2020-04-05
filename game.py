import numpy as np


class Move:
    pass


class GameState:
    board: [[]]
    board_size: int
    p1_turn: bool

    def __init__(self, board_size: int=8):
      for i in range(board_size):
        for j in range(board / 2):
            board[i][j] = 0

        

    def __eq__(self):
        pass

    def __hash__(self):
        pass

    def possible_moves(self) -> Iterable[Move]:
        pass


def move(state: GameState, move: Move) -> GameState:
    pass
