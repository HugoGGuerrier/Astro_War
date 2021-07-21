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

        self.option_height: int = 45
        self.option_margin: int = 5
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
        self._is_inverted: bool = False
        self._options: list = list()
        self._current_select: int = -1
        self._current_hover: int = -1

        self._bg = pyglet.shapes.Rectangle
        self._label = pyglet.text.Label
        self._border = Border

        self._option_border: Border = None
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

        return (self.x <= x <= self.x + self.width + self.border_width) and\
               (self.y - self.border_width <= y <= self.y + self.height)

    def _hovered_option(self, x: int, y: int) -> int:
        """
        Get the index of the option that is under the mouse if the select is open

        params :
            - x: int = The mouse x position relative to the GUI
            - y: int = The mouse y position relative to the GUI

        return -> int : The option index if one is hovered, -1 otherwise
        """

        # Check that the select is open and the mouse is on the same x
        if self._is_opened:
            if self.x <= x <= self.x + self.width:

                # Compute the options offset from the select main button border
                option_offset = self.option_margin + self.border_width

                # Compute the option panel size
                option_total_size = len(self._options_bg) * self.option_height

                # Compute the option panel y position
                option_panel_base = self.y - option_offset - option_total_size
                option_panel_top = self.y - option_offset

                # Compute the option panel inverted y positions if needed
                if self._is_inverted:
                    option_panel_base = self.y + self.height + option_offset
                    option_panel_top = self.y + self.height + option_offset + option_total_size

                # Check that the mouse is on the option panel
                if option_panel_base <= y <= option_panel_top:
                    # Compute the mouse relative position and return the index by dividing it
                    mouse_rel_y = y - option_panel_base
                    return mouse_rel_y // self.option_height
                else:
                    return -1

    def _update_visual(self):
        """
        This method update the visual of the select element, if the options are opened or not
        """

        # Check if the options are opened
        if self._is_opened:

            self._option_border.set_color(self.border_press)

        else:

            self._option_border.set_color((0, 0, 0, 0))


    # ----- Widget control methods -----

    # ----- Event handling methods -----

    # ----- Element methods -----
