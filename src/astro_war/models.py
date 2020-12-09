# different models for the game
import math
import copy
import pyglet

from src.astro_war.client.resources_manager import ResourcesManager


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
    missile_sprite = None #missile sprite, given with the color in the futur (if blue, then missile is blue)

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
        self.cannon = self.sprite.width/2  # find the formula, certainly (self.x+lenght(skin))/2 if the cannon is centred
        self.missile = []



    def shoot(self):
        """
        create a Missile
        """
        if (self.power == "laser"):  # if we have a power that modifies the shoot
            # shoot laser
            self.power = None
        else:  # if we use a normal shoot
            # for the self.y, we will have to change with the orientation, need the images to predict the formula
            # x′=(x−p) cos(θ)−(y−q) sin(θ) + p,
            # y′= (x−p) sin(θ) + (y−q) cos(θ) + q. #306 = primary location with anchor
            base_x = self.sprite.x - self.sprite.width / 2
            base_y = self.sprite.y + self.sprite.height / 2
            self.missile.append(Missile(base_x, base_y, self.orientation, self.color, self.sprite.x, self.sprite.y))



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
    sprite = None

    move = 1  # we move 1 pix by 1 pix

    def __init__(self, x, y, orientation, color,p,q):
        """
        create a missile, given initial coord, an orientation to go straight and a color to identify enemies
        """

        self.sprite = pyglet.sprite.Sprite(ResourcesManager.MISSILE_IMG)
        self.sprite.rotation = orientation
        self.orientation = orientation
        self.color = color
        self.speed = None  # will be a variable base_speed

        base_x = x + self.sprite.width/2
        base_y = y
        xcoord = (base_x - p) * math.cos(math.radians(-self.orientation)) - (base_y - q) * math.sin(
            math.radians(-self.orientation)) + p
        ycoord = (base_x - p) * math.sin(math.radians(-self.orientation)) + (
                    base_y - q) * math.cos(
            math.radians(-self.orientation)) + q

        self.sprite.x = xcoord
        self.sprite.y = ycoord

    def fly(self):
        """
        called regularly, the missile goes straight
        """
        self.sprite.y += self.move * math.cos(math.radians(self.orientation))
        self.sprite.x += self.move * math.sin(math.radians(self.orientation))
        print(self.orientation)
        # check here if we collide smth?


class Wall:
    """
    creates the wall as a whole or case/case?
    """
