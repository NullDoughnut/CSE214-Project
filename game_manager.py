from enemy import Enemy
from projectile import Projectile
from enemy import Minions
import random


# 30/03/26: Luke Abrahamse: Created Game_manager
# 18/04/26: Dillan van Wyk: Moved from class attributes to instance attributes
class Game_manager:
    def __init__(self):
        self.enemies = []  # list to store all enemy objects
        self.speed_x = 2.5  # speed of enemy in x direction
        self.minion_speed_x = 5  # speed of minion in x direction
        self.speed_y = 15  # speed of enemys in y direction

        self.drop_count = 0  # this creates a variable that keeps track of how many times the enemies dropped

    # 30/03/26: Luke Abrahamse: Added create enemies function
    def create_enemies(self):
        rows = 3
        col = 5
        spacing = 60  # spacing between enemys
        x = 150  # starting x coordinate of top left enemy
        y = 390  # starting x coordinate of top left enemy
        for i in range(rows):  # nested loop initialises all enemies in 2D list
            for j in range(col):
                enemy = Enemy()
                enemy.x = x + j * spacing
                enemy.y = y - i * spacing
                enemy.enemy_type = "alien"  # ensures every alien has a type
                self.enemies.append(enemy)

    # 15/04/26: Denlan Molokwu: Created new enemy types called the boss and the minions
    # 23/04/26: Dillan van Wyk: Gave boss a health of 3
    def create_boss(self):
        boss = Enemy()

        boss.x = 300
        boss.y = 530

        boss.radius = 35
        boss.enemy_type = "boss"
        boss.health = 3
        boss.max_health = 3

        self.enemies.append(boss)

    def create_minions(self, level):
        num_minions = level + 1  # logic to spawn more minions each level
        spacing = 60
        for i in range(num_minions):
            minions = Minions()

            minions.x = 100 + (i * spacing)
            minions.y = 450
            minions.radius = 15
            minions.enemy_type = "minion"
            self.enemies.append(minions)

    # 30/03/26: Luke Abrahamse: Added refresh_enemies function to update the state of each enemy
    # 02/04/26: Luke Abrahamse: Fixed enemy wall collision bug
    # 21/04/2026: Denlan Molokwu: Fixed the way collisions affected bumping against the wall so minion and enemies behaved differently
    def refresh_enemies(self):  # incriments all enemys in x direction by current speed

        for i in range(len(self.enemies)):
            if self.enemies[i].enemy_type == "alien":
                self.enemies[i].x += self.speed_x
            elif self.enemies[i].enemy_type == "minion":
                self.enemies[i].x += self.minion_speed_x

        alien_hit_wall = False
        minion_hit_wall = False

        for i in range(len(self.enemies)):  # checks if any enemy has hit a wall
            if self.enemies[i].alive and self.enemies[i].enemy_type == "alien":
                if self.enemies[i].x + self.enemies[i].radius >= 600:
                    alien_hit_wall = True
                    break
                elif self.enemies[i].x - self.enemies[i].radius <= 0:
                    alien_hit_wall = True
                    break
                # checks if alien hit a wall
        for i in range(len(self.enemies)):

            if self.enemies[i].alive and self.enemies[i].enemy_type == "minion":
                if self.enemies[i].x + self.enemies[i].radius >= 600:
                    minion_hit_wall = True
                    break
                elif self.enemies[i].x - self.enemies[i].radius <= 0:
                    minion_hit_wall = True
                    break

        if (
            alien_hit_wall
        ):  # if enemy has hit a wall reverse x direction and drop enemies down
            self.speed_x = -1 * self.speed_x
            self.drop_count += 1
            for i in range(len(self.enemies)):
                if self.enemies[i].enemy_type == "alien":
                    self.enemies[i].y -= self.speed_y
        if (minion_hit_wall) == True:
            self.minion_speed_x = -1 * self.minion_speed_x

    # 30/03/26: Luke Abrahamse: Added draw enemies function
    def draw_enemies(self):
        for i in range(len(self.enemies)):
            self.enemies[i].draw()

    # 31/03/26: Denlan Molokwu: Added game over screen
    # 01/04/26: Dillan van Wyk: Changed logic for when game over screen is displayed and added check for bottom of screen and added self.enemies.clear()
    # 18/04/26: Dillan van Wyk: Changed function to return "hit" to let the player lose health and "bottom" to end the game
    def check_gameover(
        self, shooter_y, shooter_x, shooter_radius, turrent_length, bottom_edge_y
    ):
        # gets the absolute tip of the shooter
        y_s = shooter_y + turrent_length

        # gets the left and right most points of the shooter
        x_s_left = shooter_x - shooter_radius
        x_s_right = shooter_x + shooter_radius

        for enemy in self.enemies:  # looking into the list of the enemies
            if enemy.alive:
                if (
                    (enemy.y - enemy.radius) <= y_s
                    and (enemy.x + enemy.radius) >= x_s_left
                    and (enemy.x - enemy.radius) <= x_s_right
                ):
                    return "hit"  # the player will lose a heart

                if (enemy.y - enemy.radius) <= bottom_edge_y:
                    self.enemies.clear()
                    return "bottom"  # immediate game over
        return None

    # 27/03/2026: Denlan Molokwu: Created a winning condition to see if the winner wins
    def check_win(self):

        for enemy in self.enemies:
            if enemy.alive == True:
                return False
        return True

    # 01/04/26: Denlan Molokwu implemented a score tracker

    def score_tracker(self):
        score = 0
        for enemy in self.enemies:
            if enemy.alive == False:
                score += 100
        return score

    # 15/04/2026: Denlan Molokwu: created the function that increases the difficulty of each level
    def difficulty(self):
        self.speed_x = self.speed_x * 1.3
        self.speed_y = self.speed_y + 4

    # 18/04/26: Dillan van Wyk: Created function to push enemies back if player lost a life from an enemy touching them
    def push_enemies(self):
        for enemy in self.enemies:
            enemy.y += 60

    # 19/04/26: Dillan van Wyk: Created method that allows an enemy to shoot a projectile with probability 0.002
    def enemy_shoot(self, shoot_chance=0.002):
        projectiles = []

        for enemy in self.enemies:
            if enemy.alive and random.random() < shoot_chance:
                projectiles.append(enemy.shoot())

        return projectiles
