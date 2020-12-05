from src.astro_war.config import Config
from src.astro_war.client.scaler import Scaler
from src.astro_war.client.resources_manager import ResourcesManager
from src.astro_war.client.states.base_state import BaseState

from src import pyglet_gui
import pyglet


class MainMenuButton(pyglet_gui.Button):
    """
    This class is the default main menu button, only customisable with the y and text
    """

    def __init__(self, text, y):
        super().__init__(
            text=text,
            x=0,
            y=y,
            width=Scaler.scale_length(200),
            height=Scaler.scale_length(50),
            color=(255, 0, 174, 60),
            font_name="Munro",
            font_size=Scaler.scale_length(20),
            lab_color=(255, 255, 255, 255),
            border_color=(255, 255, 255, 255),
            border_width=Scaler.scale_length(2),
            border_padding=Scaler.scale_length(5)
        )
        self.x = -(self.width // 2)
        self.bg_hover = (255, 0, 174, 215)
        self.bg_press = (255, 120, 212, 215)


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
        self._gui: pyglet_gui.GUI = None
        self._online_btn: MainMenuButton = None
        self._local_btn: MainMenuButton = None
        self._settings_btn: MainMenuButton = None
        self._quit_btn: MainMenuButton = None

    # ----- State necessary methods -----

    def enter(self):
        # Create the GUI and set its position
        self._gui = pyglet_gui.GUI(self._game, self._batch, self._ui_group)
        self._gui.set_pos(self._game.width // 2, Scaler.scale_length(10))

        # Compute the button position and size
        btn_space = Scaler.scale_length(10)

        # Create the gui elements
        self._quit_btn = MainMenuButton("Quit", btn_space)
        self._settings_btn = MainMenuButton("Settings", btn_space * 2 + self._quit_btn.height * 1)
        self._local_btn = MainMenuButton("Local", btn_space * 3 + self._quit_btn.height * 2)
        self._online_btn = MainMenuButton("Online", btn_space * 4 + self._quit_btn.height * 3)

        # Add all buttons to the GUI
        self._gui.add_element(self._online_btn)
        self._gui.add_element(self._local_btn)
        self._gui.add_element(self._settings_btn)
        self._gui.add_element(self._quit_btn)

        # Set the buttons callback
        self._quit_btn.on_click = self._game.stop_app

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
        self._batch.draw()
        pass
