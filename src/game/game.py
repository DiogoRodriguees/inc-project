from .board.board import Board
from .player.player import Player
from .board import board_exceptions


class Game:
    @staticmethod
    def get_position(pos):
        col = ["a", "b", "c", "d", "e", "f", "g", "h"]
        x, y = pos
        return f"{col[x -1]}{y}"

    def __init__(self, player1_name, player2_name):
        self.board = Board()
        self.player1 = Player(player1_name, self.board, self.board.white_piece)
        self.player2 = Player(player2_name, self.board, self.board.black_piece)
        self.current_player = self.player1
        self.current_piece = self.player1.piece_color
        self.hand_closed_in = None
        self.hand_open_in = None

    def moviment_is_valid(self):
        if self.current_player.piece_color != self.current_piece:
            raise board_exceptions.InvalidHouseError("")
        return self

    def update_current_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
            self.current_piece = self.player2.piece_color
        else:
            self.current_player = self.player1
            self.current_piece = self.player1.piece_color

    def move(self, pos, dest):
        try:
            # self.moviment_is_valid()
            self.board.move(pos, dest)
            self.update_current_player()
        except Exception as e:
            print(f"MOVE EXCEPTION: {e}")

    def hand_closed(self, pos_y, pos_x):
        self.hand_closed_in = (pos_x, pos_y)
        print(f"Mão fechou em {Game.get_position(self.hand_closed_in)}")

    def hand_opened(self, pos_y, pos_x):
        self.hand_open_in = (pos_x, pos_y)
        print(f"Mão abriu em {Game.get_position(self.hand_open_in)}")

        if self.hand_open_in != None:
            print(
                f"Moving piece from {Game.get_position(self.hand_closed_in)} to {Game.get_position(self.hand_open_in)}"
            )
            self.move(self.hand_closed_in, self.hand_open_in)
