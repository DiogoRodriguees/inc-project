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
        # print(board[0][0].piece)
        return board

    def print(self):
        print("  a  b  c  d  e  f  g  h")
        for i, row in enumerate(reversed(self.board), start=1):
            print(f"{9 - i} ", end="")
            for house in row:
                print(str(house), end=" ")
            print(f" {9 - i}")

        print("  a  b  c  d  e  f  g  h")

    def move(self, pos, pos_dest):
        (pos_x, pos_y) = pos
        (dest_x, dest_y) = pos_dest
        pos_x = pos_x - 1
        dest_x = dest_x - 1
        pos_y = pos_y - 1
        dest_y = dest_y - 1
        # print(f"Moving {pos_x, pos_y} to {pos_y,dest_y}")
        if self.board[pos_x][pos_y].piece == None:
            raise EmptyHouseError(pos)

        # if self.board[dest_x][dest_y].piece is not None:
        #     raise OccupiedHouseError(pos_dest)

        if self.board[dest_x][dest_y].color != self.black_house:
            raise InvalidHouseError(pos_dest)

        # Move a peça
        self.board[dest_y][dest_x].piece = self.board[pos_y][pos_x].piece
        self.board[pos_y][pos_x].piece = None
