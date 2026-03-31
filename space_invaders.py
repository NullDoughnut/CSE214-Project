import stdio, stddraw
from shooter import Shooter
from game_manager import Game_manager


# 31/03/26: Dillan van Wyk: Added function to check for collisions and implemented it
def collision(projectile, enemy):
    dx = projectile.x - enemy.x
    dy = projectile.y - enemy.y
    distance = (dx**2 + dy**2) ** 0.5
    return distance <= (enemy.radius + projectile.radius)


def main() -> None:
    # Screen setup
    x_scale_min, y_scale_min = 0, 0
    x_scale_max, y_scale_max = 600, 600
    x_canvas, y_canvas = 500, 500

    # Font sizes
    main_title_font_size = 0.07
    subtitle_font_size = 0.05
    body_font_size = 0.04

    # Canvas initialization
    stddraw.setCanvasSize(x_canvas, y_canvas)
    stddraw.setXscale(x_scale_min, x_scale_max)
    stddraw.setYscale(y_scale_min, y_scale_max)

    # Shooter and enemies
    shooter = Shooter()
    manager = Game_manager()
    manager.create_enemies()

    # Projectiles
    projectiles = []
    max_cooldown = 15
    cooldown = max_cooldown

    # Title screen
    # 26/02/26: Dillan van Wyk: set up the title screen
    while True:
        stddraw.clear(stddraw.BLACK)
        stddraw.setPenColor(stddraw.WHITE)

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
        stddraw.text(
            (x_scale_min + x_scale_max) / 2,
            (y_scale_min + y_scale_max) * 11 / 20,
            "[Q] rotate left, [W] stop rotate, [E] rotate right",
        )
        stddraw.text(
            (x_scale_min + x_scale_max) / 2,
            (y_scale_min + y_scale_max) * 10 / 20,
            "[Space] to shoot",
        )
        stddraw.text(
            (x_scale_min + x_scale_max) / 2,
            (y_scale_min + y_scale_max) * 8 / 20,
            "[H] for help",
        )
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

        stddraw.show(20)

        if stddraw.hasNextKeyTyped():
            if stddraw.nextKeyTyped() == "x":
                quit()
            else:
                break

    # Main game loop
    while True:
        stddraw.clear(stddraw.BLACK)

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
                if cooldown == 0:
                    projectiles.append(shooter.shoot())
                    cooldown = max_cooldown
            elif key == "x":
                break

        # Cooldown countdown
        if cooldown > 0:
            cooldown -= 1

        # 31/03/26: Dillan van Wyk: Projectile collisions with enemies
        for p in projectiles[:]:
            for e in manager.enemies:
                if e.alive and collision(p, e):
                    e.alive = False
                    projectiles.remove(p)
                    break

        # 31/03/26: Dillan van Wyk: Projectile movement, projectile drawing and off-screen removal
        for i in projectiles[:]:
            if (i.x < x_scale_min or i.x > x_scale_max) or (
                i.y < y_scale_min or i.y > y_scale_max
            ):
                projectiles.remove(i)
            else:
                i.move()

        # Draw projectiles
        for i in projectiles:
            i.draw()

        # Draw enemies and shooter
        manager.refresh_enemies()
        manager.draw_enemies()
        shooter.draw()

        stddraw.show(20)


if __name__ == "__main__":
    main()
