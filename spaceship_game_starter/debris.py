import random
from flying_object import FlyingObject


class Debris(FlyingObject):
    """Debris of the spaceship after explosion. """
    def __init__(self, SPACE, rot,
                 endpoint1, endpoint2,
                 x, y, x_vel, y_vel,
                 radius, fadeout):
        self.SPACE = SPACE
        self.radius = radius
        self.endpoint1 = endpoint1
        self.endpoint2 = endpoint2
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.rot_vel = self.random_rot_vel()
        self.lifespan = fadeout
        self.fadeout = self.lifespan

    def draw_me(self):
        STROKE_WEIGHT = 3
        # Fade out stroke brightness
        if self.fadeout > 0:
            self.fadeout -= 1
            strokeWeight(STROKE_WEIGHT)
            stroke(
                0,
                (self.fadeout/self.lifespan),
                (self.fadeout/self.lifespan)
            )
            line(*(self.endpoint1 + self.endpoint2))

    def random_rot_vel(self):
        TWO = 2
        POINT_FIVE = 0.5
        return (random.random() * TWO) - POINT_FIVE
