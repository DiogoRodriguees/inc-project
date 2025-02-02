import os
from game.game import Game

import tkinter as tk
from tkinter import messagebox


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")  # Limpa o terminal


try:
    game = Game("Diogo", "Guest")

    while True:
        game.board.print()

        pos = (
            input("Digite a posição da peça que deseja mover (ou 'q' para sair): ")
            .strip()
            .lower()
        )
        pos_origin_dest = pos.split(" ")
        pos = pos_origin_dest[0]
        pos_dest = pos_origin_dest[1]
        clear_screen()

        try:
            game.move(pos, pos_dest)
        except Exception as e:
            print(e)

except Exception as e:
    print(f"Erro fatal: {e}")
