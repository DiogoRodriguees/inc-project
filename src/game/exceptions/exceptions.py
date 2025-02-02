class InvalidMoveError(Exception):
    """Exceção base para movimentos inválidos."""

    pass


class EmptyHouseError(InvalidMoveError):
    """Exceção para quando a casa de origem não tem peça."""

    def __init__(self, position):
        super().__init__(f"A casa {position} não tem peça para mover.")


class OccupiedHouseError(InvalidMoveError):
    """Exceção para quando a casa de destino já tem uma peça."""

    def __init__(self, position):
        super().__init__(f"A casa {position} já possui uma peça.")


class InvalidHouseError(InvalidMoveError):
    """Exceção para quando a casa de destino não for preta."""

    def __init__(self, position):
        super().__init__(f"A casa {position} não é válida para movimentação.")
