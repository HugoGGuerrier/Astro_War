from src.astro_war import Config, utils

import os
import json


class Bootstrapper:
    """
    This class contains all methods to initialize the application client and server.
    """

    @staticmethod
    def save() -> None:
        """
        Save the current configuration in the save file
        """

        # Put the configuration in a dictionary
        save_dict: dict = {
            "SCREEN_SIZE": Config.SCREEN_SIZE,
            "FULL_SCREEN": Config.FULL_SCREEN,
            "V_SYNC": Config.V_SYNC,

            "FRAME_RATE": Config.FRAME_RATE,

            "USER_NAME": Config.USER_NAME
        }

        # Create a JSON string from the dictionary
        save_str = json.dumps(save_dict)

        # Write the JSON in the save file
        save_file = open(Config.SAVE_FILE, "w")
        save_file.write(utils.encrypt_save(save_str))
        save_file.close()

    @staticmethod
    def load() -> None:
        """
        Load the save file and set the configuration
        """

        # Get the decrypted save string
        save_file = open(Config.SAVE_FILE, "r")
        save_str: str = utils.decrypt_save(save_file.read())
        save_file.close()

        # Transform the save string into a dictionary
        save_dict: dict = json.loads(save_str)

        # Load the config from the dictionary
        Config.SCREEN_SIZE = save_dict["SCREEN_SIZE"]
        Config.FULL_SCREEN = save_dict["FULL_SCREEN"]
        Config.V_SYNC = save_dict["V_SYNC"]

        Config.FRAME_RATE = save_dict["FRAME_RATE"]

        Config.USER_NAME = save_dict["USER_NAME"]

    @staticmethod
    def load_default() -> None:
        """
        Load the default configuration when there is no save file
        """

        # Set the game settings
        Config.SCREEN_SIZE = [720, 480]
        Config.FULL_SCREEN = False
        Config.V_SYNC = False

        Config.FRAME_RATE = 60

        # Set the user settings
        Config.USER_NAME = "Looser"

    @staticmethod
    def bootstrap(base_dir: str, server_only: bool) -> None:
        """
        This method set all the application configuration

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

        if not os.path.isfile(Config.SAVE_FILE):
            # Create the save file if it doesn't exists and load the default config
            tmp = open(Config.SAVE_FILE, "w")
            tmp.close()
            Bootstrapper.load_default()
        else:
            # Load the configuration
            try:
                Bootstrapper.load()
            except json.decoder.JSONDecodeError as _:
                Bootstrapper.load_default()
