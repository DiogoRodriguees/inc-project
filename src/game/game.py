from .board.board import Board
from .player.player import Player


class Game:

    def __init__(self, player1_name, player2_name):
        print("Starting game")
        self.board = Board()
        self.player1 = Player(player1_name, self.board)
        self.player2 = Player(player2_name, self.board)
