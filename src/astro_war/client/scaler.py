from src.astro_war.config import Config

import pygame


class Scaler:
    """
    This class is here to help the developer to scale images and distances
    """

    _base_width: int = 720
    _base_height: int = 480

    @staticmethod
    def scale_length(length: int) -> int:
        """
        Scale the given length

        params :
            - length: int = The length to scale

        return -> int = The scaled length
        """

        return round((length / Scaler._base_height) * Config.SCREEN_SIZE[1])

    @staticmethod
    def scale_image(image: pygame.surface.Surface) -> pygame.surface.Surface:
        """
        Scale an image to fit the screen

        params :
            - image: pygame.surface.Surface = The image to scale
        """

        scale_coef = (Config.SCREEN_SIZE[1] / Scaler._base_height) * Config.BASE_ZOOM
        new_size = (
            round(image.get_width() * scale_coef),
            round(image.get_height() * scale_coef)
        )
        return pygame.transform.scale(image, new_size)
