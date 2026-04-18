import stddraw
import math
from audio_manager import Audio_Manager

audio = Audio_Manager()


# 31/03/26: Dillan van Wyk: Added function to check for collisions and implemented it
def collision(projectile, enemy):
    dx = projectile.x - enemy.x
    dy = projectile.y - enemy.y
    distance = (dx**2 + dy**2) ** 0.5
    return distance <= (enemy.radius + projectile.radius)


# 31/03/26: Dillan van Wyk: Made the Projectile class and the move() and draw() functions
# 18/04/26: Dillan van Wyk: Moved from class attributes to instance attributes
class Projectile:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 90
        self.speed = 15
        self.radius = 5
        self.alive = True

    def move(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))

    def draw(self):
        stddraw.setPenColor(stddraw.WHITE)
        if self.alive:
            stddraw.filledCircle(self.x, self.y, self.radius)


# 31/03/26: Dillan van Wyk: Created the Project_Manager class to contain and manage functions related to projectiles [update(), draw(), shoot()]
# 18/04/26: Dillan van Wyk: Moved from class attributes to instance attributes
class Projectile_Manager:
    def __init__(self):
        self.projectiles = []
        self.max_cooldown = 15
        self.cooldown = 0

    def update(self, x_min, x_max, y_min, y_max, enemies):
        if self.cooldown > 0:
            self.cooldown -= 1

        # Projectile collisions with enemy removes that enemy
        for p in self.projectiles[:]:
            for e in enemies:
                if e.alive and collision(p, e):
                    e.alive = False
                    self.projectiles.remove(p)
                    break

        # Projectile off-screen removal and movement of projectiles
        for p in self.projectiles[:]:
            if (p.x < x_min or p.x > x_max) or (p.y < y_min or p.y > y_max):
                self.projectiles.remove(p)
            else:
                p.move()

    # Draw projectiles
    def draw(self):
        for p in self.projectiles:
            p.draw()

    # Allows shooter to shoot projectiles
    def shoot(self, shooter):
        if self.cooldown == 0:
            self.projectiles.append(shooter.shoot())
            self.cooldown = self.max_cooldown
            audio.play_tone(4400, 0.1)
