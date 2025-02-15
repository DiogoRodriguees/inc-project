from interface.interface import HandTracker
from game.game import Game

if __name__ == "__main__":
    HandTracker(Game("Guest1", "Guest2")).capture()
