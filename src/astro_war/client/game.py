from src.astro_war import Config, bootstrapper
from src.astro_war.client import resources_manager, Colors
from src.astro_war.client.scaler import Scaler
from src.astro_war.client.states import base_state

import pygame


class Game:
    """
    This is the main class for the game application
    """

    # ----- Constructor -----

    def __init__(self):
        """
        Create a new game instance
        """

        self._is_init: bool = False
        self._is_loaded: bool = False
        self._running: bool = False
        self._interval: int = round(1000 / Config.FRAME_RATE)

        self._state: base_state.BaseState = None
        self._surface: pygame.Surface = None

    # ----- Internal methods -----

    def _init_app(self) -> None:
        """
        Initialize the application
        """

        # Initialize pygame
        pygame.init()

        # Create the containing windows flags
        flags: int = pygame.HWSURFACE
        if Config.FULL_SCREEN:
            flags |= pygame.FULLSCREEN

        # Get if the vsync is on
        vsync: int = 0
        if Config.V_SYNC:
            vsync = 1

        # Create the game window
        pygame.display.set_caption(Config.APP_NAME, Config.ICON_NAME)
        self._surface = pygame.display.set_mode(Config.SCREEN_SIZE, flags=flags, vsync=vsync)

        # Set the initialization to true
        self._is_init = True

    def _load_res(self) -> None:
        """
        Load all game resources
        """

        # Display the loading screen
        loading_font = pygame.font.Font(Config.RES_DIR + "font" + Config.FILE_SEPARATOR + "Munro.ttf", 40)
        loading_surface = loading_font.render("Loading...", False, Colors.WHITE)
        position = (
            Config.SCREEN_SIZE[0] - (loading_surface.get_width() + Scaler.scale_length(10)),
            Config.SCREEN_SIZE[1] - (loading_surface.get_height() + Scaler.scale_length(10))
        )
        self._surface.blit(loading_surface, position)
        pygame.display.flip()

        # Load the resources
        resources_manager.ResourcesManager.load()
        self._is_loaded = True

    def _cleanup(self) -> None:
        """
        Method to call just before the application end
        """

        # Close pygame
        pygame.quit()

        # Reset the class
        self._is_init = False
        self._running = False

        self._surface = None

        # Save the application config
        bootstrapper.Bootstrapper.save()

    def _handle_event(self, event: pygame.event.Event) -> None:
        """
        This methods handle all game events

        params :
            - event: pygame.event.Event = The event to handle
        """

        # Handle general events
        if event.type == pygame.QUIT:
            self.stop_app()

    # ----- Application control methods -----

    def start_app(self) -> None:
        """
        Start the application
        """

        # Initialize the game if it's not
        if not self._is_init:
            self._init_app()

        # Load all resources
        if not self._is_loaded:
            self._load_res()

        # Start the game loop
        self._running = True
        while self._running:

            # Clear the display
            self._surface.fill(Colors.EMPTY)

            # Handle all events
            for event in pygame.event.get():
                self._handle_event(event)

            # Update and render the state
            self._state.update(self._interval)
            self._state.render()

            # Update the display
            pygame.display.flip()

            # Wait the interval
            pygame.time.delay(self._interval)

        # Exit the application
        self._cleanup()

    def stop_app(self) -> None:
        """
        Stop the application
        """

        self._running = False

    def set_state(self, state: base_state.BaseState):
        """
        Set the current game state

        params :
            - state: base_state.BaseState = The state to set
        """

        # Exit the previous state
        if self._state is not None:
            self._state.exit()

        # Enter the next state
        self._state = state
        self._state.enter()
