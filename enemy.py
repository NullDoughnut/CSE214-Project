import stddraw
from picture import Picture as pic
from projectile import Projectile


enemy_img = pic("assets/alien.png")
minions_img = pic("assets/spaceShips_002.png")


# 30/03/26: Luke Abrahamse: created enemy object
# 18/04/26: Dillan van Wyk: Moved from class attributes to instance attributes
# 23/04/26: Dillan van Wyk: Added enemy health and enemy health bars
class Enemy:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 15
        self.alive = True
        self.enemy_type = "alien"
        self.max_health = 2
        self.health = self.max_health

    # 09/04/26: Dillan van Wyk: Enemies are now pictures and no longer drawn
    def draw(self):  # draws enemy
        if self.alive:
            stddraw.picture(enemy_img, self.x, self.y, self.radius * 3, self.radius * 3)
            self.draw_health_bar()
        stddraw.setPenColor(stddraw.BLACK)

    # 09/04/26: Dillan van Wyk: Creates and returns a projectile that is fired downward. Enemy projectile is half the speed of player's
    def shoot(self):
        p = Projectile()
        p.x = self.x
        p.y = self.y - self.radius
        p.angle = 270
        p.speed = 10
        return p

    # 23/04/26: Dillan van Wyk: Added method to draw enemy health bar
    def draw_health_bar(self):
        if self.health == self.max_health:
            return
        else:
            bar_width = self.radius * 2.5
            bar_height = 4
            bar_x = self.x - bar_width / 2
            bar_y = self.y - self.radius * 2

            # Draws red background representing missing health
            stddraw.setPenColor(stddraw.RED)
            stddraw.filledRectangle(bar_x, bar_y, bar_width, bar_height)

            # Draws green over red background representing remaining health
            fill = bar_width * (self.health / self.max_health)
            stddraw.setPenColor(stddraw.GREEN)
            stddraw.filledRectangle(bar_x, bar_y, fill, bar_height)


# 15/04/26: Denlan: created minions class
# 18/04/26: Dillan van Wyk: Moved from class attributes to instance attributes
# 23/04/26: Dillan van Wyk: Added enemy health and enemy health bars
class Minions:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 15
        self.alive = True
        self.enemy_type = "minion"
        self.max_health = 2
        self.health = self.max_health

    def draw(self):  # draws minions
        if self.alive:
            stddraw.picture(
                minions_img, self.x, self.y, self.radius * 3, self.radius * 3
            )
            self.draw_health_bar()
        stddraw.setPenColor(stddraw.BLACK)

    # 19/04/26: Denlan: Implemented the fact minions can shoot back at increase speed each level
    def shoot(self):
        p = Projectile()
        p.speed = 12
        p.x = self.x
        p.y = self.y - self.radius
        p.angle = 270
        p.speed = p.speed * 1.3
        return p

    # 23/04/26: Dillan van Wyk: Added method to draw enemy health bar
    def draw_health_bar(self):
        if self.health == self.max_health:
            return
        else:
            bar_width = self.radius * 2.5
            bar_height = 4
            bar_x = self.x - bar_width / 2
            bar_y = self.y - self.radius * 2

            # Draws red background representing missing health
            stddraw.setPenColor(stddraw.RED)
            stddraw.filledRectangle(bar_x, bar_y, bar_width, bar_height)

            # Draws green over red background representing remaining health
            fill = bar_width * (self.health / self.max_health)
            stddraw.setPenColor(stddraw.GREEN)
            stddraw.filledRectangle(bar_x, bar_y, fill, bar_height)
