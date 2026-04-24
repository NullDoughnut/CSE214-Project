import stddraw
from picture import Picture as pic

# 19/04/2026 Denlan Molokwu: Created a bunker class that creates bunkers for the game

bunker_img1 = pic(
    "assets/FullyBroken.png"
)  # importing pictures of asteroids to use as "Bunkers"
bunker_img2 = pic("assets/Phase2.png")
bunker_img3 = pic("assets/FullAsteroid.png")


class Bunker:
    x = 0  # initialize coordinates of bunker
    y = 0
    width = 60  # initialize size of bunker
    height = 30
    health = 5  # Allows bunker to take 5 hits before ultimately getting destroyed
    alive = True  # Initialize a variable Alive so that if bunker is destroyed bunker does not affect gameplay

    def draw(self):
        if self.alive == True:
            centre_x = self.x + (
                self.width / 2
            )  # created these coordinates because pictures are generated from centre
            centre_y = self.y + (self.height / 2)
            if self.health > 3:
                stddraw.picture(
                    bunker_img3, centre_x, centre_y, self.width, self.height
                )  # implemented different png's of the asteroids if they went below certain health
            elif self.health > 2:
                stddraw.picture(
                    bunker_img2, centre_x, centre_y, self.width, self.height
                )
            else:
                stddraw.picture(
                    bunker_img1, centre_x, centre_y, self.width, self.height
                )
