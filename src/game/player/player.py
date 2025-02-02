class Player:
    def __init__(self, name, board, piece):
        self.name = name
        self.board = board
        self.piece_color = piece

    def move(self, pos, pos_dest):
        print(f"moving {pos} to {pos_dest}")
        self.board.move(pos, pos_dest)

    def print_board(self):
        self.board.print()
