from enemy import Enemy

class Game_manager:
    enemies = []  # list to store all enemy objects
    speed_x = 3  # speed of enemys in x direction
    speed_y = 30  # speed of enemys in y direction

    drop_count = 0  # this creates a variable that keeps track of how many times the enemies dropped

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

    # 30/03/26: Luke Abrahamse: Added refresh_enemies function to update the state of each enemy
    # 02/04/26: Luke Abrahamse: Fixed enemy wall collision bug
    def refresh_enemies(self):  # incriments all enemys in x direction by current speed
        for i in range(len(self.enemies)):
            self.enemies[i].x += self.speed_x

        hit_wall = False

        for i in range(len(self.enemies)):  # checks if any enemy has hit a wall
            if (self.enemies[i].alive):
                if self.enemies[i].x + self.enemies[i].radius >= 600:
                    hit_wall = True
                    break
                elif self.enemies[i].x - self.enemies[i].radius <= 0:
                    hit_wall = True
                    break
        if (hit_wall):  # if enemy has hit a wall reverse x direction and drop enemies down
            self.speed_x = -1 * self.speed_x
            self.drop_count += 1
            for i in range(len(self.enemies)):
                self.enemies[i].y -= self.speed_y

    # 30/03/26: Luke Abrahamse: Added draw enemies function
    def draw_enemies(self):
        for i in range(len(self.enemies)):
            self.enemies[i].draw()

    # 31/03/26: Denlan Molokwu: Added game over screen
    # 01/04/26: Dillan van Wyk: Changed logic for when game over screen is displayed and added check for bottom of screen and added self.enemies.clear()
    def check_gameover(
        self, shooter_y, shooter_x, shooter_radius, turrent_length, bottom_edge_y
    ):
        # gets the absolute tip of the shooter
        y_s = shooter_y + turrent_length

        # gets the left and right most points of the shooter
        x_s_left = shooter_x - shooter_radius
        x_s_right = shooter_x + shooter_radius

        for enemy in self.enemies:  # looking into the list of the enemies
            if enemy.alive == True:
                if (
                    (enemy.y - enemy.radius) <= y_s
                    and (
                        (enemy.x + enemy.radius) >= x_s_left
                        and (enemy.x - enemy.radius) <= x_s_right
                    )
                    or (enemy.y - enemy.radius) <= bottom_edge_y
                ):  # this line checks the bottom of the enemy row that is still alive and compares it to the turrets y coordinate
                    self.enemies.clear()
                    return True
        return False

     
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
