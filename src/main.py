from interface.interface import HandTracker
from game.game import Game
from game.game_with_interface import init_game
import threading

if __name__ == "__main__":
    stop_event = threading.Event()
    try:
        game_thread = threading.Thread(target=init_game)
        game_thread.start()
        HandTracker(Game("Guest1", "Guest2")).capture()
    except Exception as e:
        print(f"EXCEPT: {e}")
    finally:
        stop_event.set()
        stop_event.join()
        print("Finalizado corretamente")
