from src.astro_war.client.event import Event

import pyglet


class BaseState:
    """
    This class is a base for all game states
    """

    # ----- Constructor -----

    def __init__(self, name: str, game: pyglet.window.Window):
        """
        Create a new state with the name and the game app

        params :
            - name: str = The state name
            - game = The game app, to render the scene
        """

        self.name: str = name
        self._game: pyglet.window.Window = game

    # ----- State necessary methods -----

    def enter(self, args: dict) -> None:
        """
        Method to call when the game enter the state

        params :
            - args: dict = Arguments for the state
        """

        pass

    def exit(self) -> None:
        """
        Method to call when the game exit the state
        """

        pass

    def handle(self, event: Event) -> None:
        """
        Handle every pygame events

        params :
            - event: pygame.event.Event = The event coming from pygame
        """

        pass

    def update(self, dt: float) -> None:
        """
        Update the state with the delta time

        params :
            - dt: float = The delta time
        """

        pass

    def render(self) -> None:
        """
        Render the state
        """

        pass
