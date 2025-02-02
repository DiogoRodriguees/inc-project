from .board.board import Board


class Game:
    def __init__(self):
        print("Starting game")

    def init(self):
        self.board = Board()
