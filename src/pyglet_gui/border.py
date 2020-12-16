import pyglet


class Border:
    """
    This class is a helper to build borders with 4 lines
    """

    def __init__(self, batch: pyglet.graphics.Batch, group: pyglet.graphics.Group, border_width: int):
        """
        Construct a new border with the default values
        """

        # Set all attributes
        self.x: float = 0
        self.y: float = 0
        self.width: float = 0
        self.height: float = 0

        self.color: tuple = (255, 255, 255, 0)
        self.border_width: int = border_width

        # Assign internal attributes
        self._batch: pyglet.graphics.Batch = batch
        self._group: pyglet.graphics.Group = group
        self._lines: list = [
            pyglet.shapes.Line(
                x=0,
                y=0,
                x2=0,
                y2=0,
                color=(255, 255, 255),
                width=self.border_width,
                batch=self._batch,
                group=self._group
            ),
            pyglet.shapes.Line(
                x=0,
                y=0,
                x2=0,
                y2=0,
                color=(255, 255, 255),
                width=self.border_width,
                batch=self._batch,
                group=self._group
            ),
            pyglet.shapes.Line(
                x=0,
                y=0,
                x2=0,
                y2=0,
                color=(255, 255, 255),
                width=self.border_width,
                batch=self._batch,
                group=self._group
            ),
            pyglet.shapes.Line(
                x=0,
                y=0,
                x2=0,
                y2=0,
                color=(255, 255, 255),
                width=self.border_width,
                batch=self._batch,
                group=self._group
            )
        ]

    # ----- Settings methods (To apply changes) -----

    def set_pos(self, x: float, y: float, width: float, height: float):
        """
        Set the border position
        """

        # Set the position attributes
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Update the lines

        # --- Top
        self._lines[0].x = self.x - self.border_width / 2
        self._lines[0].y = self.y + self.height
        self._lines[0].x2 = self.x + self.width + self.border_width / 2
        self._lines[0].y2 = self.y + self.height

        # --- Right
        self._lines[1].x = self.x + self.width
        self._lines[1].y = self.y + self.height - self.border_width / 2
        self._lines[1].x2 = self.x + self.width
        self._lines[1].y2 = self.y + self.border_width / 2

        # --- Bottom
        self._lines[2].x = self.x - self.border_width / 2
        self._lines[2].y = self.y
        self._lines[2].x2 = self.x + self.width + self.border_width / 2
        self._lines[2].y2 = self.y

        # --- Left
        self._lines[3].x = self.x
        self._lines[3].y = self.y + self.height - self.border_width / 2
        self._lines[3].x2 = self.x
        self._lines[3].y2 = self.y + self.border_width / 2

    def set_color(self, color: tuple):
        """
        Set the border color
        """

        # Set the color
        self.color = color

        # Update the lines
        for line in self._lines:
            line.color = self.color[:-1]
            line.opacity = self.color[-1]

    def delete(self):
        """
        Delete the border
        """

        for line in self._lines:
            line.delete()
