from src.astro_war.client.states.base_state import BaseState
from src.astro_war.client.states.main_menu import MainMenu
from src.astro_war.client.resources_manager import ResourcesManager
from src.astro_war.client.scaler import Scaler
from src.astro_war.client.sound_player import SoundPlayer
from src.astro_war.client.timeline import Timeline

import pyglet


class SplashScreen(BaseState):
    """
    The splash screen game state
    """

    # ----- Constructor ------

    def __init__(self, game):
        super().__init__("SplashScreen", game)

        # Get the state resources
        self._splash_image = pyglet.sprite.Sprite(ResourcesManager.HIBER_NATION_IMG)
        self._menu_music = ResourcesManager.MENU_MUSIC

        # Define the state variables
        self._image_pos = (0, 0)

        # Define the image animation
        self._image_animation: Timeline = Timeline(4)
        self._image_animation.set_initial_value(0)
        self._image_animation.set_loop(False)
        self._image_animation.add_time_point(0.5, 0)
        self._image_animation.add_time_point(1.25, 1)
        self._image_animation.add_time_point(2.75, 1)
        self._image_animation.add_time_point(3.5, 0)
        self._image_animation.set_end_callback(None)

    # ----- Class methods -----

    def animation_end(self):
        """
        Function to call when the animation is finished and you want to go to the next state
        """

        self._game.set_state(MainMenu(self._game))

    # ----- State necessary methods -----

    def enter(self) -> None:
        # Play the menu music
        SoundPlayer.play_music(self._menu_music)

        # Scale the image
        Scaler.scale_sprite(self._splash_image)

        # Compute the image position
        self._splash_image.x = self._game.width // 2 - self._splash_image.width // 2
        self._splash_image.y = self._game.height // 2 - self._splash_image.height // 2

        # Start the animation
        self._image_animation.start()

    def exit(self) -> None:
        # Reset the animation
        self._image_animation.reset()

    def update(self, dt: int) -> None:
        # Update the animation
        self._image_animation.update(dt)

        # Update the image opacity
        self._splash_image.opacity = self._image_animation.get_value() * 255

    def render(self) -> None:
        # Render the image
        self._splash_image.draw()
