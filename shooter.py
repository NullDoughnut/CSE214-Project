import math, stddraw
from projectile import Projectile
from picture import Picture as pic

shooter_img = pic("assets/shooter.png")


# 30/03/26: Luke Abrahamse: Created Shooter Class. Added draw, move and rotate functions
# 18/04/26: Dillan van Wyk: Added shooter lives. Also moved from class attributes to instance attributes
# 18/04/26: Dillan van Wyk: Added colored circle at bottom of shooter in order to differentiate between players in co-op
class Shooter:
    def __init__(self):
        self.x = 300  # starting x coordinates
        self.y = 30  # starting y coordinate
        self.speed = 10  # movement speed
        self.angle = 90  # starting angle
        self.rotate_speed = 5  # rotation speed
        self.turret_length = 20
        self.radius = 15
        self.lives = 3
        self.color = stddraw.CYAN

    # 09/04/26: Dillan van Wyk: Added enhanced graphics (shooter.png)
    # 23/04/26: Dillan van Wyk: Added on_cooldown parameter so that the turrent can be turned red for when the shooter can't shoot
    def draw(self, on_cooldown=False):
        # Draw colored circle at the bottom of the shooter
        stddraw.setPenColor(self.color)
        stddraw.filledCircle(self.x, self.y - self.radius, self.radius * 0.5)

        # Draw shooter body
        stddraw.picture(
            shooter_img,
            self.x,
            self.y,
            self.radius * 3.5,
            self.radius * 3.5,
        )

        # Draw turret
        if on_cooldown:
            stddraw.setPenColor(stddraw.RED)
        else:
            stddraw.setPenColor(stddraw.YELLOW)
        stddraw.setPenRadius(0.01)
        stddraw.line(
            self.x,
            self.y,
            self.x + self.turret_length * math.cos(math.radians(self.angle)),
            self.y + self.turret_length * math.sin(math.radians(self.angle)),
        )
        stddraw.setPenRadius(0.0)

    def move_right(self):
        self.x += self.speed  # moves shooter to the right
        if self.x + self.radius > 600:  # checks to see if shooter is out of boundary
            self.x = 600 - self.radius

    def move_left(self):
        self.x -= self.speed  # moves shooter to the left
        if self.x - self.radius < 0:  # checks to see if shooter is out of boundary
            self.x = self.radius

    def rotate_right(self):
        if self.angle - self.rotate_speed >= 0:  # checks if shooter can rotate right
            self.angle -= self.rotate_speed  # rotates shooter right
        else:
            self.angle = 0

    def rotate_left(self):
        if self.angle + self.rotate_speed <= 180:  # checks if shooter can rotate left
            self.angle += self.rotate_speed  # rotates shooter left
        else:
            self.angle = 180

    # 31/02/26: Dillan van Wyk: Gave the shooter the ability to shoot projectiles
    def shoot(self):
        p = Projectile()

        # intializes the starting position and angle for the projectile
        p.x = self.x + self.turret_length * math.cos(math.radians(self.angle))
        p.y = self.y + self.turret_length * math.sin(math.radians(self.angle))
        p.angle = self.angle

        return p
