from src.astro_war.client.states.base_state import BaseState


class Menu(BaseState):

    # ----- Constructor -----

    def __init__(self, game):
        super().__init__("Menu", game)

