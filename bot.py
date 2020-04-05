import numpy as np
from scipy.stats import logistic

from typing import List, Dict

from game import Move, GameState, move


class AI:
    """Representation of bot's state"""

    scores: Dict[GameState, float]
    current_game_states = []

    def choose_move(self, state: GameState) -> Move:
        self.current_game_states.append(state)
        moves = state.possible_moves()
        next_states = []
        for move in moves:
            next_states.append(move(state, move))

        probabilities = np.array(
            [logistic(self.scores[state]) for state in next_states]
        )
        probabilities /= np.sum(probabilities)
        return np.random.choice(moves, p=probabilities)

    def game_won(self):
        for state in self.current_game_states:
            self.scores[state] += 1
        self.current_game_states = []

    def game_loss(self):
        for state in self.current_game_states:
            self.scores[state] -= 1
        self.current_game_states = []

    def game_draw(self):
        for state in self.current_game_states:
            self.scores[state] -= 0.1
        self.current_game_states = []
