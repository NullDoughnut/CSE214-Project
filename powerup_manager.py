import random
import stddraw
from powerup import PowerUp

# 19/04/2026: Luke Abrahamse: Created the powerup_manager class

class Powerup_Manager:
    def __init__(self):
        self.powerups = []
        self.rapid_fire_timer = 0
        self.multi_shot_timer = 0
        self.powerup_duration = 300

    def spawn_powerup(self, x, y): # spawns a random powerup
        if random.random() < 0.15:
            powerup_type = random.choice(["rapid_fire", "multi_shot", "extra_life"])
            self.powerups.append(PowerUp(x, y, powerup_type))

    def update(self, shooter, projectile_manager): # Updates powerup timers
        if self.rapid_fire_timer > 0:
            self.rapid_fire_timer -= 1
            if self.rapid_fire_timer == 0:
                projectile_manager.max_cooldown = 15
        if self.multi_shot_timer > 0:
            self.multi_shot_timer -= 1

        for pu in self.powerups[:]: # Checks for collision with a square hitbox
            pu.move()
            if abs(pu.x - shooter.x) < (pu.radius + shooter.radius) and abs(pu.y - shooter.y) < (pu.radius + shooter.radius):
                self.apply_effect(pu.powerup_type, shooter, projectile_manager)
                self.powerups.remove(pu)

    def apply_effect(self, powerup_type, shooter, projectile_manager): # Applys the affect 
        pu = powerup_type
        if pu == "extra_life":
            if shooter.lives < 3:
                shooter.lives += 1
        elif pu == "rapid_fire":
            self.rapid_fire_timer = self.powerup_duration
            projectile_manager.max_cooldown = 5
        elif pu == "multi_shot":
            self.multi_shot_timer = self.powerup_duration
    
    def draw(self):
        for i in range(len(self.powerups)):
            self.powerups[i].draw()
