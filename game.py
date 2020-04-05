import numpy as np


class Move:
    current_position: ()
    new_position: ()
    player: str

    def __init__(self, current_position, new_position, player):
        self.current_position = current_position
        self.new_position = new_position
        self.player = player


class GameState:
    """Representation of the game board and current state"""

    starting_positions = set(
        (0, 0),
        (0, 2),
        (0, 4),
        (0, 6),
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (7, 0),
        (7, 2),
        (7, 4),
        (7, 6),
        (6, 1),
        (6, 3),
        (6, 5),
        (6, 7),
    )
    board: {}
    board_size: int
    p1_turn: bool

    def __init__(self, board_size: int = 8):
        self.board_size = board_size
        for row in range(board_size):
            for column in range(board_size):
                if (row, column) in self.starting_positions:
                    self.board[(row, column)] = 1
                else:
                    self.board[(row, column)] = 0
        self.p1_turn = True

    def __eq__(self, obj):
        pass

    def __hash__(self):
        pass

    def possible_moves(self) -> Iterable[Move]:
        possible_moves = []
        for point in self.board.values():
            for possible_move in self._get_diagonal_positions(point):
                if is_valid_move(point, possible_move, self.board):
                    possible_moves.append(
                        Move(point, possible_move, "p1" if self.p1_turn else "p2")
                    )
        return possible_moves

    def _get_diagonal_positions(self, position):
        return set(
            (position[0] + 1, position[1] + 1),
            (position[0] - 1, position[1] - 1),
            (position[0] + 1, position[1] - 1),
            (position[0] - 1, position[1] + 1),
        )


def is_valid_move(current_position, new_position, board) -> bool:
    if abs(current_position[0] - new_position[0]) == abs(
        current_position[1] - new_position[1]
    ):
        if board[new_position] != 1:
            return True
    return False


def move(state: GameState, move: Move) -> GameState:
    pass
