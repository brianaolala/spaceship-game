from obstacle import Obstacle
from spaceship import Spaceship
import random




class GameController:
    """
    Manages the game and combines different components altogethers. Continuously
    updates the obstacles, score, and difficulty level. Detects spaceship motions as well.
    """

    def __init__(self, SPACE, fadeout):
        """Initialize the game controller"""
        self.score = 0
        self.SPACE = SPACE
        self.fadeout = fadeout
        # when hit an obstacle
        self.spaceship_hit = False
        self.visited = []
        self.obstacles = [Obstacle(self.SPACE)]
        self.difficulty = 10
        self.spaceship = Spaceship(self.SPACE)
        self.time = 100        
        
    def add_obstacle(self):
        """add random obstacles and controls the difficulty by adjusting the probability
        of generating one obstacle"""
        if (self.time == 0):
            num = random.randint(0, self.difficulty)
            if (num == 1):
                x = random.randint(0, 600)
                new_obstacle = Obstacle(self.SPACE, x=x, y=0)
                self.obstacles.append(new_obstacle)
        else:
            self.time = self.time - 1
                  
    def display_score(self):
        textSize(20)
        fill(1)
        text("SCORE: " + str(self.score), 50, 500)
        
    
    def display_difficulty(self):
        if (self.difficulty == 10):
            text('Difficulty Level: Easy', 50, 520)
        elif (self.difficulty == 6):
            text('Difficulty Level: Medium', 50, 520)
        elif (self.difficulty == 2):
            text('Difficulty Level: Hard', 50, 520)
        textSize(12)
        text("Press SHIFT to switch level", 50, 535)
            
    def update(self):
        """Updates game state on every frame, including score, difficulty level,
        intersection between spaceship and any obstacle, and adding new obstacles."""
        self.display_score()
        self.display_difficulty()
        self.do_intersections()
        self.add_obstacle()     
        for obstacle in self.obstacles:
            obstacle.display()        
        self.spaceship.display()
        if self.spaceship_hit:
            # if spaceship hit an obstacle
            if self.fadeout <= 0:
                fill(1)
                textSize(30)
                text("YOU HIT AN ASTEROID",
                     self.SPACE['w']/2 - 165, self.SPACE['h']/2)
            else:
                self.fadeout -= 1

    def handle_keypress(self, key, keycode=None):
        if (keycode == SHIFT):
            if(self.difficulty > 2):
                self.difficulty -= 4
            elif(self.difficulty == 2):
                self.difficulty = 10
        if (key == ' '):
            if self.spaceship.intact:
                self.spaceship.control(' ', self)
        if (keycode):
            if self.spaceship.intact:
                self.spaceship.control(keycode)

    def do_intersections(self):
        """ function that handels the situation when beams hit the asteroids"""

        if self.spaceship.intact:
            # Check each obstacle for intersection

            for obstacle in self.obstacles:
                if (obstacle.y > 610):
                    self.obstacles.remove(obstacle)
                if (self.spaceship.y < obstacle.y and (obstacle not in self.visited)):
                    self.visited.append(obstacle)
                    self.score += 1
                    # increments score by how many obstacles that the player has successfully avoided
                if (
                    abs(self.spaceship.x - obstacle.x)
                    < max(obstacle.radius,
                          self.spaceship.radius)
                    and
                    abs(self.spaceship.y - obstacle.y)
                    < max(obstacle.radius,
                          self.spaceship.radius)):
                    self.spaceship.blow_up(self.fadeout)
                    self.spaceship_hit = True
            
