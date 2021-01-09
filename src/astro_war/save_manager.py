from src.astro_war.config import Config
from src.astro_war import utils

import os
import json


class SaveManager:
    """
    This class contains all methods to initialize the application client and server.
    """

    @staticmethod
    def save() -> None:
        """
        Save the current configuration in the save file
        """

        # Put the configuration in a dictionary
        save_dict = Config.get_save_dict()

        # Create a JSON string from the dictionary
        save_str = json.dumps(save_dict)

        # Write the JSON in the save file
        save_file = open(Config.SAVE_FILE, "wb")
        save_file.write(utils.encrypt_save(save_str))
        save_file.close()

    @staticmethod
    def load() -> None:
        """
        Load the save file and set the configuration
        """

        # Get the decrypted save string
        save_file = open(Config.SAVE_FILE, "rb")
        save_str: str = utils.decrypt_save(save_file.read())
        save_file.close()

        # Transform the save string into a dictionary
        save_dict: dict = json.loads(save_str)

        # Load the config from the dictionary
        Config.set_save_dict(save_dict)

    @staticmethod
    def bootstrap(base_dir: str, server_only: bool) -> None:
        """
        This method set all the application configuration, it should be launch before the game start

        params :
            - base_dir: str = The directory that contains the main.py file
            - server_only: bool = If the user just want to start the server
        """

        # Test the base dir path and set it
        if os.path.isdir(base_dir):
            Config.BASE_DIR = base_dir
        else:
            raise NotADirectoryError(base_dir + " is not a directory. Base path is corrupted !")

        # Get the file separator
        Config.FILE_SEPARATOR = os.path.sep

        # Set the resources file path
        res_dir = Config.BASE_DIR + "res" + Config.FILE_SEPARATOR
        if os.path.isdir(res_dir):
            Config.RES_DIR = res_dir
        else:
            raise NotADirectoryError(res_dir + " is not a directory. Missing the resources !")

        # Set the running mode
        Config.SERVER_ONLY = server_only

        # Set the save file path
        Config.SAVE_FILE = Config.BASE_DIR + ".save"

        # Load the save file if it exists
        if os.path.isfile(Config.SAVE_FILE):
            try:
                SaveManager.load()
            except json.decoder.JSONDecodeError as _:
                print("The save file is corrupted !")
            except KeyError as _:
                print("Missing parts in the save file !")
