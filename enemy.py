import stddraw
from picture import Picture as pic

enemy_img = pic("assets/alien.png")
minions_img = pic("assets/spaceShips_002.png")


# 30/03/26: Luke Abrahamse: created enemy object
# 18/04/26: Dillan van Wyk: Moved from class attributes to instance attributes
class Enemy:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 15
        self.alive = True
        self.enemy_type = "alien"

    # 09/04/26: Dillan van Wyk: enemies are now pictures and no longer drawn
    def draw(self):  # draws enemy
        if self.alive:
            stddraw.picture(enemy_img, self.x, self.y, self.radius * 3, self.radius * 3)
        stddraw.setPenColor(stddraw.BLACK)


# 15/04/26: Denlan: created minions class
# 18/04/26: Dillan van Wyk: Moved from class attributes to instance attributes
class Minions:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.radius = 15
        self.alive = True
        self.enemy_type = "minion"

    def draw(self):  # draws minions
        if self.alive:
            stddraw.picture(
                minions_img, self.x, self.y, self.radius * 3, self.radius * 3
            )
        stddraw.setPenColor(stddraw.BLACK)
