import stddraw
from picture import Picture as pic
from constants import WIDTH, HEIGHT, TITLE_FONT, SUBTITLE_FONT, BODY_FONT

menu_img = pic("assets/menu_img.png")


# 18/04/26: Dillan van Wyk: Created Screen_Manager class to deal with all of the screens
class Screen_Manager:
    # 26/02/26: Dillan van Wyk: set up the title screen
    # 09/04/26: Dillan van Wyk: changed background to an image
    # 18/04/26: Dillan van Wyk: Added control instructions for player 2 and moved other text around
    def draw_title_screen(self):
        while True:
            stddraw.clear()
            stddraw.picture(menu_img, WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
            stddraw.setPenColor(stddraw.WHITE)

            stddraw.setFontSize(TITLE_FONT)
            stddraw.text(WIDTH / 2, HEIGHT * 19 / 20, "SPACE INVADERS")

            stddraw.setFontSize(SUBTITLE_FONT)
            stddraw.text(WIDTH / 2, HEIGHT * 17 / 20, "Instructions:")

            stddraw.setFontSize(BODY_FONT)
            stddraw.text(
                WIDTH / 2,
                HEIGHT * 15 / 20,
                "P1: [A] move left, [S] stop movement, [D] move right",
            )
            stddraw.text(
                WIDTH / 2,
                HEIGHT * 14 / 20,
                "P1: [Q] rotate left, [W] stop rotation, [E] rotate right",
            )
            stddraw.text(WIDTH / 2, HEIGHT * 13 / 20, "P1: [Space] to shoot")

            stddraw.text(
                WIDTH / 2,
                HEIGHT * 11 / 20,
                "P2: [J] move left, [K] stop movement, [L] move right",
            )
            stddraw.text(
                WIDTH / 2,
                HEIGHT * 10 / 20,
                "P2: [U] rotate left, [I] stop rotation, [O] rotate right",
            )
            stddraw.text(WIDTH / 2, HEIGHT * 9 / 20, "P2: [N] to shoot")

            stddraw.text(WIDTH / 2, HEIGHT * 7 / 20, "[X] to quit, [P] to pause")

            stddraw.setFontSize(SUBTITLE_FONT)
            stddraw.text(WIDTH / 2, HEIGHT * 5.2 / 20, "[1] Single Player   [2] Co-op")

            stddraw.show(20)

            # 18/04/26: Dillan van Wyk: Checks if the player(s) want to play single or multiplayer
            if stddraw.hasNextKeyTyped():
                key = stddraw.nextKeyTyped()
                if key == "x":
                    quit()
                elif key == "1":
                    return False
                elif key == "2":
                    return True

    # 18/04/26: Dillan van Wyk: Created help screen that displays the controls for both players 1 and 2. Simply copied title screen instructions
    def draw_help(self):
        while True:
            stddraw.clear()
            stddraw.picture(menu_img, WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
            stddraw.setPenColor(stddraw.WHITE)

            stddraw.setFontSize(TITLE_FONT)
            stddraw.text(WIDTH / 2, HEIGHT * 18 / 20, "HELP")

            stddraw.setFontSize(BODY_FONT)
            stddraw.text(
                WIDTH / 2,
                HEIGHT * 15 / 20,
                "P1: [A] move left, [S] stop movement, [D] move right",
            )
            stddraw.text(
                WIDTH / 2,
                HEIGHT * 14 / 20,
                "P1: [Q] rotate left, [W] stop rotation, [E] rotate right",
            )
            stddraw.text(WIDTH / 2, HEIGHT * 13 / 20, "P1: [Space] to shoot")
            stddraw.text(
                WIDTH / 2,
                HEIGHT * 11 / 20,
                "P2: [J] move left, [K] stop movement, [L] move right",
            )
            stddraw.text(
                WIDTH / 2,
                HEIGHT * 10 / 20,
                "P2: [U] rotate left, [I] stop rotation, [O] rotate right",
            )
            stddraw.text(WIDTH / 2, HEIGHT * 9 / 20, "P2: [N] to shoot")

            stddraw.setFontSize(SUBTITLE_FONT)
            stddraw.text(WIDTH / 2, HEIGHT * 5 / 20, "Press any key to exit help")

            stddraw.show(20)

            if stddraw.hasNextKeyTyped():
                key = stddraw.nextKeyTyped()
                if key == "x":
                    quit()
                else:
                    return None

    # 27/03/26: Denlan Molokwu: Created the gameover and winner screen
    def draw_game_over(self, width, height):
        stddraw.clear()
        stddraw.picture(menu_img, width / 2, height / 2, width, height)
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.setFontSize(40)
        stddraw.text(width / 2, height / 2, "GAME OVER")

    def draw_winner(self, width, height):
        stddraw.clear()
        stddraw.picture(menu_img, width / 2, height / 2, width, height)
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.setFontSize(40)
        stddraw.text(width / 2, height / 2, "YOU ARE A WINNER")

    # 19/04/26: Luke Abrahamse: Created the Pause Menu
    def draw_pause_menu(self):
        while True:
            stddraw.clear()
            stddraw.picture(menu_img, WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
            stddraw.setPenColor(stddraw.WHITE)

            stddraw.setFontSize(TITLE_FONT)
            stddraw.text(WIDTH / 2, HEIGHT * 0.8, "PAUSED")

            stddraw.setFontSize(SUBTITLE_FONT)
            stddraw.text(WIDTH / 2, HEIGHT * 0.6, "[R] Resume")
            stddraw.text(WIDTH / 2, HEIGHT * 0.5, "[T] Restart Game")
            stddraw.text(WIDTH / 2, HEIGHT * 0.4, "[M] Main Menu")
            stddraw.text(WIDTH / 2, HEIGHT * 0.3, "[H] Help")
            stddraw.text(WIDTH / 2, HEIGHT * 0.2, "[X] Quit")

            stddraw.show(20)

            if stddraw.hasNextKeyTyped():
                key = stddraw.nextKeyTyped()
                if key == "x":
                    quit()
                elif key == "r":
                    return "resume"
                elif key == "t":
                    if self.draw_confirm("Restart Game?"):
                        return "restart"
                elif key == "m":
                    if self.draw_confirm("Quit to Menu?"):
                        return "menu"
                elif key == "h":
                    self.draw_help()

    # 19/04/26: Luke Abrahamse: Created the confirm screen
    def draw_confirm(self, message):
        while True:
            stddraw.clear()
            stddraw.picture(menu_img, WIDTH / 2, HEIGHT / 2, WIDTH, HEIGHT)
            stddraw.setPenColor(stddraw.WHITE)

            stddraw.setFontSize(TITLE_FONT)
            stddraw.text(WIDTH / 2, HEIGHT / 2 + 30, message)
            stddraw.text(WIDTH / 2, HEIGHT / 2 - 30, "Are you sure? [Y/N]")

            stddraw.show(20)

            if stddraw.hasNextKeyTyped():
                key = stddraw.nextKeyTyped()
                if key == "x":
                    quit()
                elif key == "y":
                    return True
                elif key == "n":
                    return False
