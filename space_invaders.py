import stdio, stddraw
from shooter import Shooter
from game_manager import Game_manager
from projectile import Projectile_Manager
from score_manager import Score_Manager

# Game world constants
WIDTH = 600
HEIGHT = 600

CANVAS_SIZE = 500

# Font sizes
TITLE_FONT = 35
SUBTITLE_FONT = 25
BODY_FONT = 18


def main() -> None:
    # Canvas setup
    stddraw.setCanvasSize(CANVAS_SIZE, CANVAS_SIZE)
    stddraw.setXscale(0, WIDTH)
    stddraw.setYscale(0, HEIGHT)

    # Shooter and enemies
    shooter = Shooter()
    manager = Game_manager()
    manager.create_enemies()

    # Projectiles
    projectile_manager = Projectile_Manager()

    # Scores
    score_manager = Score_Manager()

    # Game state and timer
    # 01/04/26: Dillan van Wyk: created infinite game loop
    game_state = "playing"  # "playing", "game_over", "winner"
    state_timer = 0

    # 26/02/26: Dillan van Wyk: set up the title screen
    while True:
        stddraw.clear(stddraw.BLACK)
        stddraw.setPenColor(stddraw.WHITE)

        stddraw.setFontSize(TITLE_FONT)
        stddraw.text(WIDTH / 2, HEIGHT * 18 / 20, "SPACE INVADERS")

        stddraw.setFontSize(SUBTITLE_FONT)
        stddraw.text(WIDTH / 2, HEIGHT * 15 / 20, "Instructions:")

        stddraw.setFontSize(BODY_FONT)
        stddraw.text(
            WIDTH / 2, HEIGHT * 12 / 20, "[A] move left, [S] stop move, [D] move right"
        )
        stddraw.text(
            WIDTH / 2,
            HEIGHT * 11 / 20,
            "[Q] rotate left, [W] stop rotate, [E] rotate right",
        )
        stddraw.text(WIDTH / 2, HEIGHT * 10 / 20, "[Space] to shoot")
        stddraw.text(WIDTH / 2, HEIGHT * 8 / 20, "[H] for help")
        stddraw.text(WIDTH / 2, HEIGHT * 7 / 20, "[X] to quit")

        stddraw.setFontSize(SUBTITLE_FONT)
        stddraw.text(WIDTH / 2, HEIGHT * 4 / 20, "Press any key to start")

        stddraw.show(20)

        if stddraw.hasNextKeyTyped():
            if stddraw.nextKeyTyped() == "x":
                quit()
            else:
                break

    # Main game loop
    while True:
        stddraw.clear(stddraw.BLACK)

        if game_state == "winner":
            score_manager.draw_winner(WIDTH, HEIGHT)
            state_timer += 1

            if state_timer >= 100:
                # Resets game
                shooter = Shooter()
                manager = Game_manager()
                manager.create_enemies()
                projectile_manager = Projectile_Manager()

                game_state = "playing"
                state_timer = 0

            if stddraw.hasNextKeyTyped():
                if stddraw.nextKeyTyped() == "x":
                    break

            stddraw.show(20)
            continue

        elif game_state == "game_over":
            score_manager.draw_game_over(WIDTH, HEIGHT)
            state_timer += 1

            if state_timer >= 100:
                # Resets game
                shooter = Shooter()
                manager = Game_manager()
                manager.create_enemies()
                projectile_manager = Projectile_Manager()

                game_state = "playing"
                state_timer = 0

            if stddraw.hasNextKeyTyped():
                if stddraw.nextKeyTyped() == "x":
                    break

            stddraw.show(20)
            continue

        else:

            # Input handling
            if stddraw.hasNextKeyTyped():
                key = stddraw.nextKeyTyped()
                if key == "a":
                    shooter.move_left()
                elif key == "d":
                    shooter.move_right()
                elif key == "q":
                    shooter.rotate_left()
                elif key == "e":
                    shooter.rotate_right()
                elif key == " ":
                    projectile_manager.shoot(shooter)
                elif key == "x":
                    break

        # update and draw the projectiles
        projectile_manager.update(0, WIDTH, 0, HEIGHT, manager.enemies)
        projectile_manager.draw()

        # Draw enemies and shooter
        manager.refresh_enemies()
        manager.draw_enemies()
        shooter.draw()

        if game_state == "playing":
            if manager.check_win():
                game_state = "winner"

            elif manager.check_gameover(
                shooter.y, shooter.x, shooter.radius, shooter.turret_length, 0
            ):
                game_state = "game_over"

        stddraw.show(20)


if __name__ == "__main__":
    main()
