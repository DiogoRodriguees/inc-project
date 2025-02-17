class Game:
    @staticmethod
    def get_position(pos):
        col = ["a", "b", "c", "d", "e", "f", "g", "h"]
        x, y = pos
        return f"{col[x -1 ]}{y}"


class InvalidMoveError(Exception):
    """Exceção base para movimentos inválidos."""

    pass


class EmptyHouseError(InvalidMoveError):
    """Exceção para quando a casa de origem não tem peça."""

    def __init__(self, position):
        super().__init__(
            f"A casa {Game.get_position(position)} não tem peça para mover."
        )


class OccupiedHouseError(InvalidMoveError):
    """Exceção para quando a casa de destino já tem uma peça."""

    def __init__(self, position):
        super().__init__(f"A casa {Game.get_position(position)} já possui uma peça.")


class AwaitYourTime(InvalidMoveError):
    """Exceção para quando não for a vez do jogador."""

    def __init__(self, position):
        super().__init__(f"É a vez do outro jogador")


class InvalidHouseError(InvalidMoveError):
    """Exceção para quando a casa de destino não for preta."""

    def __init__(self, position):
        super().__init__(
            f"A casa {Game.get_position(position)} não é válida para movimentação. Apenas casas escuras devem ser usadas"
        )
