from enemy import Enemy



class Game_manager:
    enemies = []  # list to store all enemy objects
    speed_x = 3  # speed of enemys in x direction
    speed_y = 30  # speed of enemys in y direction

    drop_count = 0 # this creates a variable that keeps track of how many times the enemies dropped

    def create_enemies(self):
        rows = 3  # number of enemy rows
        col = 5  # number of enemy coloums
        spacing = 60  # spacing between enemys
        x = 150  # starting x coordinate of top left enemy
        y = 480  # starting x coordinate of top left enemy
        for i in range(rows):  # nested loop initialises all enemies in 2D list
            for j in range(col):
                enemy = Enemy()
                enemy.x = x + j * spacing
                enemy.y = y - i * spacing
                self.enemies.append(enemy)

    def refresh_enemies(self):  # incriments all enemys in x direction by current speed
        for i in range(len(self.enemies)):
            self.enemies[i].x += self.speed_x

        hit_wall = False
        for i in range(len(self.enemies)):  # checks if any enemy has hit a wall
            if self.enemies[i].x + self.enemies[i].radius >= 600:
                hit_wall = True
            elif self.enemies[i].x - self.enemies[i].radius <= 0:
                hit_wall = True

        if (
            hit_wall
        ):  # if enemy has hit a wall reverse x direction and drop enemies down
            self.speed_x = -1 * self.speed_x
            self.drop_count += 1
            for i in range(len(self.enemies)):
                self.enemies[i].y -= self.speed_y

    def draw_enemies(self):  # draws every enemy in the enemies list
        for i in range(len(self.enemies)):
            self.enemies[i].draw()

    def check_gameover(self, shooter_y):

        for enemy in self.enemies:#looking into the list of the enemies
            if enemy.alive == True:
                if (enemy.y - enemy.radius) <= shooter_y:     #this line checks the bottom of the enemy row that is still alive and compares it to the turrets y coordinate
                    return True
        return False
    def check_win(self):
        
        for enemy in self.enemies:
            if enemy.alive == True:
                return False
        return True
                




