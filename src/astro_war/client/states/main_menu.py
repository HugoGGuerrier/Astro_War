from src.astro_war.config import Config
from src.astro_war.client.scaler import Scaler
from src.astro_war.client.resources_manager import ResourcesManager
from src.astro_war.client.states.base_state import BaseState

import pyglet


class MainMenu(BaseState):
    """
    This class is the main menu of the game
    """

    # ----- Constructor -----

    def __init__(self, game):
        super().__init__("Main Menu", game)

        # Create the groups and batches
        self._batch: pyglet.graphics.Batch = pyglet.graphics.Batch()
        self._bg_group: pyglet.graphics.OrderedGroup = pyglet.graphics.OrderedGroup(0)
        self._fg_group: pyglet.graphics.OrderedGroup = pyglet.graphics.OrderedGroup(1)
        self._ui_group: pyglet.graphics.OrderedGroup = pyglet.graphics.OrderedGroup(2)

        # Get all the state resources

        # Create main menu buttons

    # ----- State necessary methods -----

    def enter(self):
        # Compute the button position and size

        # Create the gui elements

        # Set the buttons style
        pass

    def init(self):
        pass

    def exit(self):
        pass

    def handle(self, event) -> None:
        # Handle buttons event
        pass

    def update(self, dt: int) -> None:
        # Update the ui manager
        pass

    def render(self) -> None:
        # Render the gui
        pass
