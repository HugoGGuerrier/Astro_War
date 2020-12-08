from src.astro_war.client.states.base_state import BaseState
from src.astro_war.client.states.main_menu import MainMenu
from src.astro_war.client.resources_manager import ResourcesManager
from src.astro_war.client.scaler import Scaler
from src.astro_war.client.sound_player import SoundPlayer
from src.astro_war.client.timeline import Timeline

import pyglet

from src.astro_war.models import Ship


class TestFlo(BaseState):
    """
    The splash screen game state
    """

    # ----- Constructor ------

    def __init__(self, game):
        super().__init__("Test Flo", game)

        # Get the state resources
        self._menu_music = ResourcesManager.MENU_MUSIC

        self._ship_image = pyglet.sprite.Sprite(ResourcesManager.SHIP_IMG)
        self._ship_image.image.anchor_x = self._ship_image.width/2
        self._ship_image.image.anchor_y = self._ship_image.height/2


       #65362 self._missile_image.image.anchor_x = self._missile_image.width / 2
       # self._missile_image.image.anchor_y = self._missile_image.height / 2


        self.shade = True
        self.pressed_buttons = []

        self.my_ship = Ship("blue", self._ship_image)

    # ----- Class methods -----


    # ----- State necessary methods -----

    def enter(self, args) -> None:
        # Play the menu music
        SoundPlayer.play_music(self._menu_music)

        # Scale the image
        Scaler.scale_sprite(self._ship_image)

        # Compute the image position
        self._ship_image.x = self._game.width // 2 - self._ship_image.width // 2
        self._ship_image.y = self._game.height // 2 - self._ship_image.height // 2



    def update(self, dt: int) -> None:
        # Update the image opacity
        if self.shade :
            self._ship_image.opacity -=1
        else:
            self._ship_image.opacity +=1

        if self._ship_image.opacity < 170:
            self.shade = False
        elif self._ship_image.opacity >253:
            self.shade = True

        if 65361 in self.pressed_buttons:
            self.my_ship.rotateLeft()
        if 65363 in self.pressed_buttons:
            self.my_ship.rotateRight()
        if 32 in self.pressed_buttons:
            self.my_ship.shoot()
            self.pressed_buttons.remove(32)

        self.my_ship.fly()
        for i in self.my_ship.missile:
            i.fly()

    def render(self) -> None:
        # Render the image
        self.my_ship.sprite.draw()
        for i in self.my_ship.missile:
            i.sprite.draw()
