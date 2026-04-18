import stdio, stddraw
from shooter import Shooter
from game_manager import Game_manager
from projectile import Projectile_Manager
from score_manager import Score_Manager
from audio_manager import Audio_Manager
from picture import Picture as pic
from screen_manager import Screen_Manager
from constants import WIDTH, HEIGHT, CANVAS_SIZE


def main() -> None:
    # Canvas setup
    stddraw.setCanvasSize(CANVAS_SIZE, CANVAS_SIZE)
    stddraw.setXscale(0, WIDTH)
    stddraw.setYscale(0, HEIGHT)
    background_img = pic("assets/background_img.png")

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

    # Screens
    screen_manager = Screen_Manager()
    multiplayer = screen_manager.draw_title_screen()

    # Game state and timer
    # 01/04/26: Dillan van Wyk: created infinite game loop
    game_state = "playing"  # "playing", "game_over", "winner"
    state_timer = 0

    # Movement states
    move_state = None
    rotate_state = None

    # Creating level tracker
    current_level = 1
    final_level = 2

    # 18/04/26: Dillan van Wyk: Spawns player 1 on the left of the screen and player 2 on the right of the screen, if playing co-op
    if multiplayer:
        shooter2 = Shooter()
        shooter2.x = 450
        shooter2.color = stddraw.RED
        shooter.x = 150
        projectile_manager2 = Projectile_Manager()
        move_state2 = None
        rotate_state2 = None

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
            screen_manager.draw_winner(WIDTH, HEIGHT)
            state_timer += 1

            if state_timer >= 100:
                # Resets game
                shooter = Shooter()
                manager = Game_manager()
                manager.create_enemies()
                projectile_manager = Projectile_Manager()

                if multiplayer:
                    shooter2 = Shooter()
                    shooter2.x = 450
                    shooter.x = 150
                    projectile_manager2 = Projectile_Manager()

                game_state = "playing"
                state_timer = 0

            if stddraw.hasNextKeyTyped():
                if stddraw.nextKeyTyped() == "x":
                    break

            stddraw.show(20)
            continue

        elif game_state == "game_over":
            screen_manager.draw_game_over(WIDTH, HEIGHT)
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

            # 18/04/26: Dillan van Wyk: Draw both players' lives at the top right of the screen if co-op is selected
            if multiplayer:
                score_manager.draw_lives(shooter.lives, WIDTH, HEIGHT, "P1: ", 120)
                score_manager.draw_lives(shooter2.lives, WIDTH, HEIGHT, "P2: ")
            else:
                score_manager.draw_lives(shooter.lives, WIDTH, HEIGHT)

            # 02/04/26: Luke Abrahamse: Added movement and rotation of shooter
            # 18/04/26: Dillan van Wyk: Implemented player movement for player 2
            # 18/04/26: Dillan van Wyk: Fixed bug were player 1's movement code prevented player 2's input from being read.
            if stddraw.hasNextKeyTyped():
                key = stddraw.nextKeyTyped()

                # Player 1 controls
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
                    if shooter.lives > 0:
                        projectile_manager.shoot(shooter)
                elif key == "h":
                    screen_manager.draw_help()
                elif key == "x":
                    break

                # Player 2 controls
                if multiplayer:
                    if key == "j":
                        move_state2 = "left"
                    elif key == "k":
                        move_state2 = None
                    elif key == "l":
                        move_state2 = "right"
                    elif key == "u":
                        rotate_state2 = "left"
                    elif key == "i":
                        rotate_state2 = None
                    elif key == "o":
                        rotate_state2 = "right"
                    elif key == "n":
                        if shooter2.lives > 0:
                            projectile_manager2.shoot(shooter2)

            if move_state == "left":
                shooter.move_left()
            elif move_state == "right":
                shooter.move_right()
            if rotate_state == "left":
                shooter.rotate_left()
            elif rotate_state == "right":
                shooter.rotate_right()

            if multiplayer:
                if move_state2 == "left":
                    shooter2.move_left()
                elif move_state2 == "right":
                    shooter2.move_right()
                if rotate_state2 == "left":
                    shooter2.rotate_left()
                elif rotate_state2 == "right":
                    shooter2.rotate_right()

        # Update and draw the projectiles
        projectile_manager.update(0, WIDTH, 0, HEIGHT, manager.enemies)
        projectile_manager.draw()

        # 18/04/26: Dillan van Wyk: Update and draw the projectiles for player 2
        if multiplayer:
            projectile_manager2.update(0, WIDTH, 0, HEIGHT, manager.enemies)
            projectile_manager2.draw()

        # Draw enemies and shooter
        manager.refresh_enemies()
        manager.draw_enemies()
        if shooter.lives > 0:
            shooter.draw()

        # 18/04/26: Dillan van Wyk: Draw player 2
        if multiplayer:
            if shooter2.lives > 0:
                shooter2.draw()

        # 15/04/26: Denlan Molokwu: Created the concept of different levels and the addition of a boss once reached the end
        if game_state == "playing":
            if manager.check_win():

                if current_level < final_level:
                    current_level += 1
                    manager.enemies.clear()
                    manager.create_minions()

                    if current_level == final_level:
                        manager.create_boss()

                        manager.create_minions()  # created once reached final level a boss character spawns
                    else:
                        manager.difficulty()
                        manager.create_enemies()  # increase the difficulty each new level
                    projectile_manager = Projectile_Manager()
                else:
                    game_state = "winner"

        # 18/04/26: Dillan van Wyk: Fixed bug were enemies were interacting with dead player by only checking gameover if the shooter has lives
        if shooter.lives > 0:
            result = manager.check_gameover(
                shooter.y, shooter.x, shooter.radius, shooter.turret_length, 0
            )

            # 18/04/26: Dillan van Wyk: Added player lives logic
            if result == "hit":
                shooter.lives -= 1
                shooter.x = 300  # reset position of shooter to starting position
                shooter.angle = 90
                manager.push_enemies()

            elif result == "bottom":
                game_state = "game_over"

        # 18/04/26: Dillan van Wyk: Handles game over logic for both players
        if multiplayer:
            # 18/04/26: Dillan van Wyk: Fixed bug were enemies were interacting with dead player by only checking gameover if the shooter has lives
            if shooter2.lives > 0:
                result2 = manager.check_gameover(
                    shooter2.y, shooter2.x, shooter2.radius, shooter2.turret_length, 0
                )

                if result2 == "hit":
                    shooter2.lives -= 1
                    shooter2.x = 450
                    shooter2.angle = 90
                    manager.push_enemies()
                elif result2 == "bottom":
                    game_state = "game_over"

            # Game only ends when both players lose all of their lives
            if shooter.lives <= 0 and shooter2.lives <= 0:
                game_state = "game_over"

        else:
            if shooter.lives <= 0:
                game_state = "game_over"

        stddraw.show(20)


if __name__ == "__main__":
    main()
