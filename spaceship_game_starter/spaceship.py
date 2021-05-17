from flying_object import FlyingObject
from debris import Debris
import math




class Spaceship(FlyingObject, object):
    """A spaceship"""
    
    
    def __init__(self, SPACE):
        self.intact = True
        self.SPACE = SPACE
        self.x = self.SPACE['w']/2
        self.y = self.SPACE['w']/2
        self.x_vel = 0
        self.y_vel = 0
        self.rotation = 0.0
        self.rotation_speed_factor = 5
        self.tip_point = (0, 6)
        self.port_corner_point = (-3.2, 2)
        self.starboard_corner_point = (3.2, 2)
        # the above three params are for drawing the triangle shaped spaceship
        self.radius = 7

    def control(self, keycode, gc=None):
        """Handle keyboard operations on the spaceship"""
        if keycode == UP:
            self.y = self.y - 3
        if keycode == RIGHT:
            self.x = self.x + 3
        if keycode == LEFT:
            self.x = self.x - 3
        if keycode == DOWN:
            self.y= self.y + 3
        
    def blow_up(self, fade):
        """Blow up the spaceship and performs the animation of spaceship blowing
        up into debris pieces"""
        
        self.debris = [
            # Portside debris piece
            Debris(self.SPACE, self.rotation,
                   self.port_corner_point, self.tip_point,
                   self.x, self.y,
                   # Direction debris will fly
                   math.sin(math.radians(self.rotation-45))/3,
                   - math.cos(math.radians(self.rotation-45))/3,
                   self.radius, fade),
            # Starboardside debris piece
            Debris(self.SPACE, self.rotation,
                   self.tip_point, self.starboard_corner_point,
                   self.x, self.y,
                   # Direction debris will fly
                   math.sin(math.radians(self.rotation+45))/2.7,
                   - math.cos(math.radians(self.rotation+45))/3.0,
                   self.radius, fade),
            # Stern debris piece
            Debris(self.SPACE, self.rotation,
                   self.port_corner_point, self.starboard_corner_point,
                   self.x, self.y,
                   # Direction debris will fly
                   math.sin(math.radians(self.rotation+180))/3.5,
                   - math.cos(math.radians(self.rotation+180))/3.7,
                   self.radius, fade)]
        self.intact = False

    def display(self):
        """Overrides the FlyingObject display method"""
        if self.intact:
            super(Spaceship, self).display()
        else:
            for piece in self.debris:
                piece.display()

    def draw_me(self):
        """Sets Processing values and calls draw functionality"""
        CYAN = (0, 1.0, 1.0)
        STROKE_WEIGHT = 3
        fill(0)
        strokeWeight(STROKE_WEIGHT)
        stroke(*CYAN)
        self.draw_ship()

    def draw_ship(self):
        """Draws the spaceship triangle"""
        triangle(*
                 (
                    self.port_corner_point +
                    self.tip_point +
                    self.starboard_corner_point
                    )
                 )

   
