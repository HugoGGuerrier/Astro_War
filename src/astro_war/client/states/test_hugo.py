from src.astro_war.client.states.base_state import BaseState

import src.pyglet_gui as pyglet_gui
import pyglet


class TestHugo(BaseState):

    def __init__(self, game):
        super().__init__("TestHugo", game)

        # Create the batch and group
        self._batch = pyglet.graphics.Batch()
        group = pyglet.graphics.OrderedGroup(0)

        # Create the interface widgets
        self.gui = pyglet_gui.GUI(self._game, self._batch, group)
        self.btn = pyglet_gui.Button()

        # Add the gui elems
        self.gui.add_element(self.btn)

        # Test shapes :)

    def render(self) -> None:
        # Render the menu
        self._batch.draw()
        pass
