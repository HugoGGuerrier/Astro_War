from .ui_element import UIElement
from .border import Border

import pyglet
from pyglet.window import mouse


class Slider(UIElement):
    """
    This class represent a slider to select a value between 2 other values
    """

    def __init__(self):
        """
        Create a slider with the default parameters
        """

        # Call the super constructor
        super().__init__(0, 0, 400, 40)

        # Set all customization attributes
        self.min_value: float = 0
        self.max_value: float = 1
        self.init_value: float = 0.5

        self.cursor_width: int = 20
        self.cursor_color: tuple = (95, 95, 95, 255)
        self.cursor_hover: tuple = (95, 95, 168, 255)
        self.cursor_press: tuple = (60, 60, 60, 255)

        self.border_color: tuple = (255, 255, 255, 255)
        self.border_hover: tuple = None
        self.border_press: tuple = None
        self.border_width: int = 4

        self.bar_width: int = 5
        self.empty_color: tuple = (255, 255, 255, 100)
        self.full_color: tuple = (255, 255, 255, 255)
        self.show_bar_under_cursor: bool = False

        self.on_value_change = None

        # Assign the internal attributes
        self._cursor: pyglet.shapes.Rectangle = None
        self._border: Border = None
        self._empty: pyglet.shapes.Line = None
        self._full: pyglet.shapes.Line = None
        self._value: float = self.init_value
        self._gui_x: int = 0
        self._gui_y: int = 0

        self._is_hovered: bool = False
        self._is_pressed: bool = False

    # ----- Internal methods -----

    def _get_cursor_x(self) -> float:
        """
        Get the current cursor position by computing the value

        return -> int = The cursor x position relative to the slider origin
        """

        coef = (self._value - self.min_value) / (self.max_value - self.min_value)
        return (self.width * coef) + self.x - self.cursor_width / 2

    def _is_on_cursor(self, x: int, y: int) -> bool:
        """
        Get if the mouse is on the slider cursor

        params :
            - x: int = The mouse x position
            - y: int = The mouse y position

        return -> bool = If the mouse is on the cursor
        """

        cursor_x = self._get_cursor_x()
        return (cursor_x <= x <= cursor_x + self.cursor_width + self.border_width) and\
               (self.y - self.border_width <= y <= self.y + self.height)

    def _update_visual(self):
        """
        Update the slider visual with the current value
        """

        # Compute the new position
        cursor_x = self._get_cursor_x()

        stop_full_x = cursor_x - self.border_width / 2
        stop_empty_x = cursor_x + self.cursor_width + self.border_width / 2
        if self.show_bar_under_cursor:
            stop_full_x = cursor_x + self.cursor_width / 2
            stop_empty_x = stop_full_x

        # Update the cursor position
        self._cursor.x = cursor_x + self._gui_x

        # Update the border position
        self._border.set_pos(
            x=cursor_x + self._gui_x,
            y=self._border.y,
            width=self._border.width,
            height=self._border.height
        )

        # Update the full and empty
        self._full.x2 = stop_full_x + self._gui_x
        self._empty.x = stop_empty_x + self._gui_x

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
        if self._exists:
            self._update_visual()

        # Call the function
        if self.on_value_change is not None:
            self.on_value_change(self._value)

    # ----- Event handling methods -----

    def on_mouse_move(self, x: int, y: int):
        """
        Check the mouse move to make the hover effect
        """

        if not self._is_pressed:

            if self._is_on_cursor(x, y):

                # Set the hovered state to true
                self._is_hovered = True

                # Change the cursor color
                if self.cursor_hover is not None:
                    self._cursor.color = self.cursor_hover[:-1]
                    self._cursor.opacity = self.cursor_hover[-1] * self.opacity

                # Change the border color
                if self.border_hover is not None:
                    self._border.set_color(self.border_hover[:-1] + (self.border_hover[-1] * self.opacity,))

            else:

                # Set the hovered state to false
                self._is_hovered = False

                # Reset the cursor color
                if self.cursor_hover is not None:
                    self._cursor.color = self.cursor_color[:-1]
                    self._cursor.opacity = self.cursor_color[-1] * self.opacity

                # Reset the border color
                if self.border_hover is not None:
                    self._border.set_color(self.border_color[:-1] + (self.border_color[-1] * self.opacity,))

        else:

            # Get the coef for the current mouse x
            coef = (x - self.x) / (self.x + self.width - self.x)
            coef = max(min(coef, 1.0), 0.0)

            # Update the current value
            self._value = (coef * (self.max_value - self.min_value)) + self.min_value

            # Update the visual
            self._update_visual()

            # Call the function
            if self.on_value_change is not None:
                self.on_value_change(self._value)

    def on_mouse_drag(self, x: int, y: int, button: int, mod: int):
        # Just do the same as mouse move
        self.on_mouse_move(x, y)

    def on_mouse_press(self, x: int, y: int, button: int, mod: int):
        """
        Handle the mouse click
        """

        if button & mouse.LEFT:

            if self._is_hovered:

                # Set the pressed state to true
                self._is_pressed = True

                # Change the cursor color
                if self.cursor_press is not None:
                    self._cursor.color = self.cursor_press[:-1]
                    self._cursor.opacity = self.cursor_press[-1] * self.opacity

                # Change the border color
                if self.border_press is not None:
                    self._border.set_color(self.border_press[:-1] + (self.border_press[-1] * self.opacity,))

    def on_mouse_release(self, x: int, y: int, button: int, mod: int):
        """
        Handle the click end
        """

        if button & mouse.LEFT:

            if self._is_pressed:

                # Set the pressed state to false and update the widget state
                self._is_pressed = False
                self.on_mouse_move(x, y)

    # ----- Element methods -----

    def create_element(self, gui):
        """
        Create the slider in the gui

        params :
            - gui = The GUI to create the slider in
        """

        # Call the super method
        super(Slider, self).create_element(gui)

        # Get the computed position
        cursor_x = self._get_cursor_x() + self.x

        stop_full_x = cursor_x - self.border_width / 2
        stop_empty_x = cursor_x + self.cursor_width + self.border_width / 2
        if self.show_bar_under_cursor:
            stop_full_x = cursor_x + self.cursor_width / 2
            stop_empty_x = stop_full_x

        # Create the cursor
        self._cursor = pyglet.shapes.Rectangle(
            x=cursor_x + self._gui_x,
            y=self.y + self._gui_y,
            width=self.cursor_width,
            height=self.height,
            color=self.cursor_color[:-1],
            batch=self._batch,
            group=pyglet.graphics.OrderedGroup(1, parent=self._group)
        )
        self._cursor.opacity = self.cursor_color[-1] * self.opacity

        # Create the cursor border
        self._border = Border(
            batch=self._batch,
            group=pyglet.graphics.OrderedGroup(2, self._group),
            border_width=self.border_width
        )
        self._border.set_pos(
            x=cursor_x + self._gui_x,
            y=self.y + self._gui_y,
            width=self.cursor_width,
            height=self.height
        )
        self._border.set_color(self.border_color[:-1] + (self.border_color[-1] * self.opacity,))

        # Create the before line
        self._full = pyglet.shapes.Line(
            x=self.x + self._gui_x,
            y=self.y + self.height / 2 + self._gui_y,
            x2=stop_full_x + self._gui_x,
            y2=self.y + self.height / 2 + self._gui_y,
            color=self.full_color[:-1],
            width=self.bar_width,
            batch=self._batch,
            group=pyglet.graphics.OrderedGroup(0, self._group)
        )
        self._full.opacity = self.full_color[-1] * self.opacity

        # Create the after line
        self._empty = pyglet.shapes.Line(
            x=stop_empty_x + self._gui_x,
            y=self.y + self.height / 2 + self._gui_y,
            x2=self.x + self.width + self._gui_x,
            y2=self.y + self.height / 2 + self._gui_y,
            color=self.empty_color[:-1],
            width=self.bar_width,
            batch=self._batch,
            group=pyglet.graphics.OrderedGroup(0, self._group)
        )
        self._empty.opacity = self.empty_color[-1] * self.opacity

    def rebuild(self, gui):
        """
        Rebuild the slider with the new GUI state

        params :
            - gui = The GUI
        """

        # Call the super methods
        super(Slider, self).rebuild(gui)

        # Get the computed position
        cursor_x = self._get_cursor_x() + self.x

        stop_full_x = cursor_x - self.border_width / 2
        stop_empty_x = cursor_x + self.cursor_width + self.border_width / 2
        if self.show_bar_under_cursor:
            stop_full_x = cursor_x + self.cursor_width / 2
            stop_empty_x = stop_full_x

        # Rebuild the cursor
        self._cursor.x = cursor_x + self._gui_x
        self._cursor.y = self.y + self._gui_y
        self._cursor.width = self.cursor_width
        self._cursor.height = self.height
        self._cursor.color = self.cursor_color[:-1]
        self._cursor.opacity = self.cursor_color[-1]

        # Rebuild the border
        self._border.delete()
        self._border = Border(
            batch=self._batch,
            group=pyglet.graphics.OrderedGroup(2, parent=self._group),
            border_width=self.border_width
        )
        self._border.set_pos(
            x=cursor_x + self._gui_x,
            y=self.y + self._gui_y,
            width=self.cursor_width,
            height=self.height
        )
        self._border.set_color(self.border_color[:-1] + (self.border_color[-1] * self.opacity,))

        # Rebuild the before line
        self._full.delete()
        self._full = pyglet.shapes.Line(
            x=self.x + self._gui_x,
            y=self.y + self.height / 2 + self._gui_y,
            x2=stop_full_x + self._gui_x,
            y2=self.y + self.height / 2 + self._gui_y,
            color=self.full_color[:-1],
            width=self.bar_width,
            batch=self._batch,
            group=pyglet.graphics.OrderedGroup(0, self._group)
        )
        self._full.opacity = self.full_color[-1] * self.opacity

        # Rebuild the after line
        self._empty.delete()
        self._empty = pyglet.shapes.Line(
            x=stop_empty_x + self._gui_x,
            y=self.y + self.height / 2 + self._gui_y,
            x2=self.x + self.width + self._gui_x,
            y2=self.y + self.height / 2 + self._gui_y,
            color=self.empty_color[:-1],
            width=self.bar_width,
            batch=self._batch,
            group=pyglet.graphics.OrderedGroup(0, self._group)
        )
        self._empty.opacity = self.empty_color[-1] * self.opacity

    def delete_element(self):
        """
        Delete the element from the gui
        """
        
        # Call the super method
        super(Slider, self).delete_element()

        # Delete all graphical elements
        self._cursor.delete()
        self._border.delete()
        self._full.delete()
        self._empty.delete()
