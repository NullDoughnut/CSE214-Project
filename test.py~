import stddraw
from shooter import Shooter

stddraw.setCanvasSize(600, 600)
stddraw.setXscale(0, 100)
stddraw.setYscale(0, 100)

s = Shooter()

while True:
    stddraw.clear(stddraw.GRAY)

    if stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if key == 'a':
            s.move_left()
        elif key == 'd':
            s.move_right()
        elif key == 'q':
            s.rotate_left()
        elif key == 'e':
            s.rotate_right()
        elif key == 'x':
            break

    s.draw()
    stddraw.show(20)
