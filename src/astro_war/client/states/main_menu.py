from src.astro_war.config import Config
from src.astro_war.client.scaler import Scaler
from src.astro_war.client.timeline import Timeline
from src.astro_war.client.resources_manager import ResourcesManager
from src.astro_war.client.colors import Colors
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
            color=Colors.MAIN_COLOR + (160,),
            font_name="Munro",
            font_size=Scaler.scale_length(20),
            lab_color=(255, 255, 255, 255),
            border_color=(255, 255, 255, 255),
            border_width=Scaler.scale_length(2),
            border_padding=Scaler.scale_length(5)
        )
        self.x = -(self.width // 2)
        self.bg_hover = Colors.MAIN_COLOR + (215,)
        self.bg_press = Colors.MAIN_COLOR + (255,)


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
        self._mask_group: pyglet.graphics.OrderedGroup = pyglet.graphics.OrderedGroup(3)

        # Declare the mask and it's animation
        self._mask: pyglet.shapes.Rectangle = None
        self._mask_animation: Timeline = Timeline(1.1)
        self._mask_animation.set_loop(False)
        self._mask_animation.set_initial_value(1.0)
        self._mask_animation.add_time_point(1.0, 0.0)

        # Get all the state resources

        # Assign the ui attributes
        self._gui: pyglet_gui.GUI = None
        self._online_btn: MainMenuButton = None
        self._local_btn: MainMenuButton = None
        self._settings_btn: MainMenuButton = None
        self._quit_btn: MainMenuButton = None

        # Declare the menu elements list
        self._menu_elements: list = list()

    # ----- State necessary methods -----

    def enter(self, args):

        # Check if you have to fade in
        if args.get("fade_in_black", False):
            # Create the mask
            self._mask = pyglet.shapes.Rectangle(
                x=0,
                y=0,
                width=self._game.width,
                height=self._game.height,
                color=Colors.BLACK,
                batch=self._batch,
                group=self._mask_group
            )

            # Start the mask animation
            self._mask_animation.start()

        # Create the GUI and set its position
        self._gui = pyglet_gui.GUI(self._game, self._batch, self._ui_group)
        self._gui.set_pos(self._game.width // 2, Scaler.scale_length(10))

        # Compute the button spacing
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

    def handle(self, event) -> None:
        # Handle buttons event
        pass

    def update(self, dt: int) -> None:
        # Update the mask animation if there is the need to
        if not self._mask_animation.is_finish() and self._mask_animation.is_running():
            self._mask_animation.update(dt)
            self._mask.opacity = self._mask_animation.get_value() * 255
        pass

    def render(self) -> None:
        # Render the menu
        self._batch.draw()
        pass
