import stdio
import sys
import stddraw
from game_manager import Game_manager


class Score_Manager:

    # 01/04/26: Denlan Molokwu: Created score tracking for when enemies are killed
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
