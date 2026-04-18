import stdio
import sys
import stddraw
from game_manager import Game_manager
from picture import Picture as pic

menu_img = pic("assets/menu_img.png")


class Score_Manager:

    def draw_game_over(self, width, height):
        # creates the gameover screen
        stddraw.clear()
        stddraw.picture(menu_img, width / 2, height / 2, width, height)
        stddraw.setPenColor(stddraw.WHITE)  # This creates a black background
        stddraw.setFontSize(40)
        stddraw.text(width / 2, height / 2, "GAME OVER")  # Prints Game Over text

    def draw_winner(self, width, height):
        stddraw.clear()
        stddraw.picture(menu_img, width / 2, height / 2, width, height)
        stddraw.setPenColor(stddraw.WHITE)  # This creates a black background
        stddraw.setFontSize(40)
        stddraw.text(width / 2, height / 2, "YOU ARE A WINNER")  # Prints WINNER text

    # 09/04/26: Dillan van Wyk: Fixed score positioning and added background box behind score
    def score_tracking(self, current_score, height):
        # Background box at top-left corner
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.filledRectangle(0, height - 40, 140, 40)

        # Player's current score is drawn
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.setFontSize(18)
        stddraw.text(70, height - 20, "Score: " + str(current_score))

    # 18/04/26: Dillan van Wyk: Created method to draw player lives at the top right of the window
    # 18/04/26: Dillan van Wyk: Updated method to be compatible with two players
    def draw_lives(self, lives, width, height, label="", x_offset=0):
        # Background box at top right of window is drawn
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.filledRectangle(width - 120 - x_offset, height - 40, 120, 40)

        # Remaining hearts are drawn
        stddraw.setPenColor(stddraw.RED)
        stddraw.setFontSize(18)
        hearts = "♥ " * lives
        stddraw.text(width - 60 - x_offset, height - 20, label + hearts)
