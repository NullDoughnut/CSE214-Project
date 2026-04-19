import stddraw
from picture import Picture as pic

RF_IMG = pic("assets/rapid_fire.png")
MS_IMG = pic("assets/multi_shot.png")
ONEUP_IMG = pic("assets/extra_life.png")

# 19/04/2026 Luke Abrahamse: Created PowerUp class

class PowerUp:
    def __init__(self, x, y, powerup_type):
        self.x = x
        self.y = y
        self.powerup_type = powerup_type
        self.radius = 15
        self.speed = 3
        self.alive = True

    def move(self):
        self.y -= self.speed

    def draw(self): # Draws PowerUp Icon
        if self.alive:
            icon = RF_IMG
            if self.powerup_type == "multi_shot":
                icon = MS_IMG
            elif self.powerup_type == "extra_life":
                icon = ONEUP_IMG
            stddraw.picture(icon, self.x, self.y, self.radius*2, self.radius*2)
