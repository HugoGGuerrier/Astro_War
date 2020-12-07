from .ui_element import UIElement

import pyglet
from pyglet.window import mouse


class Button(UIElement):
    """
    This class represent a base button with default style and event handler
    """

    def __init__(
            self,
            x: int = 0,
            y: int = 0,
            width: int = 200,
            height: int = 50,
            text: str = "Button",
            font_name: str = None,
            font_size: int = 12,
            color: tuple = (150, 150, 150, 255),
            lab_color: tuple = (255, 255, 255, 255),
            border_color: tuple = (255, 255, 255, 255),
            border_width: int = 1,
            border_padding: int = 0
    ):
        """
        Create a button with the wanted parameters

        params :
            - x: int = The button x position, relative to the GUI position
            - y: int = The button y position, relative to the GUI position
            - width: int = The button width
            - height: int = The button height
            - text: str = The button text
            - font_name: str = The font name for the button text
            - font_size: int = The button font size
            - color: tuple = The button background color
            - lab_color: tuple = The button text color
            - border_color: tuple = The button border color
            - border_width: int = 1 = The width of the border
            - border_padding: int = 0 = The space between border and button edge
        """

        # Call the super constructor
        super().__init__(x, y, width, height)

        # Assign personalisation attributes
        self.text: str = text
        self.font_name: str = font_name
        self.font_size: int = font_size
        self.bg_color: tuple = color
        self.bg_hover: tuple = (95, 95, 168, 255)
        self.bg_press: tuple = (60, 60, 60, 255)
        self.label_color: tuple = lab_color
        self.label_hover: tuple = None
        self.label_press: tuple = None
        self.border_color: tuple = border_color
        self.border_hover: tuple = None
        self.border_press: tuple = None
        self.border_width: int = border_width
        self.border_padding: int = border_padding
        self.on_click = None

        # Assign internal attributes
        self._is_clicked: bool = False
        self._is_hovered: bool = False
        self._bg: pyglet.shapes.Rectangle = None
        self._label: pyglet.text.Label = None
        self._borders: list = list()

    # ----- Internal methods -----

    def _is_hover(self, x: int, y: int) -> bool:
        """
        Check if the point is in the button

        params :
            - x: int = The gui relative x position
            - y: int = The gui relative y position
        """

        return (self.x <= x <= self.x + self.width) and (self.y <= y <= self.y + self.height)

    # ----- Event handling methods -----

    def on_mouse_move(self, x: int, y: int):
        """
        Check the mouse move to make the hover effect
        """

        # Check if the button is not clicked
        if not self._is_clicked:

            # Check if the button is hovered
            if self._is_hover(x, y):

                # Set the hovered state to true
                self._is_hovered = True

                # Set the background color
                self._bg.color = self.bg_hover[:-1]
                self._bg.opacity = self.bg_hover[-1] * self.opacity

                # Set the label color
                if self.label_hover is not None:
                    self._label.color = self.label_hover[:-1] + (round(self.label_hover[-1] * self.opacity),)

                # Set the borders color
                if self.border_hover is not None:
                    for border in self._borders:
                        border.color = self.border_hover[:-1]
                        border.opacity = self.border_hover[-1] * self.opacity

            elif self._is_hovered:

                # Set the hovered state to false
                self._is_hovered = False

                # Reset the background color
                self._bg.color = self.bg_color[:-1]
                self._bg.opacity = self.bg_color[-1] * self.opacity

                # Reset the label color
                if self.label_hover is not None:
                    self._label.color = self.label_color[:-1] + (round(self.label_color[-1] * self.opacity),)

                # Reset the borders color
                if self.border_hover is not None:
                    for border in self._borders:
                        border.color = self.border_color[:-1]
                        border.opacity = self.border_color[-1] * self.opacity

    def on_mouse_drag(self, x: int, y: int, button: int, mod: int):
        # Just do the same as mouse move
        self.on_mouse_move(x, y)

    def on_mouse_press(self, x: int, y: int, button: int, mod: int):
        """
        Handle the mouse click
        """

        # Check that the mouse is over the button and the click is the left
        if button & mouse.LEFT and self._is_hover(x, y):

            # Set the clicked to true
            self._is_clicked = True

            # Set the background color
            self._bg.color = self.bg_press[:-1]
            self._bg.opacity = self.bg_press[-1] * self.opacity

            # Set the label color
            if self.label_press is not None:
                self._label.color = self.label_press

            # Set the borders color
            if self.border_press is not None:
                for border in self._borders:
                    border.color = self.border_press[:-1]
                    border.opacity = self.border_press[-1] * self.opacity

    def on_mouse_release(self, x, y, button, mod):
        """
        Handle the mouse release
        """

        # Check that the click release is the left one
        if button & mouse.LEFT:

            # Set the clicked to false
            self._is_clicked = False

            # Call the button update
            self.on_mouse_move(x, y)

            # If the mouse is over the button when release, call the on_click method
            if self._is_hover(x, y):
                if self.on_click is not None:
                    self.on_click()

    # ----- Element methods -----

    def create_element(self, gui):
        """
        Add the button to the wanted GUI

        params :
            - gui : The parent GUI
        """

        # Call the super method
        super(Button, self).create_element(gui)

        # Get the gui attributes
        gui_x, gui_y = gui.get_pos()

        # Create the background rectangle
        self._bg = pyglet.shapes.Rectangle(
            x=self.x + gui_x,
            y=self.y + gui_y,
            width=self.width,
            height=self.height,
            color=self.bg_color[:-1],
            batch=self._batch,
            group=pyglet.graphics.OrderedGroup(0, parent=self._group)
        )
        self._bg.opacity = self.bg_color[-1] * self.opacity

        # Create the label text
        self._label = pyglet.text.Label(
            text=self.text,
            font_name=self.font_name,
            font_size=self.font_size,
            color=self.label_color[:-1] + (round(self.label_color[-1] * self.opacity),),
            anchor_x="center",
            anchor_y="center",
            x=(self.x + gui_x) + self.width // 2,
            y=(self.y + gui_y) + self.height // 2,
            batch=self._batch,
            group=pyglet.graphics.OrderedGroup(2, parent=self._group)
        )

        # Create the borders

        # --- Top
        self._borders.append(
            pyglet.shapes.Line(
                x=(self.x + self.border_padding - self.border_width / 2) + gui_x,
                y=(self.y + self.height - self.border_padding) + gui_y,
                x2=(self.x + self.width - self.border_padding + self.border_width / 2) + gui_x,
                y2=(self.y + self.height - self.border_padding) + gui_y,
                color=self.border_color[:-1],
                width=self.border_width,
                batch=self._batch,
                group=pyglet.graphics.OrderedGroup(1, parent=self._group)
            )
        )

        # --- Right
        self._borders.append(
            pyglet.shapes.Line(
                x=(self.x + self.width - self.border_padding) + gui_x,
                y=(self.y + self.height - self.border_padding) + gui_y,
                x2=(self.x + self.width - self.border_padding) + gui_x,
                y2=(self.y + self.border_padding) + gui_y,
                color=self.border_color[:-1],
                width=self.border_width,
                batch=self._batch,
                group=pyglet.graphics.OrderedGroup(1, parent=self._group)
            )
        )

        # --- Bottom
        self._borders.append(
            pyglet.shapes.Line(
                x=(self.x + self.border_padding - self.border_width / 2) + gui_x,
                y=(self.y + self.border_padding) + gui_y,
                x2=(self.x + self.width - self.border_padding + self.border_width / 2) + gui_x,
                y2=(self.y + self.border_padding) + gui_y,
                color=self.border_color[:-1],
                width=self.border_width,
                batch=self._batch,
                group=pyglet.graphics.OrderedGroup(1, parent=self._group)
            )
        )

        # --- Left
        self._borders.append(
            pyglet.shapes.Line(
                x=(self.x + self.border_padding) + gui_x,
                y=(self.y + self.height - self.border_padding) + gui_y,
                x2=(self.x + self.border_padding) + gui_x,
                y2=(self.y + self.border_padding) + gui_y,
                color=self.border_color[:-1],
                width=self.border_width,
                batch=self._batch,
                group=pyglet.graphics.OrderedGroup(1, parent=self._group)
            )
        )

        # Set the borders opacity
        for border in self._borders:
            border.opacity = self.border_color[-1] * self.opacity

    def rebuild(self, gui):
        """
        Rebuild the button with the new GUI state

        Add the button to the wanted GUI

        params :
            - gui : The parent GUI
        """

        # Get the gui attributes
        gui_x, gui_y = gui.get_pos()

        # Rebuild the background
        self._bg.x = self.x + gui_x
        self._bg.y = self.y + gui_y
        self._bg.width = self.width
        self._bg.height = self.height
        self._bg.color = self.bg_color[:-1]
        self._bg.opacity = self.bg_color[-1] * self.opacity

        # Rebuild the label
        self._label.x = (self.x + gui_x) + self.width // 2
        self._label.y = (self.y + gui_y) + self.height // 2
        self._label.text = self.text
        self._label.font_name = self.font_name
        self._label.font_size = self.font_size
        self._label.color = self.label_color[:-1] + (round(self.label_color[-1] * self.opacity),)

        # Rebuild the borders
        # TODO
        for border in self._borders:
            border.opacity = self.border_color[-1] * self.opacity
