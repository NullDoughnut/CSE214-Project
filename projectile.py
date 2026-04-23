import stddraw
import math
from audio_manager import Audio_Manager
from bunker import Bunker

audio = Audio_Manager()


# 31/03/26: Dillan van Wyk: Added function to check for collisions and implemented it
def collision(projectile, enemy):
    dx = projectile.x - enemy.x
    dy = projectile.y - enemy.y
    distance = (dx**2 + dy**2) ** 0.5
    return distance <= (enemy.radius + projectile.radius)


# 19/04/2026: Denlan Molokwu: Created a collision function just for the bunker
def bunker_collision(projectile, bunker):
    left_edge = bunker.x
    right_edge = (
        bunker.x + bunker.width
    )  # these just give the boundaries to check whether a bullet collides with the bunker will implement in a different function
    bottom = bunker.y
    top = bunker.y + bunker.height
    if projectile.x >= left_edge and projectile.x <= right_edge:
        if (
            projectile.y >= bottom and projectile.y <= top
        ):  # implemented logic for bullet and return true if collision occured and false if not
            return True

    return False


# 31/03/26: Dillan van Wyk: Made the Projectile class and the move() and draw() functions
# 18/04/26: Dillan van Wyk: Moved from class attributes to instance attributes
class Projectile:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 90
        self.speed = 15
        self.radius = 5
        self.alive = True

    def move(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))

    # 19/04/26: Dillan van Wyk: Added color to parameters so that the color of the projectiles can be changed
    def draw(self, color=stddraw.WHITE):
        stddraw.setPenColor(color)
        if self.alive:
            stddraw.filledCircle(self.x, self.y, self.radius)


# 31/03/26: Dillan van Wyk: Created the Project_Manager class to contain and manage functions related to projectiles [update(), draw(), shoot()]
# 18/04/26: Dillan van Wyk: Moved from class attributes to instance attributes
# 19/04/26: Denlan Molokwu: Implemented logic for bunker collision
# 20/04/26: Dillan van Wyk: Added score tracking based off enemy colision in update method
# 23/04/26: Dillan van Wyk: Enemies now have health. They should now only die when their health is zero and score only added when enemy dies
#                           and enemies should only drop powerups if they die
class Projectile_Manager:
    def __init__(self):
        self.projectiles = []
        self.max_cooldown = 10
        self.cooldown = 0

    def update(
        self,
        x_min,
        x_max,
        y_min,
        y_max,
        enemies,
        bunker,
        score_mgr,
        powerup_manager=None,
    ):
        if self.cooldown > 0:
            self.cooldown -= 1

        # Projectile collisions with enemy removes that enemy
        # projectile collisions with bunker reduces health of bunker
        for p in self.projectiles[:]:
            bullet_destroyed = False  # helps identify if it has hit the bunker and if it has the bullet ultimately gets destroyed

            for b in bunker:
                if b.alive and bunker_collision(p, b):
                    b.health -= 1
                    if b.health <= 0:
                        b.alive = False
                    self.projectiles.remove(p)
                    bullet_destroyed = True
                    break
            if bullet_destroyed:
                continue  # did this so that if it has hit a bunker dont check for enemy collision after that

            # Added score tracking
            for e in enemies:
                if e.alive and collision(p, e):
                    e.health -= 1
                    self.projectiles.remove(p)
                    if e.health <= 0:
                        e.alive = False
                        score_mgr.register_points(100)
                        if powerup_manager:
                            powerup_manager.spawn_powerup(e.x, e.y)

                    break

        # Projectile off-screen removal and movement of projectiles
        for p in self.projectiles[:]:
            if (p.x < x_min or p.x > x_max) or (p.y < y_min or p.y > y_max):
                self.projectiles.remove(p)
            else:
                p.move()

    # Draw projectiles
    def draw(self, color=stddraw.WHITE):
        for p in self.projectiles:
            p.draw(color)

    # Allows shooter to shoot projectiles
    def shoot(self, shooter, powerup_manager=None):
        if self.cooldown == 0:
            self.projectiles.append(shooter.shoot())

            if powerup_manager and powerup_manager.multi_shot_timer > 0:
                lp = shooter.shoot()
                lp.angle += 20
                rp = shooter.shoot()
                rp.angle -= 20
                self.projectiles.append(lp)
                self.projectiles.append(rp)

            self.cooldown = self.max_cooldown
            audio.play_tone(4400, 0.1)
