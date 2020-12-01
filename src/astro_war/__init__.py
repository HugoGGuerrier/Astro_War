class Config:
    """
    This class contains all the application configuration attributes
    """

    # Application constants
    APP_NAME = "Astro War"
    ICON_NAME = "Ast. W."

    # File management
    BASE_DIR: str = ""
    FILE_SEPARATOR: str = ""

    RES_DIR: str = ""
    SAVE_FILE: str = ""

    # Running mode
    SERVER_ONLY: bool = False

    # Game settings
    SCREEN_SIZE: list = [-1, -1]
    FULL_SCREEN: bool = False
    V_SYNC: bool = False

    FRAME_RATE = -1

    # User settings
    USER_NAME: str = ""
