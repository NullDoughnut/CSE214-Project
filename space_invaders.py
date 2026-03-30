import stdio, stddraw
from shooter import Shooter
from game_manager import Game_manager

def main() -> None:
    ############ TITLE SCREEN ############
    #               LOG_1                #
    # name:     Dillan van Wyk           #
    # date:     26/02/26                 #
    # change:   set up the title screen  #
    ######################################

    ##$ I'D LIKE TO MOVE ALL OF THIS TO A DIFFERENT FILE WITH DIFFERENT CLASSES $##

    ### set up screen ###
    ## variables to make the program scaleable

    # x and y axis scales
    x_scale_min: int = 0
    y_scale_min: int = 0
    x_scale_max: int = 600
    y_scale_max: int = 600

    # canvas sizing
    ##$ maybe merge them into one variable calles canvas_size so that the canvas stays a square
    x_canvas: int = 500
    y_canvas: int = 500

    # font sizing
    main_title_font_size: float = 0.07
    subtitle_font_size: float = 0.05
    body_font_size: float = 0.04

    ## initializing the canvas
    stddraw.setCanvasSize(x_canvas, y_canvas)
    stddraw.setXscale(x_scale_min, x_scale_max)
    stddraw.setYscale(y_scale_min, y_scale_max)

    ### putting everything onto the canvas ###
    while True:
        stddraw.clear(stddraw.BLACK)
        stddraw.setPenColor(stddraw.WHITE)

        ## drawing all of the text onto the canvas
        stddraw.setFontSize(int(x_canvas * main_title_font_size))
        stddraw.text(
            (x_scale_min + x_scale_max) / 2,
            (y_scale_min + y_scale_max) * 18 / 20,
            "SPACE INVADERS",
        )

        stddraw.setFontSize(int(x_canvas * subtitle_font_size))
        stddraw.text(
            (x_scale_min + x_scale_max) / 2,
            (y_scale_min + y_scale_max) * 15 / 20,
            "Instructions:",
        )

        stddraw.setFontSize(int(x_canvas * body_font_size))
        stddraw.text(
            (x_scale_min + x_scale_max) / 2,
            (y_scale_min + y_scale_max) * 12 / 20,
            "[A] move left, [S] stop move, [D] move right",
        )

        stddraw.setFontSize(int(x_canvas * body_font_size))
        stddraw.text(
            (x_scale_min + x_scale_max) / 2,
            (y_scale_min + y_scale_max) * 11 / 20,
            "[Q] rotate left, [W] stop rotate, [E] rotate right",
        )

        stddraw.setFontSize(int(x_canvas * body_font_size))
        stddraw.text(
            (x_scale_min + x_scale_max) / 2,
            (y_scale_min + y_scale_max) * 10 / 20,
            "[Space] to shoot",
        )

        stddraw.setFontSize(int(x_canvas * body_font_size))
        stddraw.text(
            (x_scale_min + x_scale_max) / 2,
            (y_scale_min + y_scale_max) * 8 / 20,
            "[H] for help",
        )

        stddraw.setFontSize(int(x_canvas * body_font_size))
        stddraw.text(
            (x_scale_min + x_scale_max) / 2,
            (y_scale_min + y_scale_max) * 7 / 20,
            "[X] to quit",
        )

        stddraw.setFontSize(int(x_canvas * subtitle_font_size))
        stddraw.text(
            (x_scale_min + x_scale_max) / 2,
            (y_scale_min + y_scale_max) * 4 / 20,
            "Press any key to start",
        )
        # stddraw.show(x) always must be called after all the drawing has taken place
        stddraw.show(20)

        if stddraw.hasNextKeyTyped():
            if stddraw.nextKeyTyped() == "x":
                quit()
            else:
                break
    shooter = Shooter()
    manager = Game_manager()
    manager.create_enemies()

    while True:
        stddraw.clear(stddraw.BLACK)
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()
            if key == 'a':
                shooter.move_left()
            elif key == 'd':
                shooter.move_right()
            elif key == 'q':
                shooter.rotate_left()
            elif key == 'e':
                shooter.rotate_right()
            elif key == 'x':
                break
        manager.refresh_enemies()
        manager.draw_enemies()
        shooter.draw()
        stddraw.show(20)

if __name__ == "__main__":
    main()

