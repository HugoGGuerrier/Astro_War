import pygame

from src.astro_war.client.states import base_state


class SplashScreen(base_state.BaseState):
    """
    The splash screen game state
    """

    # ----- Constructor ------

    def __init__(self, game):
        super().__init__("SplashScreen", game)

    # ----- State necessary methods -----

    def enter(self):
        pass

    def exit(self):
        pass

    def handle(self, event: pygame.event.Event) -> None:
        pass

    def update(self, dt: int) -> None:
        pass

    def render(self) -> None:
        pass
