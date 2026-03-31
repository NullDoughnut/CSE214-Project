import stdio
import sys
import stddraw




class Score_Manager:

    def draw_game_over(self,width,height):
    #creates the gameover screen
        stddraw.clear(stddraw.BLACK)
        stddraw.setPenColor(stddraw.WHITE)  #This creates a black background
        stddraw.setFontSize(40)
        stddraw.text(width/2, height / 2, "GAME OVER")  #Prints Game Over text

        
    def draw_winner(self, width, height):
        stddraw.clear(stddraw.BLACK)
        stddraw.setPenColor(stddraw.WHITE)  #This creates a black background
        stddraw.setFontSize(40)
        stddraw.text(width/2, height / 2, "YOU ARE A WINNER")  #Prints WINNER text

        



 
