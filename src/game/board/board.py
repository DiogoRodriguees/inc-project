from .board_exceptions import (
    EmptyHouseError,
    OccupiedHouseError,
    InvalidHouseError,
)

from .board_house import House


class Board:
    white_house = "⬜"
    black_house = "🟫"

    white_piece = "🔴"
    black_piece = "⚫"

    def __init__(self):
        self.board = self.generate_board()

    def generate_board(self):
        board = list()
        for row in range(8):
            board_row = list()
            for col in range(8):
                position = f"{chr(ord('a') + col)}{row + 1}"
                color = self.black_house if (row + col) % 2 == 0 else self.white_house
                piece = None

                # Posicionamento inicial das peças
                if row < 3 and color == self.black_house:
                    piece = self.white_piece  # Peças brancas nas 3 primeiras linhas
                elif row > 4 and color == self.black_house:
                    piece = self.black_piece  # Peças pretas nas 3 últimas linhas

                board_row.append(House(position, color, piece))
            board.append(board_row)

        return board

    def print(self):
        print("  a  b  c  d  e  f  g  h")
        for i, row in enumerate(reversed(self.board), start=1):
            print(f"{9 - i} ", end="")
            for house in row:
                print(str(house), end=" ")
            print(f" {9 - i}")

        print("  a  b  c  d  e  f  g  h")

    def convert_position(self, position: str):
        letter, number = position[0], position[1]  # Separa os caracteres
        row = ord(letter) - ord("a") + 1  # Converte 'a' -> 1, 'b' -> 2, etc.
        col = int(number)  # Converte '1' -> 1, '2' -> 2, etc.
        return col - 1, row - 1

    def move(self, pos, pos_dest):
        pos_line, pos_col = self.convert_position(pos)
        pos_dest_line, pos_dest_col = self.convert_position(pos_dest)

        if self.board[pos_line][pos_col].piece is None:
            raise EmptyHouseError(pos)

        if self.board[pos_dest_line][pos_dest_col].piece is not None:
            raise OccupiedHouseError(pos_dest)

        if self.board[pos_dest_line][pos_dest_col].color != self.black_house:
            raise InvalidHouseError(pos_dest)

        # Move a peça
        self.board[pos_dest_line][pos_dest_col].piece = self.board[pos_line][
            pos_col
        ].piece
        self.board[pos_line][pos_col].piece = None
