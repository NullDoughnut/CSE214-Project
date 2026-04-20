import stdio
import sys
import stddraw
from game_manager import Game_manager


# 20/04/26: Dillan van Wyk: Reworked the way scores are calculated and added functionality to track session high score. Added register_points and reset methods
#                           and reworked score_tracking into draw_score
class Score_Manager:
    def __init__(self):
        self.current_score = 0
        self.high_score = 0

    def register_points(self, points):
        self.current_score += points
        if self.current_score > self.high_score:
            self.high_score = self.current_score

    def reset(self):
        self.current_score = 0

    def draw_score(self, width, height):
        # Background box at top-left corner
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.filledRectangle(0, height - 40, 280, 40)

        # Player's current score is drawn
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.setFontSize(18)
        stddraw.text(70, height - 20, "Score: " + str(self.current_score))

        # Session's high score is drawn next to player's current score
        stddraw.text(200, height - 20, "High: " + str(self.high_score))

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
