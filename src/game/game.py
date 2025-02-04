from .board.board import Board
from .player.player import Player
from .board import board_exceptions


class Game:

    def __init__(self, player1_name, player2_name):
        self.board = Board()
        self.player1 = Player(player1_name, self.board, self.board.white_piece)
        self.player2 = Player(player2_name, self.board, self.board.black_piece)
        self.current_player = self.player1
        self.current_piece = self.player1.piece_color

    def moviment_is_valid(self):
        if self.current_player.piece_color != self.current_piece:
            raise board_exceptions.InvalidHouseError("")
        return  self

    def update_current_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
            self.current_piece = self.player2.piece_color
        else:
            self.current_player = self.player1
            self.current_piece = self.player1.piece_color

    def move(self, pos, dest):
        try:
            self.moviment_is_valid()
            self.board.move(pos, dest)
            self.update_current_player()
        except Exception as e:
            print(f"MOVE EXCEPTION: {e}")

    def hand_closed(self, pos, pos2):
        print(f"Mão fechou em ({pos},{pos2})")

    def hand_opened(self, pos, pos2):
        print(f"Mão abriu em ({pos},{pos2})")
