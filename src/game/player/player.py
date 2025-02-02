class Player:
    def __init__(self, name, board):
        self.name = name
        self.board = board

    def move(self, pos, pos_dest):
        print(f"moving {pos} to {pos_dest}")
        self.board.move(pos, pos_dest)

    def print_board(self):
        self.board.print()
