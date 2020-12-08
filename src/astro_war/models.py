# different models for the game
import math


class Ship:
    """
    The ship, controlled by player
    """
    # all the ship var

    # Coord (bottom left of the image)
    x = None
    y = None

    # All the coord that define the ship in function of x/y, for example if a ship is:
    #   1
    #  111
    # then hitboxes will be (0,3),(1,2)(1,3)(1,4)
    hitboxes = None

    # other var
    status = None  # status will be like 0 for dead, 1 for foetus, 2 for alive
    color = None
    orientation = None  # will decide the direction of ship/missiles
    power = None  # laser, blade, etc
    cannon = None  # coord of the cannon, calculated with orientation,x,y and the skin
    sprite = None

    # var for calc
    rotation = 1  # we turn 1 degree by 1 degree
    move = 1  # we move 1 pix by 1 pix

    def __init__(self, color, sprite):
        """
        Create a ship with coord to place it and a color (plus a sprite)
        No need coord, will work directly on sprite x and y
        """

        self.sprite = sprite
        self.hitboxes = None  # will depend of the image
        self.status = 2
        self.color = color
        self.orientation = 0  # didn't rotate yet
        self.cannon = None  # find the formula, certainly (self.x+lenght(skin))/2 if the cannon is centred



    def shoot(self):
        """
        create a Missile
        """
        if (self.power != "laser"):  # if we have a power that modifies the shoot
            # shoot laser
            self.power = None
        else:  # if we use a normal shoot
            # for the self.y, we will have to change with the orientation, need the images to predict the formula
            M = Missile(self.cannon, self.y, self.orientation, self.color)

    def rotateLeft(self):  # will be called while player press the button
        """
        the ship turn to the left
        """

        self.sprite.rotation -= self.rotation

        self.orientation -= self.rotation

    def rotateRight(self):
        """
        the sihip turn to the right
        """
        self.sprite.rotation += self.rotation

        self.orientation += self.rotation

    def fly(self):
        """
        called regularly, the ship goes straight
        """
        self.sprite.y += self.move * math.cos(math.radians(self.orientation))
        self.sprite.x += self.move * math.sin(math.radians(self.orientation))
        # check here if we collide smth?

    def powered(self, power):
        """
        get a power
        """
        self.power = power

    def getshot(self):
        if self.status == 1:
            self.status = 0
        else:
            self.status = 1  # if we are dead we can't get shot, and just add an 'if' if we have a power like a shield


class Missile:
    """
    a missile, object that goes in straight line with decreasing speed
    """

    # base coord
    x = None
    y = None
    orientation = None
    speed = None  # will decrease in time
    color = None  # will decide which ship to destroy

    def __init__(self, x, y, orientation, color):
        """
        create a missile, given initial coord, an orientation to go straight and a color to identify enemies
        """

        self.x = x
        self.y = y
        self.orientation = orientation
        self.color = color
        self.speed = None  # will be a variable base_speed

    def fly(self):
        """
        called regularly, the missile goes straight
        """
        self.x = self.move * math.cos(math.radians(self.orientation))  # check formula with visual
        self.y = self.move * math.sin(math.radians(self.orientation))
        # check here if we collide smth?


class Wall:
    """
    creates the wall as a whole or case/case?
    """
