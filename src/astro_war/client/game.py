from src.astro_war.config import Config
from src.astro_war.bootstrapper import Bootstrapper
from src.astro_war.client.scaler import Scaler
from src.astro_war.client.colors import Colors
from src.astro_war.client.resources_manager import ResourcesManager
from src.astro_war.client.sound_player import SoundPlayer
from src.astro_war.client.states.base_state import BaseState
from src.astro_war.client.states.splash_screen import SplashScreen

import pyglet
import time


class Game(pyglet.window.Window):
    """
    The class that is the game window, this is the main game container
    """

    # ----- Constructor -----

    def __init__(self):
        """
        Create a new app deriving from the windows of pyglet
        """

        # Call the super constructor
        super().__init__(
            width=Config.SCREEN_SIZE[0],
            height=Config.SCREEN_SIZE[1],
            fullscreen=Config.FULL_SCREEN,
            caption=Config.APP_NAME,
            vsync=Config.V_SYNC
        )

        # Set the attributes
        self._is_init: bool = False
        self._is_loaded: bool = False
        self._running: bool = False
        self._time_accu: float = 0
        self._interval: float = 1/Config.FRAME_RATE

        self._state: BaseState = None
        self._clock: pyglet.clock.Clock = None

    # ----- Internal methods -----

    def _init_app(self) -> None:
        """
        Initialize the application
        """

        # Create the clock
        self._clock = pyglet.clock.get_default()

        # Initialize the sound player
        pyglet.options['audio'] = ('pulse', 'directsound', 'openal', 'silent')
        SoundPlayer.init()

        # Set the initialized to true
        self._is_init = True

    def _load_res(self):
        """
        Load all game resources
        """

        # Display the loading text
        pyglet.font.add_file(Config.RES_DIR + "font" + Config.FILE_SEPARATOR + "Munro.ttf")
        pyglet.font.load("Munro")
        loading_label = pyglet.text.Label(
            "Loading...",
            font_name="Munro",
            font_size=36,
            color=(195, 195, 195, 255),
            x=self.width - Scaler.scale_length(10), y=Scaler.scale_length(20),
            anchor_x="right"
        )
        loading_label.draw()
        self.flip()

        # Load the resources
        ResourcesManager.load_all_resources()

        # Set the loaded to true
        self._is_loaded = True

    # ----- Event handling -----

    def on_show(self):
        """
        Event triggered when the window is shown
        """

        # Load the resources adn set the clock
        if not self._is_loaded:
            self._load_res()

            # Set the clock callback method
            self._clock.schedule_interval(self.update, self._interval)

        # Set the initial state if there is none
        if self._state is None:
            self.set_state(SplashScreen(self))

    def on_close(self):
        """
        Method that handle the game close
        """

        self.stop_app()

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        """
        This event triggers when a keyboard key is pressed
        """

        print("Key pressed : " + str(symbol))

    # ----- Application control methods -----

    def update(self, dt: float):
        """
        Update the game state, this method is called every tick of the game

        params :
            - dt: float = The number of seconds since the last call
        """

        # Verify that the app is running
        if self._running:
            # Clean the screen
            self.clear()

            # Update the current state
            self._state.update(self._time_accu + dt)

            # Configure the opengl scaling function
            pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)
            pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)

            # Render the state
            self._state.render()
        else:
            # Increase the time accumulator
            self._time_accu += dt

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
        print("--- Enter " + state.name + " state")
        self._state = state
        self._state.enter()

    def start_app(self) -> None:
        """
        Start the application
        """

        # Init the application
        if not self._is_init:
            self._init_app()

        # Start the app
        self._running = True

        pyglet.app.run()

    def stop_app(self):
        """
        Stop the application
        """

        # Cleanup the application
        Bootstrapper.save()

        # Clear the window
        self.clear()

        # Close the windows
        pyglet.app.exit()
