import pyglet


class UIElement:
    """
    This class is the base class for all UI elements. This is here to factorize code
    """

    def __init__(
            self,
            x: int = 0,
            y: int = 0,
            width: int = 0,
            height: int = 0
    ):
        """
        Create a new ui element with the basic parameters

        params :
            - x: int = The element's x position, relative to the GUI position
            - y: int = The element's y position, relative to the GUI position
            - width: int = The element's width
            - height: int = The element's height
        """
        # Assign attributes
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        self.opacity: float = 1.0

        self._batch: pyglet.graphics.Batch = None
        self._group: pyglet.graphics.Group = None
        self._gui_x: int = 0
        self._gui_y: int = 0

    # ----- Event handling methods -----

    def on_mouse_move(self, x: int, y: int):
        """
        Handle the event when the mouse move in the GUI
        """

        pass

    def on_mouse_drag(self, x: int, y: int, button: int, mod: int):
        """
        Handle the event of a mouse drag
        """

        pass

    def on_mouse_press(self, x: int, y: int, button: int, mod: int):
        """
        Handle the event of a mouse click press
        """

        pass

    def on_mouse_release(self, x: int, y: int, button: int, mod: int):
        """
        Handle the event of a mouse click release
        """

        pass

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        """
        Handle the event of a mouse scroll
        """

        pass

    # ----- General element methods -----

    def create_element(self, gui):
        """
        Add the ui element to the parent GUI

        params :
            - gui : The parent GUI
        """

        # Assign the gui attributes
        self._batch = gui.get_batch()
        self._group = gui.get_group()
        self._gui_x = gui.get_pos()[0]
        self._gui_y = gui.get_pos()[1]

    def rebuild(self, gui):
        """
        Rebuild the element with the new state of the gui

        params :
            - gui : The parent GUI
        """

        # Reassign the gui position
        self._gui_x = gui.get_pos()[0]
        self._gui_y = gui.get_pos()[1]

    def delete_element(self):
        """
        Delete all element parts from the batch
        """

        pass
