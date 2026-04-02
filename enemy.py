import stddraw

# 30/03/26: Luke Abrahamse: created enemy object 
class Enemy:
    x = 0
    y = 0
    radius = 15
    alive = True

    def draw(self): # draws enemy
        stddraw.setPenColor(stddraw.RED)
        if self.alive:
            stddraw.filledCircle(self.x, self.y, self.radius)
        stddraw.setPenColor(stddraw.BLACK)
