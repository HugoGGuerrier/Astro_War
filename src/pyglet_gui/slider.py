from .ui_element import UIElement

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
        self.init_value: float = 0.5

        self.font_name: str = None
        self.font_size: int = 12

        self.cursor_color: tuple = (95, 95, 95, 255)
        self.cursor_hover: tuple = (95, 95, 168, 255)
        self.cursor_press: tuple = (60, 60, 60, 255)

        self.label_color: tuple = (255, 255, 255, 255)
        self.label_padding: int = 5

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
        self._borders: list = list()
        self._empty: pyglet.shapes.Line = None
        self._full: pyglet.shapes.Line = None
        self._min_label: pyglet.text.Label = None
        self._max_label: pyglet.text.Label = None

    # ----- Internal methods -----

    # ----- Event handling methods -----

    # ----- Element methods -----
