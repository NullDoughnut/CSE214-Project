import stdio, stddraw
from shooter import Shooter
from game_manager import Game_manager
from projectile import Projectile_Manager
from score_manager import Score_Manager
from audio_manager import Audio_Manager
from picture import Picture as pic


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
    background_img = pic("assets/background_img.png")
    menu_img = pic("assets/menu_img.png")

    # Shooter and enemies
    shooter = Shooter()
    manager = Game_manager()
    manager.create_enemies()

    # Projectiles
    projectile_manager = Projectile_Manager()

    # Scores
    score_manager = Score_Manager()

    # Audio
    audio_manager = Audio_Manager()

    # Game state and timer
    # 01/04/26: Dillan van Wyk: created infinite game loop
    game_state = "playing"  # "playing", "game_over", "winner"
    state_timer = 0

    # Movement states
    move_state = None
    rotate_state = None

    # 26/02/26: Dillan van Wyk: set up the title screen
    # 09/04/26: Dillan van Wyk: changed background to an image
    while True:
        stddraw.clear()
        stddraw.picture(menu_img, WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
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
    #Creating what level tracker

    current_level = 1
    final_level = 2
    # Main game loop
    while True:
        stddraw.clear(stddraw.BLACK)

        # 09/04/26: Dillan van Wyk: Changes background to image
        stddraw.picture(background_img, WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)

        # 01/04/26:Denlan Molokwu: created a score tracker at the top
        # Draw the score card
        current_score = (
            manager.score_tracker()
        )  # pulls the score from the manager class and retrieves value of score from score_tracker function

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
            score_manager.score_tracking(current_score, HEIGHT)

            # 02/04/26: Luke Abrahamse: Added movement and rotation of shooter
            if stddraw.hasNextKeyTyped():
                key = stddraw.nextKeyTyped()
                if key == "a":
                    move_state = "left"
                elif key == "d":
                    move_state = "right"
                elif key == "q":
                    rotate_state = "left"
                elif key == "e":
                    rotate_state = "right"
                elif key == "s":
                    move_state = None
                elif key == "w":
                    rotate_state = None
                elif key == " ":
                    projectile_manager.shoot(shooter)
                elif key == "x":
                    break
            if move_state == "left":
                shooter.move_left()
            elif move_state == "right":
                shooter.move_right()
            if rotate_state == "left":
                shooter.rotate_left()
            elif rotate_state == "right":
                shooter.rotate_right()

        # update and draw the projectiles
        projectile_manager.update(0, WIDTH, 0, HEIGHT, manager.enemies)
        projectile_manager.draw()

        # Draw enemies and shooter
        manager.refresh_enemies()
        manager.draw_enemies()
        shooter.draw()
    # 27/03/26:Denlan Molokwu: Created the gameover and winner screen 

    #15/04/26: Denlan Molokwu: Created the concept of different levels and the addition of a boss once reached the end
        if game_state == "playing":
            if manager.check_win():

                if current_level < final_level:
                    current_level += 1
                    manager.enemies.clear()
                    manager.create_minions()
                    

                    if current_level == final_level:
                        manager.create_boss()
                        
                        manager.create_minions()#created once reached final level a boss character spawns
                    else:
                        manager.difficulty()
                        manager.create_enemies()    #increase the difficulty each new level
                    projectile_manager = Projectile_Manager()
                else:
                    game_state = "winner"

        elif manager.check_gameover(
            shooter.y, shooter.x, shooter.radius, shooter.turret_length, 0
        ):
            game_state = "game_over"

        stddraw.show(20)


if __name__ == "__main__":
    main()
