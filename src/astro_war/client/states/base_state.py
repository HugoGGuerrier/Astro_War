import pygame


class BaseState:
    """
    This class is a base for all game states
    """

    # ----- Constructor -----

    def __init__(self, name: str, game):
        """
        Create a new state with the name and the game app

        params :
            - name: str = The state name
            - game = The game app, to render the scene
        """

        self._name: str = name
        self._game = game
        self._surface: pygame.surface.Surface = game.get_surface()

    # ----- State necessary methods -----

    def enter(self) -> None:
        """
        Method to call when the game enter the state
        """

        pass

    def exit(self) -> None:
        """
        Method to call when the game exit the state
        """

        pass

    def handle(self, event: pygame.event.Event) -> None:
        """
        Handle every pygame events

        params :
            - event: pygame.event.Event = The event coming from pygame
        """

        pass

    def update(self, dt: int) -> None:
        """
        Update the state with the delta time

        params :
            - dt: int = The delta time
        """

        pass

    def render(self) -> None:
        """
        Render the state
        """

        pass
