import stddraw
import math


# 31/03/26: Dillan van Wyk: Made the Projectile class and the move() and draw() functions
class Projectile:
    x = 0
    y = 0
    angle = 90
    speed = 15
    radius = 5
    alive = True

    def move(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))

    def draw(self):
        stddraw.setPenColor(stddraw.WHITE)
        if self.alive:
            stddraw.filledCircle(self.x, self.y, self.radius)
