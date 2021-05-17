class FlyingObject:
    """Handles common behaviors for flying objects, such as debris and obstacle. Potential 
    extra classes can be extended from this class as well in future improvements"""
    def display(self):
        self.x = self.x + self.x_vel
        self.y = self.y + self.y_vel

        self.position_and_draw(self.x, self.y)

        # Calculate rotation for objects that have a rot_vel attribute

    def position_and_draw(self, x, y):
        translate(x, y)

        self.draw_me()
        translate(-x, -y)
