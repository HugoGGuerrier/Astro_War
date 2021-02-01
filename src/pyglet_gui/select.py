from .ui_element import UIElement
from .border import Border

import pyglet


class Select(UIElement):
    """
    This class is a select list
    """
    
    def __init__(self):
        """
        Create a new select list with the default parameters and an empty set of options
        """
        
        # Call the super contructor
        super(Select, self).__init__(0, 0, 200, 50)

        # Assign personalisation attributes
        self.placeholder = "Choose a value"
        self.font_name: str = None
        self.font_size: int = 12

        self.bg_color: tuple = (0, 0, 0, 0)
        self.bg_hover: tuple = (255, 255, 255, 30)
        self.bg_press: tuple = None

        self.label_color: tuple = (255, 255, 255, 255)
        self.label_hover: tuple = None
        self.label_press: tuple = None

        self.border_color: tuple = (255, 255, 255, 255)
        self.border_hover: tuple = None
        self.border_press: tuple = None
        self.border_width: int = 4

        self.option_reverse: bool = False
        self.option_height: int = 45
        self.option_font_name = None
        self.option_font_size = 12

        self.option_bg_color: tuple = (0, 0, 0, 0)
        self.option_bg_hover: tuple = (255, 255, 255, 30)
        self.option_bg_press: tuple = None
        self.option_bg_select: tuple = (255, 255, 255, 60)

        self.option_label_color: tuple = (255, 255, 255, 255)
        self.option_label_hover: tuple = None
        self.option_label_press: tuple = None
        self.option_label_select: tuple = None

        # Assign internal attributes
        self._is_hovered: bool = False
        self._is_pressed: bool = False
        self._is_opened: bool = False
        self._options: list = list()
        self._current_select: int = -1
        self._current_hover: int = -1

        self._bg = pyglet.shapes.Rectangle
        self._label = pyglet.text.Label
        self._border = Border

        self._options_bg: list = list()
        self._options_label: list = list()

    # ----- Internal methods -----

    def _is_hover_main(self, x: int, y: int) -> bool:
        """
        Return if the mouse is hover the main select button

        params :
            - x: int = The mouse x position relative to the GUI
            - y: int = The mouse y position relative to the GUI

        return -> bool = True if the mouse is over the main button
        """

        return (self.x <= x <= self.x + self.width + self.border_width) and (self.y - self.border_width <= y <= self.y + self.height)

    def _hovered_option(self, x: int, y: int):
        """
        Get the index of the option that is under the mouse if the select is open

        params :
            - x: int = The mouse x position relative to the GUI
            - y: int = The mouse y position relative to the GUI
        """

        # Check that the select is open and the mouse is on the same x
        if self._is_opened:
            if self.x <= x <= self.x + self.width:

                # Compute the options offset
                option_offset =

                # Iterate over the options
                for i in range(len(self._options)):



    # ----- Event handling methods -----

    # ----- Element methods -----
