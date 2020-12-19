import pyglet


class Icon:
    """
    General class for all icons in the pyglet_gui lib
    """

    def __init__(self, batch: pyglet.graphics.Batch, group: pyglet.graphics.Group):
        """
        Create an icon with the default parameters

        params :
            - batch: pyglet.graphics.Batch = The batch to draw the icon in
            - group: pyglet.graphics.Group = The group that the icon belongs to
        """

        # Set the personalisation attributes
        self.x: int = 0
        self.y: int = 0
        self.width: int = 20
        self.height: int = 20
        self.color: tuple = (255, 255, 255)
        self.opacity: int = 255

        # Assign the intern attributes
        self._batch = batch
        self._group = group

    # ----- Setters -----

    def set_pos(self, x: int, y: int, width: int, height: int):
        """
        Set the position and the size of the icon

        params :
            - x: int = The new x position of the icon
            - y: int = The new y position of the icon
            - width: int = The new width of the icon
            - height: int = The new height of the icon
        """

        # Update attributes
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def set_color(self, color: tuple):
        """
        Set the icon color

        params :
            - color: tuple = The new icon's color
        """

        # Update the attribute
        self.color = color

    def set_opacity(self, opacity: int):
        """
        Set the icon opacity

        params :
            - opacity: int = The new icon opacity
        """

        # Update the attribute
        self.opacity = opacity

    def delete(self):
        """
        Delete the icon
        """

        pass


class Cross(Icon):
    """
    This class represent an icon cross
    """

    def __init__(self, batch: pyglet.graphics.Batch, group: pyglet.graphics.Group, **kwargs):
        """
        Create a new cross with the default parameters
        """

        # Call the super constructor
        super().__init__(batch, group)

        # Assign the specific customisation attributes
        self.line_width: int = kwargs.get("line_width", 4)

        # Assign the specific intern attributes
        self._line1: pyglet.shapes.Line = pyglet.shapes.Line(
            x=0,
            y=0,
            x2=0,
            y2=0,
            width=self.line_width,
            color=self.color,
            batch=self._batch,
            group=self._group
        )
        self._line1.opacity = self.opacity

        self._line2: pyglet.shapes.Line = pyglet.shapes.Line(
            x=0,
            y=0,
            x2=0,
            y2=0,
            width=self.line_width,
            color=self.color,
            batch=self._batch,
            group=self._group
        )
        self._line2.opacity = self.opacity

    # ----- Setters -----

    def set_pos(self, x: int, y: int, width: int, height: int):
        """
        Set the cross pos and size
        """

        # Call the super method
        super(Cross, self).set_pos(x, y, width, height)

        # Set the line 1 position
        self._line1.x = self.x
        self._line1.y = self.y
        self._line1.x2 = self.x + self.width
        self._line1.y2 = self.y + self.height

        # Set the line 2 position
        self._line2.x = self.x
        self._line2.y = self.y + self.height
        self._line2.x2 = self.x + self.width
        self._line2.y2 = self.y

    def set_color(self, color: tuple):
        """
        Set the cross color
        """

        # Call the super method
        super(Cross, self).set_color(color)

        # Set the lines color
        self._line1.color = self.color
        self._line2.color = self.color
        
    def set_opacity(self, opacity: int):
        """
        Set the cross opacity
        """
        
        # Call the super method
        super(Cross, self).set_opacity(opacity)

        # Set the lines opacity
        self._line1.opacity = opacity
        self._line2.opacity = opacity

    def delete(self):
        """
        Delete the cross
        """

        # Delete graphical elements
        self._line1.delete()
        self._line2.delete()


class Square(Icon):
    """
    This class represent an icon square
    """

    def __init__(self, batch: pyglet.graphics.Batch, group: pyglet.graphics.Group, **kwargs):
        """
        Create a new square with the default parameters
        """

        # Call the super method
        super().__init__(batch, group)

        # Assign the internal attributes
        self._square: pyglet.shapes.Rectangle = pyglet.shapes.Rectangle(
            x=0,
            y=0,
            width=0,
            height=0,
            color=self.color,
            batch=self._batch,
            group=self._group
        )

    # ----- Setters -----

    def set_pos(self, x: int, y: int, width: int, height: int):
        """
        Set the square position and size
        """

        # Call the super method
        super(Square, self).set_pos(x, y, width, height)

        # Set the shape parameters
        self._square.x = self.x
        self._square.y = self.y
        self._square.width = self.width
        self._square.height = self.height

    def set_color(self, color: tuple):
        """
        Set the square color
        """

        # Call the super method
        super(Square, self).set_color(color)

        # Set the shape color
        self._square.color = self.color

    def set_opacity(self, opacity: int):
        """
        Set the square opacity
        """

        # Call the super method
        super(Square, self).set_opacity(opacity)

        # Set the square opacity
        self._square.opacity = self.opacity

    def delete(self):
        """
        Delete the square
        """

        # Delete the shape
        self._square.delete()
