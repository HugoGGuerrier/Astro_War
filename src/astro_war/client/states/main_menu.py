from src.astro_war.config import Config
from src.astro_war.client.states.base_state import BaseState
from src.astro_war.client.scaler import Scaler

import pygame
import pygame_gui


class MainMenu(BaseState):

    # ----- Constructor -----

    def __init__(self, game):
        super().__init__("MainMenu", game)

        # Get all the state resources

        # Create main menu buttons
        self._gui_manager: pygame_gui.ui_manager.UIManager = None
        self._online_btn: pygame_gui.elements.UIButton = None
        self._local_btn: pygame_gui.elements.UIButton = None
        self._settings_btn: pygame_gui.elements.UIButton = None
        self._quit_btn: pygame_gui.elements.UIButton = None

    # ----- State necessary methods -----

    def enter(self):
        # Compute the button position
        btn_width = Scaler.scale_length(200)
        btn_height = Scaler.scale_length(50)
        btn_x = (Config.SCREEN_SIZE[0] / 2) - (btn_width / 2)
        btn_base_y = Config.SCREEN_SIZE[1] - 10
        btn_space = btn_height + Scaler.scale_length(10)

        online_btn_pos = pygame.Rect(btn_x, btn_base_y - btn_space * 4, btn_width, btn_height)
        local_btn_pos = pygame.Rect(btn_x, btn_base_y - btn_space * 3, btn_width, btn_height)
        settings_btn_pos = pygame.Rect(btn_x, btn_base_y - btn_space * 2, btn_width, btn_height)
        quit_btn_pos = pygame.Rect(btn_x, btn_base_y - btn_space, btn_width, btn_height)

        # Create the gui elements
        self._gui_manager = pygame_gui.ui_manager.UIManager(tuple(Config.SCREEN_SIZE))
        self._online_btn = pygame_gui.elements.UIButton(
            relative_rect=online_btn_pos,
            text="Online",
            manager=self._gui_manager
        )
        self._local_btn = pygame_gui.elements.UIButton(
            relative_rect=local_btn_pos,
            text="Local",
            manager=self._gui_manager
        )
        self._settings_btn = pygame_gui.elements.UIButton(
            relative_rect=settings_btn_pos,
            text="Settings",
            manager=self._gui_manager
        )
        self._quit_btn = pygame_gui.elements.UIButton(
            relative_rect=quit_btn_pos,
            text="Quit",
            manager=self._gui_manager
        )

    def init(self):
        pass

    def exit(self):
        pass

    def handle(self, event: pygame.event.Event) -> None:
        # Handle buttons event
        if event.type == pygame.USEREVENT :
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self._quit_btn:
                    self._game.stop_app()

        # Process the event in the manager
        self._gui_manager.process_events(event)

    def update(self, dt: int) -> None:
        # Update the ui manager
        self._gui_manager.update(dt)

    def render(self) -> None:
        # Render the gui
        self._gui_manager.draw_ui(self._surface)
