import stddraw
from picture import Picture as pic

#19/04/2026 Denlan Molokwu: Created a bunker class that creates bunkers for the game

bunker_img = pic("assets/Bunker.png")

class Bunker:
    x = 0
    y = 0
    width = 60
    height = 30
    health = 5
    alive = True
    def draw(self):
        if self.alive == True:
            if self.health > 3:
                stddraw.setPenColor(stddraw.GREEN)
            elif self.health > 2:
                stddraw.setPenColor(stddraw.YELLOW)
            else:
                stddraw.setPenColor(stddraw.RED)
            stddraw.filledRectangle(self.x,self.y,self.width,self.height)


