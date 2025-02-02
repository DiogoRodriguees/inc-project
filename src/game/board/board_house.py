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
