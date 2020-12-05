from .ui_element import UIElement

import pyglet


class GUI:
    """
    This class represent a GUI container, this is where you add all widgets
    """

    def __init__(
            self,
            window,
            batch,
            group,
            _x=0,
            _y=0
    ):
        # Assign attributes
        self._window = window
        self._batch = batch
        self._group = group
        self._pos = (_x, _y)
        self._ui_elements = list()

        # Set the event handlers
        @self._window.event
        def on_mouse_motion(x, y, dx, dy):
            for elem in self._ui_elements:
                elem.on_mouse_move(x - self._pos[0], y - self._pos[1])

        @self._window.event
        def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
            for elem in self._ui_elements:
                elem.on_mouse_drag(x - self._pos[0], y - self._pos[1], buttons, modifiers)

        @self._window.event
        def on_mouse_press(x, y, button, modifiers):
            for elem in self._ui_elements:
                elem.on_mouse_press(x - self._pos[0], y - self._pos[1], button, modifiers)

        @self._window.event
        def on_mouse_release(x, y, button, modifiers):
            for elem in self._ui_elements:
                elem.on_mouse_release(x - self._pos[0], y - self._pos[1], button, modifiers)

        @self._window.event
        def on_mouse_scroll(x, y, scroll_x, scroll_y):
            pass

    # ----- Getters -----

    def get_batch(self):
        return self._batch

    def get_group(self):
        return self._group

    def get_pos(self):
        return self._pos

    # ----- Setters -----

    def set_pos(self, x, y):
        self._pos = (x, y)
        for elem in self._ui_elements:
            elem.rebuild(self)

    # ----- Elements -----

    def add_element(self, elem):
        elem.create_element(self)
        self._ui_elements.append(elem)
