from enemy import Enemy
from projectile import Projectile
from enemy import Minions
import random


# 30/03/26: Luke Abrahamse: Created Game_manager
# 18/04/26: Dillan van Wyk: Moved from class attributes to instance attributes
class Game_manager:
    def __init__(self):
        self.enemies = []  # list to store all enemy objects
        self.speed_x = 3  # speed of enemys in x direction
        self.speed_y = 30  # speed of enemys in y direction

        self.drop_count = 0  # this creates a variable that keeps track of how many times the enemies dropped

    # 30/03/26: Luke Abrahamse: Added create enemies function
    def create_enemies(self):
        rows = 3
        col = 5
        spacing = 60  # spacing between enemys
        x = 150  # starting x coordinate of top left enemy
        y = 480  # starting x coordinate of top left enemy
        for i in range(rows):  # nested loop initialises all enemies in 2D list
            for j in range(col):
                enemy = Enemy()
                enemy.x = x + j * spacing
                enemy.y = y - i * spacing
                self.enemies.append(enemy)

    # 15/04/2026: Denlan Molokwu: Created new enemy types called the boss and the minions
    def create_boss(self):
        boss = Enemy()

        boss.x = 300
        boss.y = 500

        boss.radius = 45
        boss.enemy_type = "boss"

        self.enemies.append(boss)

    def create_minions(self):

        minions = Minions()

        minions.x = 100
        minions.y = 405
        minions.radius = 15
        minions.enemy_type = "minion"
        self.enemies.append(minions)

    # 30/03/26: Luke Abrahamse: Added refresh_enemies function to update the state of each enemy
    # 02/04/26: Luke Abrahamse: Fixed enemy wall collision bug
    def refresh_enemies(self):  # incriments all enemys in x direction by current speed

        for i in range(len(self.enemies)):
            if self.enemies[i].enemy_type != "boss":
                self.enemies[i].x += self.speed_x

        hit_wall = False

        for i in range(len(self.enemies)):  # checks if any enemy has hit a wall
            if self.enemies[i].alive and self.enemies[i].enemy_type != "boss":
                if self.enemies[i].x + self.enemies[i].radius >= 600:
                    hit_wall = True
                    break
                elif self.enemies[i].x - self.enemies[i].radius <= 0:
                    hit_wall = True
                    break
        if (
            hit_wall
        ):  # if enemy has hit a wall reverse x direction and drop enemies down
            self.speed_x = -1 * self.speed_x
            self.drop_count += 1
            for i in range(len(self.enemies)):
                if self.enemies[i].enemy_type == "alien":
                    self.enemies[i].y -= self.speed_y

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


# def boss_shooting(self):
#    if len(self.enemies) > 0:
#       p = Projectile()
#     boss = self.enemies[0]
# intializes the starting position and angle for the projectile
#    p.x = boss.x
#     p.y = boss.y - boss_radius
#    p.angle = 270
#     p.speed = 20

#   return p
