from src.astro_war.save_manager import SaveManager
from src.astro_war.client import game

import os
import sys


# Start the game with the main function
if __name__ == '__main__':
    # Read the arguments to see if the user want the full game or just the server
    server_only: bool = False
    for arg in sys.argv:
        if arg == "--server":
            server_only = True

    # Bootstrap the application
    base_dir = os.path.abspath(".") + os.path.sep
    SaveManager.bootstrap(
        base_dir=base_dir,
        server_only=server_only
    )
    print("Application bootstrapped !")

    # Start the application
    app = game.Game()
    app.start_app()
