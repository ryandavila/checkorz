import numpy as np
from scipy.stats import logistic

from typing import List, Dict

from game import Move, GameState, move

class AI:
    """Representation of bot's state"""
    scores: Dict[GameState, float]
    current_game_states = []

    def choose_move(self, state: GameState) -> Move:
        current_game_states.append(state)
        moves = state.possible_moves()
        next_states = []
        for move in moves:
            next_states.add(move(state, move))

        probabilities = np.array([logistic(self.scores[state]) for state in next_states])
        probabilities /= np.sum(probabilities)
        return np.random.choice(moves, p=probabilities)

    def game_won():
        for state in current_game_states:
            scores[state] += 1
        current_game_states = []

    def game_loss():
        for state in current_game_states:
            scores[state] -= 1
        current_game_states = []

    def game_draw():
        for state in current_game_states:
            scores[state] -= 0.1
        current_game_states = []


