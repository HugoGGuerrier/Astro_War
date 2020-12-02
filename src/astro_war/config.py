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
