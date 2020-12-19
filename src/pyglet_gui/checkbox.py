from .ui_element import UIElement
from .border import Border
from .icons import *

import pyglet
from pyglet.window import mouse


class CheckBox(UIElement):
    """
    This class represent a simple check box with its label
    """

    def __init__(self):
        """
        Create a new checkbox with the default parameters
        """

        # Call the super constructor
        super().__init__(0, 0, 150, 40)

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

        self.border_width: int = 4
        self.border_color: tuple = (255, 255, 255, 255)
        self.border_hover: tuple = None
        self.border_press: tuple = None

        self.tick_style: str = "cross"
        self.tick_padding: int = 8
        self.tick_color: tuple = (255, 255, 255, 255)
        self.tick_hover: tuple = None
        self.tick_press: tuple = None

        self.on_checked = None

        # Assign intern attributes
        self._case: pyglet.shapes.Rectangle = None
        self._tick: Icon = None
        self._border: Border = None
        self._label: pyglet.text.Label = None

        self._is_checked: bool = False
        self._is_hovered: bool = False
        self._is_pressed: bool = False

    # ----- Internal methods -----

    def _is_hover(self, x: int, y: int) -> bool:
        """
        Get if the mouse cursor is hover the tick box

        params :
            - x: int = The mouse x position relative to the GUI
            - y: int = The mouse y position relative to the GUI
        """

        case_x = self.x + (self.width - self.height)
        return (case_x <= x <= self.x + self.width) and (self.y <= y <= self.y + self.height)

    def _update_visual(self):
        """
        Update the checkbox visual
        """

        # Update the tick according to the state
        if self._is_checked:

            if self._is_pressed and self.tick_press is not None:
                self._tick.set_opacity(self.tick_press[-1] * self.opacity)
            elif self._is_hovered and self.tick_hover is not None:
                self._tick.set_opacity(self.tick_hover[-1] * self.opacity)
            else:
                self._tick.set_opacity(self.tick_color[-1] * self.opacity)

        else:
            self._tick.set_opacity(0)

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
        if self._exists:
            self._update_visual()

        # Call the function
        if self.on_checked is not None:
            self.on_checked(self._is_checked)

    # ----- Event handling methods -----

    def on_mouse_move(self, x: int, y: int):
        """
        Handle mouse moving
        """

        # Check if the checkbox is clicked
        if not self._is_pressed:

            # Check if the mouse cursor is on the checkbox
            if self._is_hover(x, y):

                # Set the hover state to true
                self._is_hovered = True

                # Set the case color
                if self.case_hover is not None:
                    self._case.color = self.case_hover[:-1]
                    self._case.opacity = self.case_hover[-1] * self.opacity

                # Set the label color
                if self.label_hover is not None:
                    self._label.color = self.label_hover[:-1] + (round(self.label_hover[-1] * self.opacity),)

                # Set the border color
                if self.border_hover is not None:
                    self._border.set_color(self.border_hover[:-1] + (self.border_hover[-1] * self.opacity,))

                # Set the tick color
                if self.tick_hover is not None:
                    self._tick.set_color(self.tick_hover[:-1])
                    self._update_visual()

            else:

                # Set the hovered state to false
                self._is_hovered = False

                # Reset the case color
                if self.case_hover is not None:
                    self._case.color = self.case_color[:-1]
                    self._case.opacity = self.case_color[-1] * self.opacity

                # Reset the label color
                if self.label_hover is not None:
                    self._label.color = self.label_color[:-1] + (round(self.label_color[-1] * self.opacity),)

                # Reset the border color
                if self.border_hover is not None:
                    self._border.set_color(self.border_color[:-1] + (self.border_color[-1] * self.opacity,))

                # Reset the tick color
                if self.tick_hover is not None:
                    self._tick.set_color(self.tick_color[:-1])
                    self._update_visual()

    def on_mouse_drag(self, x: int, y: int, button: int, mod: int):
        # Just do the same as mouse move
        self.on_mouse_move(x, y)

    def on_mouse_press(self, x: int, y: int, button: int, mod: int):
        """
        Handle the mouse pressing
        """

        # Check the pressed button and the mouse position
        if button & mouse.LEFT and self._is_hovered:

            # Set the pressed state
            self._is_pressed = True

            # Set the case color
            if self.case_press is not None:
                self._case.color = self.case_press[:-1]
                self._case.opacity = self.case_press[-1] * self.opacity

            # Set the label color
            if self.label_press is not None:
                self._label.color = self.label_press[:-1] + (round(self.label_press[-1] * self.opacity),)

            # Set the border color
            if self.border_press is not None:
                self._border.set_color(self.border_press[:-1] + (self.border_press[-1] * self.opacity,))

            # Set the tick color
            if self.tick_press is not None:
                self._tick.set_color(self.tick_press[:-1])
                self._update_visual()

    def on_mouse_release(self, x: int, y: int, button: int, mod: int):
        """
        Handle the mouse release
        """

        # Verify the pressed button and the pressed state
        if button & mouse.LEFT and self._is_pressed:

            # Set the pressed state to false
            self._is_pressed = False

            # Update the checkbox state
            self.on_mouse_move(x, y)

            # Change the check value
            if self._is_hover(x, y):
                self._is_checked = not self._is_checked
                self._update_visual()
                if self.on_checked is not None:
                    self.on_checked(self._is_checked)

    # ----- Element methods -----

    def create_element(self, gui):
        """
        Create the checkbox
        """

        # Call the super method
        super(CheckBox, self).create_element(gui)

        # Compute the element's position
        case_x = self.x + (self.width - self.height)

        # Get the icon style
        icon = Cross
        if self.tick_style == "square":
            icon = Square

        # Create the label
        self._label = pyglet.text.Label(
            text=self.text,
            font_name=self.font_name,
            font_size=self.font_size,
            color=self.label_color[:-1] + (round(self.label_color[-1] * self.opacity),),
            x=self.x + self._gui_x,
            y=self.y + self.height / 2 + self._gui_y,
            anchor_y="center",
            batch=self._batch,
            group=pyglet.graphics.OrderedGroup(0, parent=self._group)
        )

        # Create the case rectangle
        self._case = pyglet.shapes.Rectangle(
            x=case_x + self._gui_x,
            y=self.y + self._gui_y,
            width=self.height,
            height=self.height,
            color=self.case_color[:-1],
            batch=self._batch,
            group=pyglet.graphics.OrderedGroup(1, parent=self._group)
        )
        self._case.opacity = self.case_color[-1] * self.opacity

        # Create the case border
        self._border = Border(
            batch=self._batch,
            group=pyglet.graphics.OrderedGroup(2, parent=self._group),
            border_width=self.border_width
        )
        self._border.set_pos(
            x=case_x + self._gui_x,
            y=self.y + self._gui_y,
            width=self.height,
            height=self.height,
        )
        self._border.set_color(self.border_color[:-1] + (self.border_color[-1] * self.opacity,))

        # Create the case tick icon
        self._tick = icon(
            batch=self._batch,
            group=pyglet.graphics.OrderedGroup(3, parent=self._group),
            line_width=4
        )
        self._tick.set_pos(
            x=case_x + self.tick_padding + self._gui_x,
            y=self.y + self.tick_padding + self._gui_y,
            width=self.height - self.tick_padding * 2,
            height=self.height - self.tick_padding * 2,
        )
        self._tick.set_color(self.tick_color[:-1])
        self._tick.set_opacity(self.tick_color[-1] * self.opacity)

        # Update the visual
        self._update_visual()

    def rebuild(self, gui):
        """
        Rebuild all graphical elements of the checkbox
        """

        # Call the super method
        super(CheckBox, self).rebuild(gui)

        # Compute the case position
        case_x = self.x + (self.width - self.height)

        # Get the icon style
        icon = Cross
        if self.tick_style == "square":
            icon = Square

        # Rebuild the label
        self._label.text = self.text
        self._label.font_name = self.font_name
        self._label.font_size = self.font_size
        self._label.color = self.label_color[:-1] + (round(self.label_color[-1] * self.opacity),)
        self._label.x = self.x + self._gui_x
        self._label.y = self.y + self.height / 2 + self._gui_y

        # Rebuild the case
        self._case.x = case_x + self._gui_x
        self._case.y = self.y + self._gui_y
        self._case.width = self.height
        self._case.height = self.height
        self._case.color = self.case_color[:-1]
        self._case.opacity = self.case_color[-1] * self.opacity

        # Rebuild the case border
        self._border.delete()
        self._border = Border(
            batch=self._batch,
            group=pyglet.graphics.OrderedGroup(2, parent=self._group),
            border_width=self.border_width
        )
        self._border.set_pos(
            x=case_x + self._gui_x,
            y=self.y + self._gui_y,
            width=self.height,
            height=self.height,
        )
        self._border.set_color(self.border_color[:-1] + (self.border_color[-1] * self.opacity,))

        # Rebuild the tick
        self._tick.delete()
        self._tick = icon(
            batch=self._batch,
            group=pyglet.graphics.OrderedGroup(3, parent=self._group),
            line_width=4
        )
        self._tick.set_pos(
            x=case_x + self.tick_padding + self._gui_x,
            y=self.y + self.tick_padding + self._gui_y,
            width=self.height - self.tick_padding * 2,
            height=self.height - self.tick_padding * 2,
        )
        self._tick.set_color(self.tick_color[:-1])
        self._tick.set_opacity(self.tick_color[-1] * self.opacity)

        # Update the visual
        self._update_visual()

    def delete_element(self):
        """
        Remove the checkbox from the GUI
        """

        # Call the super method
        super(CheckBox, self).delete_element()

        # Destroy all graphical elements
        self._case.delete()
        self._tick.delete()
        self._border.delete()
        self._label.delete()
