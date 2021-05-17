from flying_object import FlyingObject




class Obstacle(FlyingObject):
    """An Obstacle"""
    def __init__(self, SPACE, x=100, y=100, x_vel=0, y_vel=0.25):
        self.SPACE = SPACE
        self.x = x
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.radius = 7


    def draw_me(self):
        STROKE_COLOR = (0.8, 0.8, 1.2)
        STROKE_WEIGHT = 3
        FILL_COLOR = 0

        stroke(*STROKE_COLOR)
        strokeWeight(STROKE_WEIGHT)

        point(0,0)
