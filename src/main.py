from game.game import Game


try:
    game = Game("Diogo", "Guest")
    game.board.print()

    game.player1.move("a3", "b4")
    game.player1.move("b4", "a5")
    game.board.print()
    game.player1.print_board()
    game.player2.print_board()
except Exception as e:
    print(e)
