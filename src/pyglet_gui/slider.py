from .ui_element import UIElement
from .border import Border

import pyglet


class Slider(UIElement):
    """
    This class represent a slider to select a value between 2
    """

    def __init__(self):
        """
        Create a slider with the default parameters
        """

        # Call the super constructor
        super().__init__(0, 0, 500, 40)

        # Set all customization attributes
        self.min_value: float = 0
        self.max_value: float = 1
        self.init_value: float = 0

        self.cursor_width: int = 20
        self.cursor_color: tuple = (95, 95, 95, 255)
        self.cursor_hover: tuple = (95, 95, 168, 255)
        self.cursor_press: tuple = (60, 60, 60, 255)

        self.border_color: tuple = (255, 255, 255, 255)
        self.border_hover: tuple = None
        self.border_press: tuple = None
        self.border_width: int = 0

        self.bar_width: int = 5
        self.empty_color: tuple = (255, 255, 255, 100)
        self.full_color: tuple = (255, 255, 255, 100)

        self.on_value_change = None

        # Assign the internal attributes
        self._cursor: pyglet.shapes.Rectangle = None
        self._border: Border = None
        self._empty: pyglet.shapes.Line = None
        self._full: pyglet.shapes.Line = None
        self._value: float = self.init_value

    # ----- Internal methods -----

    def _get_cursor_pos(self) -> float:
        """
        Get the current cursor position by computing the value

        return -> int = The cursor x position relative to the slider origin
        """

        coef = (self._value - self.min_value) / (self.max_value - self.min_value)
        return (self.width * coef) + self.x

    # ----- Widget control methods -----

    def get_value(self) -> float:
        """
        Get the current slider value

        return -> float = The current slider value
        """

        return self._value

    def set_value(self, value: float):
        """
        Set the slider value and update the visual elements

        params:
            - value: float = The new value
        """

        # Assign the value
        if value >= self.max_value:
            self._value = self.max_value
        elif value <= self.min_value:
            self._value = self.min_value
        else:
            self._value = value

        # Update the visual elements

    # ----- Event handling methods -----

    # ----- Element methods -----

    def create_element(self, gui):
        """
        Create the slider in the gui

        params :
            - gui = The GUI to create the slider in
        """

        # Call the super method
        super(Slider, self).create_element(gui)

        # Get thee GUI position
        gui_x, gui_y = gui.get_pos()

        # Create the cursor
        self._cursor = pyglet.shapes.Rectangle(
            x=self._get_cursor_pos() + self.x,
            y=self.y,
            width=self.cursor_width,
            height=self.height,
            batch=self._batch,
            group=pyglet.graphics.OrderedGroup(1, parent=self._group)
        )
