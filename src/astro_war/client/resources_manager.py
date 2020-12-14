from src.astro_war.config import Config
from src.astro_war.client.scaler import Scaler

import pyglet


class ResourcesManager:
    """
    This class contains all resources needed
    """

    # ----- Fonts -----

    MUNRO_FONT: str = "Munro"

    # ----- Images -----

    # --- Menu images

    HIBER_NATION_IMG: pyglet.image.AbstractImage = None
    SHIP_IMG: pyglet.image.AbstractImage = None
    MISSILE_IMG: pyglet.image.AbstractImage = None

    # ----- Sounds -----

    # --- Music

    MENU_MUSIC: pyglet.media.Source = None

    # ----- Loading methods -----

    @staticmethod
    def _load_font(file: str) -> None:
        """
        A short function to load a font file

        params :
            - file: str = The font file to load
        """

        pyglet.font.add_file(Config.RES_DIR + "font" + Config.FILE_SEPARATOR + file)
        pyglet.font.load("Munro")

    @staticmethod
    def _load_image(file: str) -> pyglet.image.AbstractImage:
        """
        A short function to load an image file

        params :
            - file: str = The image file to load

        return -> pygame.surface.Surface = The loaded image in a surface
        """

        return pyglet.image.load(Config.RES_DIR + "img" + Config.FILE_SEPARATOR + file)

    @staticmethod
    def _load_sound(file: str) -> pyglet.media.Source:
        """
        A short function to load an sound file

        params :
            - file: str = The sound file to load

        return -> pygame.mixer.Sound = The loaded sound
        """

        return pyglet.media.load(Config.RES_DIR + "sound" + Config.FILE_SEPARATOR + file)

    @staticmethod
    def load_all_resources():
        """
        Load all the resources
        """

        # Load the fonts
        ResourcesManager._load_font("Munro.ttf")

        # Load images
        ResourcesManager.HIBER_NATION_IMG = ResourcesManager._load_image("hiber_nation.png")
        ResourcesManager.SHIP_IMG = ResourcesManager._load_image("ship.png")
        ResourcesManager.MISSILE_IMG = ResourcesManager._load_image("missile.png")

        # Load sounds
        ResourcesManager.MENU_MUSIC = ResourcesManager._load_sound("menu.ogg")
