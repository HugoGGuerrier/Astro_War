from src.astro_war.client.states.base_state import BaseState
from src.astro_war.client.states.menu import Menu
from src.astro_war.config import Config
from src.astro_war.client.resources_manager import ResourcesManager
from src.astro_war.client.sound_player import SoundPlayer
from src.astro_war.client.timeline import Timeline


class SplashScreen(BaseState):
    """
    The splash screen game state
    """

    # ----- Constructor ------

    def __init__(self, game):
        super().__init__("SplashScreen", game)

        # Get the state resources
        self._splash_image = ResourcesManager.HIBER_NATION_IMG
        self._menu_music = ResourcesManager.MENU_MUSIC

        # Define the state variables
        self._image_pos = (0, 0)

        # Define the image animation
        self._image_animation: Timeline = Timeline(3500)
        self._image_animation.set_initial_value(0)
        self._image_animation.set_coef(255)
        self._image_animation.set_loop(False)
        self._image_animation.set_update_callback(self._splash_image.set_alpha)
        self._image_animation.set_end_callback(self.animation_end)
        self._image_animation.add_time_point(750, 1)
        self._image_animation.add_time_point(2250, 1)
        self._image_animation.add_time_point(3000, 0)

    # ----- Class methods -----

    def animation_end(self):
        """
        Function to call when the animation is finished and you want to go to the next state
        """

        self._game.set_state(Menu(self._game))

    # ----- State necessary methods -----

    def enter(self):
        # Play the menu music
        SoundPlayer.play_music(self._menu_music)

        # Reset the animation
        self._image_animation.reset()

    def init(self):
        # Compute the image position
        self._image_pos = (
            (Config.SCREEN_SIZE[0] / 2) - (self._splash_image.get_width() / 2),
            (Config.SCREEN_SIZE[1] / 2) - (self._splash_image.get_height() / 2)
        )

        # Start the animation
        self._image_animation.start()

    def update(self, dt: int) -> None:
        self._image_animation.update(dt)
        pass

    def render(self) -> None:
        self._surface.blit(self._splash_image, self._image_pos)
        pass
