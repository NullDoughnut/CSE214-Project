import stddraw
from shooter import Shooter

stddraw.setCanvasSize(600, 600)
stddraw.setXscale(0, 600)
stddraw.setYscale(0, 600)

shooter = Shooter()
move_state = None
rotate_state = None

while True:
    stddraw.clear(stddraw.BLACK)

    if stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if key == 'a':
            move_state = "left"
        elif key == 'd':
            move_state = "right"
        elif key == 'q':
            rotate_state = "left"
        elif key == 'e':
            rotate_state = "right"
        elif key == "s":
            move_state = None
        elif key == "w":
            rotate_state = None
        elif key == 'x':
            break


    if move_state == "left":
        shooter.move_left()
    elif move_state == "right":
        shooter.move_right()
    if rotate_state == "left":
        shooter.rotate_left()
    elif rotate_state == "right":
        shooter.rotate_right()


    shooter.draw()
    stddraw.show(20)
