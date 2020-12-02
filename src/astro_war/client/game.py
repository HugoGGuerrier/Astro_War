from src.astro_war.config import Config
from src.astro_war.bootstrapper import Bootstrapper
from src.astro_war.client.scaler import Scaler
from src.astro_war.client.colors import Colors
from src.astro_war.client.resources_manager import ResourcesManager
from src.astro_war.client.sound_player import SoundPlayer
from src.astro_war.client.states.base_state import BaseState
from src.astro_war.client.states.splash_screen import SplashScreen

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

        self._clock: pygame.time.Clock = None
        self._state: BaseState = None
        self._surface: pygame.Surface = None

    # ----- Getters -----

    def get_surface(self) -> pygame.surface.Surface:
        """
        Get the drawing surface

        return -> pygame.surface.Surface = The surface
        """

        return self._surface

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

        # Initialize the sound player
        SoundPlayer.init()

        # Create the clock
        self._clock = pygame.time.Clock()

        # Set the initialization to true
        self._is_init = True

    def _load_res(self) -> None:
        """
        Load all game resources
        """

        # Display the loading screen
        loading_font = pygame.font.Font(Config.RES_DIR + "font" + Config.FILE_SEPARATOR + "Munro.ttf", 40)
        loading_surface = loading_font.render("Loading...", False, (220, 220, 220))
        position = (
            Config.SCREEN_SIZE[0] - (loading_surface.get_width() + Scaler.scale_length(10)),
            Config.SCREEN_SIZE[1] - (loading_surface.get_height() + Scaler.scale_length(10))
        )
        self._surface.blit(loading_surface, position)
        pygame.display.flip()

        # Load the resources
        ResourcesManager.load_all_resources()
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
        Bootstrapper.save()

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

        # Set the starting state
        self.set_state(SplashScreen(self))

        # Reset the clock
        self._clock.tick()

        # Start the game loop
        self._running = True
        while self._running:

            # Get the delta time
            dt = self._clock.tick(Config.FRAME_RATE)

            # Clear the display
            self._surface.fill(Colors.EMPTY)

            # Handle all events
            for event in pygame.event.get():
                self._handle_event(event)

            # Update and render the state
            self._state.update(dt)
            self._state.render()

            # Update the display
            pygame.display.flip()

        # Exit the application
        self._cleanup()

    def stop_app(self) -> None:
        """
        Stop the application
        """

        self._running = False

    def set_state(self, state: BaseState):
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
        self._state.init()
