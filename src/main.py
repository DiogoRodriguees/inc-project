from game.game import Game


try:
    game = Game("Diogo", "Guest")
    game.board.print()

    game.player1.move("a3", "b4")
    game.player1.move("b4", "a6")
    game.board.print()
except Exception as e:
    print(e)
