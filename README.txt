Dillan van Wyk:

20/04/26: Used Google's AI Overview to figure out how to use the 'global' keyword in order to fix a bug where the high score was reset after every session.
SEARCH:
"what does global key mean in python"

RESPONSE:
In Python, the global keyword is a statement used inside a function to indicate that a specific variable belongs to the global scope (the top-level scope of a module). 
It allows you to modify a variable that was defined outside of the function, rather than creating a new local variable with the same name inside the function. 

Core Functions and Purpose
Modifying Global Variables: By default, if you assign a value to a variable inside a function, Python treats it as a local variable. To change a global variable's value from within a function, you must declare it with global.
Preventing Local Shadowing: It tells Python, "Do not create a new local variable; use the one from the module level".
Sharing State: It is used to share and update a variable's state across different functions or modules. 
How to Use global
Without global (Creates a local variable):
python
x = 10
def modify_x():
    x = 20  # This creates a new LOCAL variable x
    print("Inside:", x)

modify_x()
print("Outside:", x)  # The global x remains 10
# Output:
# Inside: 20
# Outside: 10
With global (Modifies the global variable):
python
x = 10
def modify_x():
    global x  # Declares that we are using the global x
    x = 20    # Modifies the global x
    print("Inside:", x)

modify_x()
print("Outside:", x)  # The global x is now 20
# Output:
# Inside: 20
# Outside: 20
Important Rules and Considerations
Access vs. Modification: You can read (access) global variables inside a function without the global keyword, but you cannot reassign (modify) them.
Mutable Objects: If a global variable is a mutable object (like a list or dictionary), you can modify its contents (e.g., list.append()) without the global keyword. You only need global when you want to reassign the variable to a new object (e.g., list = [1, 2]).
Best Practice: Overusing global is discouraged because it can make code harder to debug and understand (spaghetti code). It is better to pass variables to functions and return the updated values.
Placement: The global keyword must be declared before the variable is used inside the function.

Used Claude:
Prompt: "When game is reset from the pause menu the current score is not reset. The boss level only appears on the first game — if the shooter dies the boss levels do not appear again."

Response: "Both bugs are in space_invaders.py. The score isn't being reset in the pause menu restart branch — it's only reset in the game over path. The boss not reappearing is because current_level is never reset when the game restarts, so the level progression logic never runs again properly."

Prompt: "After the boss is defeated the first time it never appears again. Powerups don't disappear when the game is restarted from the pause menu."

Response: "The boss issue is that current_level stays at final_level after the boss is beaten, so on the next playthrough it jumps straight to the winner state. The powerup issue is a typo in the pause restart unpack — the fresh Powerup_Manager is being caught into a variable named powerup_timer instead of powerup_manager, so the old one with lingering powerups keeps being used." 

Prompt: "The player 2 movement is not working at all."

Response: "stddraw only queues one keypress per frame, and player 1's input block is consuming it before player 2 gets a chance. Read the key once and route it to both players in the same block instead of using two separate hasNextKeyTyped() calls."

Denlan Molokwu:
Used Gemini:
Prompt: "The bunkers are working mathematically but are not showing up on the screen, even though the code is there."
Response: Identified a Z-index (draw order) and syntax bug. The bunkers were either being drawn before the background image (causing them to be covered up) or the .draw method was missing parentheses. Advised moving the bunker drawing loop to the very end of the render phase.
prompt:What could i do to fix the aliens and minions bouncing at the same time
 Response: Identify the "short leash" bug. Decouple the minion and alien movement into separate loops with independent speed variables so their wall-collision checks wouldn't cancel each other out.
Used gemini different times to just help me understand the code my teammates coded, just for better understanding too.

Luke Abrahamse:
Used Claude:
Prompt: "Guide me on how to implement a pause menu that has the option that resume restart and go back the main screen. I have a screenmanager class that handles my other screens"

Response:
Add a draw_pause_menu() method to your Screen_Manager that runs its own while True loop — the same pattern you're already using in draw_title_screen(). Return a string like "resume", "restart", or "menu" based on the key pressed. In your main game loop, when "p" is pressed, call choice = screen_manager.draw_pause_menu() and handle the result. For restart, reinitialise everything via your reset_game() function and reset score_manager and current_level. For menu, call main() and return to cleanly restart the call stack.

Prompt: "My shooter can only move once every time i press a key. if i wnat it to keep moving until i press another key, how do I go about that. Dont give me the code guide me to solve it"

Response:
stddraw.hasNextKeyTyped() only captures key press events, not a held state, so movement only triggers once per keypress. To get continuous movement, you need to decouple detecting the keypress from actually moving the shooter.
Store the current movement direction in a variable — call it move_state — and update it when keys are pressed. Pressing "a" should set move_state = "left", pressing "d" sets move_state = "right", and pressing "s" sets move_state = None to stop. This variable just remembers the intended direction, it doesn't move anything yet.
Then, outside the if stddraw.hasNextKeyTyped() block, check move_state every frame and call the appropriate method — so shooter.move_left() if move_state == "left", and shooter.move_right() if move_state == "right". Since this runs every iteration of the game loop regardless of input, the shooter keeps moving until move_state is explicitly changed.
The same approach applies cleanly to your rotation — a rotate_state variable updated by "q", "e", and "w" keys, with shooter.rotate_left() and shooter.rotate_right() called each frame based on its value.

Used Gemini:
Prompts:
"generate a a unique space background for a space invaders game"
"in the same style, generate a background for a pause menu"
"generate a spaceship for the shooter in the exact same style"
"now generate a simple design for an alien spaceship. it should face downwards"

Advanced Features:
Gameplay:
Multi-level progression with increasing difficulty
Boss enemy on the final level, with increased health.
Minion enemy type with faster projectile speed
Enemy health bars that appear when damaged
Bunkers with 5 hit points and colour coded damage states

Combat systems:
Enemies fir back with random probability per frame
Projectile-Bunker Collison that destroys bunkers incrementally

Power Ups:
3 different Power ups(Rapid Fire, Multi-shot and Extra Life)
15% drop rate when killing enemy
Co-op Multiplayer:
2 Player support with separate controls

UI and Screens:
Pause menu with; Resume, Restart, Main Menu, Help, Quit options
Confirmation screen before restart and quit to menu actions
Live score tracking and High Score tracking.

Audio:
Custom sound affects for shooting, taking damage, collecting power ups, game-over and winning.
Shooting sound effects
