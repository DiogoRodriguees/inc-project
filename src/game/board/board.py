from ..exceptions.exceptions import (
    EmptyHouseError,
    OccupiedHouseError,
    InvalidHouseError,
)


class House:
    def __init__(self, pos, color, piece=None):
        self.color = color
        self.pos = pos
        self.piece = piece

    def __str__(self):
        if self.piece:
            return self.piece
        return self.color  # Representação visual da casa branca
        # return "white"  # Representação visual da casa branca


class Board:

    def __init__(self):
        print("Starting board")
        self.board = [
            [
                House("a1", "⬛", "⚫"),
                House("a2", "⬜"),
                House("a3", "⬛", "⚫"),
                House("a4", "⬜"),
                House("a5", "⬛", "⚫"),
                House("a6", "⬜"),
                House("a7", "⬛", "⚫"),
                House("a8", "⬜"),
            ],
            [
                House("b1", "⬜"),
                House("b2", "⬛", "⚫"),
                House("b3", "⬜"),
                House("b4", "⬛", "⚫"),
                House("b5", "⬜"),
                House("b6", "⬛", "⚫"),
                House("b7", "⬜"),
                House("b8", "⬛", "⚫"),
            ],
            [
                House("c1", "⬛", "⚫"),
                House("c2", "⬜"),
                House("c3", "⬛", "⚫"),
                House("c4", "⬜"),
                House("c5", "⬛", "⚫"),
                House("c6", "⬜"),
                House("c7", "⬛", "⚫"),
                House("c8", "⬜"),
            ],
            [
                House("d1", "⬜"),
                House("d2", "⬛"),
                House("d3", "⬜"),
                House("d4", "⬛"),
                House("d5", "⬜"),
                House("d6", "⬛"),
                House("d7", "⬜"),
                House("d8", "⬛"),
            ],
            [
                House("e1", "⬛"),
                House("e2", "⬜"),
                House("e3", "⬛"),
                House("e4", "⬜"),
                House("e5", "⬛"),
                House("e6", "⬜"),
                House("e7", "⬛"),
                House("e8", "⬜"),
            ],
            [
                House("f1", "⬜"),
                House("f2", "⬛", "⚪"),
                House("f3", "⬜"),
                House("f4", "⬛", "⚪"),
                House("f5", "⬜"),
                House("f6", "⬛", "⚪"),
                House("f7", "⬜"),
                House("f8", "⬛", "⚪"),
            ],
            [
                House("g1", "⬛", "⚪"),
                House("g2", "⬜"),
                House("g3", "⬛", "⚪"),
                House("g4", "⬜"),
                House("g5", "⬛", "⚪"),
                House("g6", "⬜"),
                House("g7", "⬛", "⚪"),
                House("g8", "⬜"),
            ],
            [
                House("h1", "⬜"),
                House("h2", "⬛", "⚪"),
                House("h3", "⬜"),
                House("h4", "⬛", "⚪"),
                House("h5", "⬜"),
                House("h6", "⬛", "⚪"),
                House("h7", "⬜"),
                House("h8", "⬛", "⚪"),
            ],
        ]

    def print(self):
        print("  a b c d e f g h")  # Cabeçalho com letras das colunas
        for i, row in enumerate(
            reversed(self.board), start=1
        ):  # Inverte a ordem das linhas
            print(f"{9 - i} ", end="")  # Ajusta a numeração correta
            for house in row:
                print(str(house), end=" ")
            print(f" {9 - i}")  # Número da linha no final

        print("  a b c d e f g h")  # Rodapé com letras das colunas

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

        if self.board[pos_dest_line][pos_dest_col].color != "⬛":
            raise InvalidHouseError(pos_dest)

        # Move a peça
        self.board[pos_dest_line][pos_dest_col].piece = self.board[pos_line][
            pos_col
        ].piece
        self.board[pos_line][pos_col].piece = None
