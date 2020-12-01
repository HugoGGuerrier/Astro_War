from src.astro_war import Config

import pygame


class ResourcesManager:
    """
    This class contains all resources needed in the game
    """

    # ----- Fonts -----

    @staticmethod
    def MUNRO_FONT(size):
        return ResourcesManager._load_font("Munro.ttf", size)

    # ----- Images -----

    # --- Menu images

    HIBER_NATION_IMG: pygame.surface.Surface = None

    # ----- Sounds -----

    # --- Music

    MENU_MUSIC: pygame.mixer.Sound = None

    # ----- Loading methods -----

    @staticmethod
    def _load_font(file: str, size: int) -> pygame.font.Font:
        """
        A short function to load a font file

        params :
            - file: str = The font file to load

        return -> pygame.font.Font = The loaded font
        """

        return pygame.font.Font(Config.RES_DIR + "font" + Config.FILE_SEPARATOR + file, size)

    @staticmethod
    def _load_image(file: str) -> pygame.surface.Surface:
        """
        A short function to load an image file

        params :
            - file: str = The image file to load

        return -> pygame.surface.Surface = The loaded image in a surface
        """

        return pygame.image.load(Config.RES_DIR + "img" + Config.FILE_SEPARATOR + file)

    @staticmethod
    def _load_sound(file: str) -> pygame.mixer.Sound:
        """
        A short function to load an sound file

        params :
            - file: str = The sound file to load

        return -> pygame.mixer.Sound = The loaded sound
        """

        return pygame.mixer.Sound(Config.RES_DIR + "sound" + Config.FILE_SEPARATOR + file)

    @staticmethod
    def load():
        """
        Load all the resources
        """

        # Load images
        ResourcesManager.HIBER_NATION_IMG = ResourcesManager._load_image("hiber_nation.png")

        # Load sounds
        ResourcesManager.MENU_MUSIC = ResourcesManager._load_sound("menu.ogg")
