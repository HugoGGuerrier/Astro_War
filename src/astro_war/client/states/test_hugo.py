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
        self.gui.set_pos(10, 10)
        self.btn = pyglet_gui.Button()

        self.slider = pyglet_gui.Slider()
        self.slider.y = 75

        # Add the gui elements
        self.gui.add_element(self.btn)
        self.gui.add_element(self.slider)

        # Test shapes :)

    def render(self) -> None:
        # Render the menu
        self._batch.draw()
        pass
