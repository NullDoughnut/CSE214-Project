import math, stddraw


class Shooter:
    x = 50  # starting x coordinates
    y = 5  # starting y coordinate
    speed = 2  # movement speed
    angle = 90  # starting angle
    rotate_speed = 5  # rotation speed
    turret_length = 5
    radius = 3

    def draw(self):  # draws shooters current position
        stddraw.filledCircle(
            self.x, self.y, self.radius
        )  # draws shooter body at current coordinate
        stddraw.setPenRadius(0.5)
        stddraw.line(
            self.x,
            self.y,
            self.x + self.turret_length * math.cos(math.radians(self.angle)),
            self.y + self.turret_length * math.sin(math.radians(self.angle)),
        )  # draws shooter turret at curent angle
        stddraw.setPenRadius(0.0)

    def move_right(self):
        self.x += self.speed  # moves shooter to the right
        if self.x + self.radius > 100:  # checks to see if shooter is out of boundary
            self.x = 100 - self.radius

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
