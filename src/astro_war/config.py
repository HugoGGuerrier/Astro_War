class Config:
    """
    This class contains all the application configuration attributes
    """

    # Application constants
    APP_NAME: str = "Astro War"
    ICON_NAME: str = "Ast. W."

    BASE_ZOOM: float = 2.0

    # File management
    BASE_DIR: str = ""
    FILE_SEPARATOR: str = ""

    RES_DIR: str = ""
    SAVE_FILE: str = ""

    # Running mode
    SERVER_ONLY: bool = False

    # Game settings
    SCREEN_SIZE: list = [720, 480]
    FULL_SCREEN: bool = False
    V_SYNC: bool = False

    FRAME_RATE = 60

    MUSIC_VOLUME: float = 1.0
    SOUND_VOLUME: float = 1.0

    # User settings
    USER_NAME: str = "Looser"

    # ----- Getting methods -----

    @staticmethod
    def get_save_dict() -> dict:
        """
        Get the dictionary to save it into a file
        """

        return {
            "SCREEN_SIZE": Config.SCREEN_SIZE,
            "FULL_SCREEN": Config.FULL_SCREEN,
            "V_SYNC": Config.V_SYNC,

            "FRAME_RATE": Config.FRAME_RATE,

            "MUSIC_VOLUME": Config.MUSIC_VOLUME,
            "SOUND_VOLUME": Config.SOUND_VOLUME,

            "USER_NAME": Config.USER_NAME
        }

    @staticmethod
    def set_save_dict(save_dict: dict) -> None:
        """
        Set the configuration from a save dictionary

        params :
            - save_dict: dict = The save dictionary
        """

        Config.SCREEN_SIZE = save_dict.get("SCREEN_SIZE", [720, 480])
        Config.FULL_SCREEN = save_dict.get("FULL_SCREEN", False)
        Config.V_SYNC = save_dict.get("V_SYNC", False)

        Config.FRAME_RATE = save_dict.get("FRAME_RATE", 60)

        Config.MUSIC_VOLUME = save_dict.get("MUSIC_VOLUME", 1.0)
        Config.SOUND_VOLUME = save_dict.get("SOUND_VOLUME", 1.0)

        Config.USER_NAME = save_dict.get("USER_NAME", "Looser")

    # ----- Config changing methods -----
