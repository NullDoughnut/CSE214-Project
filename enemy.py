import stddraw
from picture import Picture as pic

enemy_img = pic("assets/alien.png")


# 30/03/26: Luke Abrahamse: created enemy object
class Enemy:
    x = 0
    y = 0
    radius = 15
    alive = True

    # 09/04/26: Dillan van Wyk: enemies are now pictures and no longer drawn
    def draw(self):  # draws enemy
        if self.alive:
            stddraw.picture(enemy_img, self.x, self.y, self.radius * 3, self.radius * 3)
        stddraw.setPenColor(stddraw.BLACK)
