from .ui_element import UIElement
from .border import Border
from .icons import *

import pyglet


class CheckBox(UIElement):
    """
    This class represent a simple check box with its label
    """

    def __init__(self):
        """
        Create a new checkbox with the default parameters
        """

        # Call the super constructor
        super().__init__(0, 0, 350, 40)

        # Assign personalisation attributes
        self.text: str = "Checkbox"
        self.font_name: str = None
        self.font_size: int = 12

        self.case_color: tuple = (0, 0, 0, 0)
        self.case_hover: tuple = (255, 255, 255, 30)
        self.case_press: tuple = None

        self.label_color: tuple = (255, 255, 255, 255)
        self.label_hover: tuple = None
        self.label_press: tuple = None

        self.border_color: tuple = (255, 255, 255, 255)
        self.border_hover: tuple = None
        self.border_press: tuple = None

        self.tick_style: str = "cross"
        self.tick_color: tuple = (255, 255, 255, 255)
        self.tick_hover: tuple = None
        self.tick_press: tuple = None

        self.on_checked = None

        # Assign intern attributes
        self._is_hovered: bool = False
        self._is_checked: bool = False
        self._case: pyglet.shapes.Rectangle = None
        self._tick: Icon = None
        self._border: Border = None
        self._label: pyglet.text.Label = None

    # ----- Internal methods -----

    def _is_hover(self, x: int, y: int) -> bool:
        """
        Get if the mouse cursor is hover the tick box

        params :
            - x: int = The mouse x position relative to the GUI
            - y: int = The mouse y position relative to the GUI
        """

        return False

    # ----- Widget control methods -----

    def is_checked(self) -> bool:
        """
        Get if the checkbox is checked
        """

        return self._is_checked

    def set_checked(self, is_checked: bool) -> None:
        """
        Set the checked state
        """

        # Set the state attribute
        self._is_checked = is_checked

        # Update the visual
        # TODO

        # Call the function
        if self.on_checked is not None:
            self.on_checked(self._is_checked)

    # ----- Event handling methods -----

    # ----- Element methods -----

    def create_element(self, gui):
        """
        Create the checkbox
        """

        # Call the super method
        super(CheckBox, self).create_element(gui)

        # Compute the element's position
        case_x = self.x + (self.width - self.height)

        # Create the case rectangle

