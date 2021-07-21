from .ui_element import UIElement

import pyglet


class GUI:
    """
    This class represent a GUI container, this is where you add all widgets
    """

    def __init__(
            self,
            window: pyglet.window.Window,
            batch: pyglet.graphics.Batch,
            group: pyglet.graphics.Group,
            _x: int = 0,
            _y: int = 0
    ):
        """
        Create a new GUI with the wanted parameters

        params :
            - window: pyglet.window.Window = The pyglet window where the GUI is
            - batch: pyglet.graphics.Batch = The batch where the GUI is drawing
            - group: pyglet.graphics.Group = The group to order the whole GUI on the screen
            - _x: int = The GUI x position
            - _y: int = The GUI y position
        """

        # Assign attributes
        self._window: pyglet.window.Window = window
        self._batch: pyglet.graphics.Batch = batch
        self._group: pyglet.graphics.Group = group
        self._pos: tuple = (_x, _y)
        self._opacity: float = 1.0
        self._ui_elements: list = list()

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

    def get_batch(self) -> pyglet.graphics.Batch:
        """
        Get the GUI batch

        return -> pyglet.graphics.Batch = The GUI batch
        """

        return self._batch

    def get_group(self) -> pyglet.graphics.Group:
        """
        Get the GUI group

        return -> pyglet.graphics.Group = The GUI main group
        """

        return self._group

    def get_pos(self) -> tuple:
        """
        Get the GUI position on the screen

        return -> tuple = The GUI position in a tuple (x, y)
        """

        return self._pos

    # ----- Setters -----

    def set_pos(self, x: int, y: int) -> None:
        """
        Set the GUI position

        params :
            - x: int = The new GUI x position
            - y: int = The new GUI y position
        """

        # Set the position
        self._pos = (x, y)

        # Update all the elements
        for elem in self._ui_elements:
            elem.rebuild(self)

    def set_opacity(self, opacity: int) -> None:
        """
        Set the whole GUI opacity

        params :
            - opacity: int = The new opacity between 0 and 255
        """

        self._opacity = (opacity / 255) % 1.0
        for elem in self._ui_elements:
            elem.opacity = self._opacity
            elem.rebuild(self)

    # ----- Elements -----

    def add_element(self, elem: UIElement) -> None:
        elem.opacity = self._opacity
        elem.create_element(self)
        self._ui_elements.append(elem)

    def remove_element(self, elem: UIElement) -> None:
        elem.delete_element()
        self._ui_elements.remove(elem)
