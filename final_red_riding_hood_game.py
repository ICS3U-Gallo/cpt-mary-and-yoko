import random
import arcade
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

# Width and height of the screen
WIDTH = 1000
HEIGHT = 650

# Start up for the stopwatch that will increase as time goes on
timer = 0.0

"Main Menu"
# Variable for the menu screen (will have other screens assigned to it (level one and two and instructions)
current_screen = "menu"

# Uploaded background for the menu
menu_background = arcade.load_texture('images/menu_background.jpg')
home_background = arcade.load_texture('images/home_background.jpg')
red_riding_sprite = arcade.Sprite('images/littleRed.png', 0.2, center_x=WIDTH/2 + 200, center_y=HEIGHT/2 - 50)
wolf_sprite = arcade.Sprite('images/wolf.png', 0.2, center_x=WIDTH / 2 + 200, center_y=HEIGHT / 2 - 50)

# play button in the menu
play_btn_x = 0
play_btn_y = 1
play_btn_width = 2
play_btn_height = 3
play_btn_clicked: int = 4
play_btn_colour = 5
play_btn_clicked_colour = 6

play_button = [WIDTH/2 - 125, HEIGHT/4 - 15, 250, 50, False, arcade.color.BRICK_RED, arcade.color.CADMIUM_RED]


"Menu Functions"

# Drawing for menu buttons/ texts
def draw_menu():
    arcade.set_background_color(arcade.color.WHITE_SMOKE)

    # Draw play_button
    arcade.draw_xywh_rectangle_filled(play_button[play_btn_x],
                                      play_button[play_btn_y],
                                      play_button[play_btn_width],
                                      play_button[play_btn_height],
                                      arcade.color.APPLE_GREEN)


    # Texts on main menu
    arcade.draw_rectangle_filled(WIDTH / 2, HEIGHT / 2 + 170, 500, 70, arcade.color.LIGHT_GREEN)
    arcade.draw_text("Red Riding Hood Adventures", WIDTH / 2, HEIGHT / 2 + 150,
                     arcade.color.BLACK, font_size=30, anchor_x="center")
    arcade.draw_text("Play", WIDTH / 2, HEIGHT / 4,
                     arcade.color.BLACK, font_size=20, anchor_x="center")


def draw_instructions():
    arcade.draw_texture_rectangle(WIDTH // 2, HEIGHT // 2, WIDTH, HEIGHT, menu_background)
    arcade.draw_rectangle_filled(WIDTH / 2, HEIGHT / 2, 600, 400, arcade.color.LIGHT_GREEN)
    arcade.draw_rectangle_filled(WIDTH / 2, HEIGHT / 2 + 300, 200, 100, arcade.color.LIGHT_GREEN)
    arcade.draw_text("Instructions", WIDTH / 2, 600,
                     arcade.color.BLACK, font_size=30, anchor_x="center")

    arcade.draw_text('''
    Level 1: Catch the falling apples for Grandma!
    1. Move the basket around with the arrow keys
    2. 50 apples must be caught to advance 
    to next level before 60 seconds
    3. After every 6 apples, they will fall faster

    Level 2: Red Riding Hood is on the run from the Wolf!
    1. Use the arrow keys to move left and right, 
        avoiding the obstacles.
    2. Gain points by collecting apples
    3. Lose points if Red Riding Hood runs into a log.
    4. Red Riding hood will drown 
        if she falls into the water, and the game will end.
    5. Game ends if you survive for 1 minute
        
    Press Enter to continue...''',
                     WIDTH / 2, HEIGHT / 2, arcade.color.BLACK, font_size=20, anchor_x="center", anchor_y="center")


"Falling Apples Game Setup"

# Falling apples game background
background = arcade.load_texture('images/background.png')

# Apple and basket sprite scales
apple_scale = 0.02
basket_scale = 0.2

# Basket sprite drawing
basket_sprite = arcade.Sprite('images/basket.png', basket_scale, center_x=WIDTH/2, center_y=HEIGHT/2)

# Apples and basket speed when in movement
BASKET_MOVEMENT_SPEED = 10
APPLE_MOVEMENT_SPEED = 2

# List of the 6 apples in the trees
apples_in_trees_list = arcade.SpriteList()

apple_caught_counter = 0

# Counter for going through the apples_in_trees_list
# (as the apples list will decrease when it falls, counter resets to 0 when 6 apples are gone)
i = 0

apple_spawn_counter = 0


"Falling Apples Game Functions"


# stopwatch that counts the time
def stopwatch():
    minutes = int(timer) // 60
    seconds = int(timer) % 60
    output = f"Time: {minutes:02d}:{seconds:02d}"
    arcade.draw_text(output, 50, 20, arcade.color.BLACK, 30)

# function that creates the positions (x and y coords) of the 6 apples
def create_apples():
    for _ in range(6):
        apple_sprite = arcade.Sprite('images/apple1.png', apple_scale)
        apple_sprite.center_x = random.randint(5, 998)
        apple_sprite.center_y = random.randint(500, 640)
        apples_in_trees_list.append(apple_sprite)

# Allows the apples to fall one at a time according to the apple movement speed
def apple_falling():
    global i
    try:
        falling_apple = apples_in_trees_list[i]
        falling_apple.center_y -= APPLE_MOVEMENT_SPEED
    except IndexError:
        i = 0

# Allows apple to disappear once it hits the floor or when it is caught by the basket
def catch_apple():
    global apple_caught_counter, i
    try:
        falling_apple = apples_in_trees_list[i]
        apples_list = arcade.check_for_collision(basket_sprite, falling_apple)
        if apples_list:
            falling_apple.kill()
            apple_caught_counter += 1
            i += 1
        else:
            if falling_apple.center_y < 0:
                falling_apple.kill()
                i += 1
    except IndexError:
        i = 0

# Function that spawns the apples again once the 6 apples have all disappeared
def apple_spawn():
    global apple_spawn_counter
    create_apples()
    apple_spawn_counter += 1

# Increases falling speed of the apples after each spawn
def apple_falling_speed_increase():
    global APPLE_MOVEMENT_SPEED
    APPLE_MOVEMENT_SPEED += 2

# Displays the number of apples caught
def apple_counter():
    arcade.draw_text(f"Apple Caught: {int(apple_caught_counter)}", 50, 80, arcade.color.BLACK, 30)

# If 50 apples are caught, this function tells the player
def success():
    arcade.draw_texture_rectangle(WIDTH // 2, HEIGHT // 2, WIDTH, HEIGHT, background)
    arcade.draw_rectangle_filled(WIDTH / 2, HEIGHT / 2, 600, 400, arcade.color.LIGHT_GREEN)
    arcade.draw_text('''Congratulations! 
    
    You have caught enough 
    apples for Red Riding Hood. 
    However, the Wolf will be coming to 
    chase you soon so you better run!

    Press Enter to continue.''',
                     WIDTH / 2, HEIGHT / 2, arcade.color.BLACK, font_size=20, align="center", anchor_x="center", anchor_y="center")

# If player does not catch 50 apples in 60 seconds, the game is over and this function displays a message
def falling_apples_game_over():
    arcade.draw_texture_rectangle(WIDTH // 2, HEIGHT // 2, WIDTH, HEIGHT, background)
    wolf_sprite.draw()
    arcade.draw_text('''
                    Game Over :( 
                    
                    The Wolf came and you did 
                    not catch enough apples
                    
                    Press ESC to go back.''',
                     WIDTH / 2 - 100, HEIGHT / 2 + 100, arcade.color.BLACK, font_size=20, anchor_x="center", anchor_y="center")


# Set up variables for the second level
"Running Game"

CHARACTER_SCALING = 1
PLAYER_MOVEMENT_SPEED = 5
apple_Scale = 0.01
log_Scale = 0.2
pond_scale = 0.1
score = 0
player_sprite = arcade.Sprite('images/girl.png', CHARACTER_SCALING, center_x=WIDTH/6, center_y=HEIGHT/4,)

# Lists for the objects in the game
apples = arcade.SpriteList()
logs = arcade.SpriteList()
ponds = arcade.SpriteList()

"Running Game Functions"

# Sets random positions (x, y coords) for the ponds
def pond_draw():
    for i in range(1):
        pond = arcade.Sprite('images/water.png', pond_scale)
        pond.center_x = random.randint(0, WIDTH)
        pond.center_y = HEIGHT
        ponds.append(pond)
        #pond.draw()

# Sets random positions (x, y coords) for the logs
def log_draw():
    for i in range(5):
        log = arcade.Sprite('images/logs.png', log_Scale)
        log.center_x = random.randrange(WIDTH)
        log.center_y = HEIGHT
        logs.append(log)
        #log.draw()

# Sets random positions (x, y coords) for the apples
def apple_draw():
    for i in range(50):
        apple = arcade.Sprite('images/apple.jpg', apple_Scale)
        apple.center_x = random.randrange(WIDTH)
        apple.center_y = HEIGHT
        apples.append(apple)
        #apple.draw()


# Resets the apple's positions after it goes down the screen
def reset(apple):
    for _ in range(50):
        apple.center_y = random.randrange(HEIGHT + 20, HEIGHT + 100)
        apple.center_x = random.randrange(WIDTH)


# Game over function for when player touches the pond
def draw_game_over():
    global score
    arcade.set_background_color(arcade.color.RED)
    arcade.draw_text("Game Over", WIDTH / 2, HEIGHT / 2,
                     arcade.color.BLACK, font_size=30, anchor_x="center")
    arcade.draw_text("You fell into the water and drowned.", WIDTH / 2, HEIGHT / 2 - 60,
                     arcade.color.BLACK, font_size=20, anchor_x="center")
    arcade.draw_text(f"Final score: {score}", WIDTH / 2, HEIGHT / 2 - 120,
                     arcade.color.BLACK, font_size=20, anchor_x="center")


def draw_success_apple_run():
    arcade.draw_texture_rectangle(WIDTH // 2, HEIGHT // 2, WIDTH, HEIGHT, home_background)
    arcade.draw_rectangle_filled(WIDTH / 2, 20, 900, 150, arcade.color.LIGHT_GREEN)
    red_riding_sprite.draw()
    arcade.draw_text('''Congrats! You have successfully brought 
    Red Riding Hood safely to Grandma's and many apples for Grandma!''', WIDTH/2, 20,
                     arcade.color.BLACK, font_size=25, align="center", anchor_x="center")



"The Merging of Level 1 and 2 + Menu"


def on_key_press(key, modifiers):
    global current_screen
    if current_screen == "instructions":
        instructions_keybinds(key, modifiers)

    # Falling apples game:
    # Arrow keys for moving the basket around
    if current_screen == "play falling apples game":
        if key == arcade.key.UP:
            basket_sprite.change_y = BASKET_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            basket_sprite.change_y = -BASKET_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            basket_sprite.change_x = -BASKET_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            basket_sprite.change_x = BASKET_MOVEMENT_SPEED
    # When falling apples game is failed, apple_game_over_keybinds(key, modifiers) called
    if current_screen == "game over falling apples":
        apple_game_over_keybinds(key, modifiers)

    if current_screen == "success falling apples":
        apple_game_success_keybinds(key, modifiers)

    #For level 2 game, moves player side to side
    if current_screen == "running_game":
        if key == arcade.key.LEFT:
            player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            player_sprite.change_x = PLAYER_MOVEMENT_SPEED


def instructions_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.ENTER:
        current_screen = "play falling apples game"


def apple_game_over_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.ESCAPE:
        current_screen = "menu"


def apple_game_success_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.ENTER:
        current_screen = "running_game"


def on_key_release(key, modifiers):
    if current_screen == "play falling apples game":
        if key == arcade.key.UP:
            basket_sprite.change_y = 0
        elif key == arcade.key.DOWN:
            basket_sprite.change_y = 0
        elif key == arcade.key.LEFT:
            basket_sprite.change_x = 0
        elif key == arcade.key.RIGHT:
            basket_sprite.change_x = 0
       
    if current_screen == "running_game":
        if key == arcade.key.LEFT:
            player_sprite.change_x = 0
        elif key == arcade.key.RIGHT:
            player_sprite.change_x = 0
   

def on_mouse_press(x, y, button, modifiers):
    global current_screen
    if current_screen == "menu":
        # When play_button is clicked
        if (play_button[play_btn_x] < x < play_button[play_btn_x] + play_button[play_btn_width] and
                play_button[play_btn_y] < y < play_button[play_btn_y] + play_button[play_btn_height]):
            play_button[play_btn_clicked] = True
            current_screen = "instructions"


def on_mouse_release(x, y, button, modifiers):
    # When you let go of the mouse, all buttons should be set to False.
    if play_button[play_btn_clicked]:
        play_button[play_btn_clicked] = False


def update(delta_time):
    global current_screen, timer
    # For falling apples game
    if current_screen == "play falling apples game":
        # Draw basket sprite
        basket_sprite.update()
        # Updates timer as every second passes
        stopwatch()
        timer += delta_time

        apple_falling()
        catch_apple()
        # When apples in trees list is empty, 6 apples will spawn again
        if not apples_in_trees_list:
            apple_spawn()
            # After each spawn, it will increase the falling apple's speed
            apple_falling_speed_increase()
        # When the player catches 50 apples, the game ends and proceeds to next game
        if apple_caught_counter == 50:
            current_screen = "success falling apples"
        # If player does not catch 50 apples in 60 seconds, the game will end and go back to main menu
        elif apple_caught_counter < 50 and int(timer) % 60 == 60:
            current_screen = "game over falling apples"

    if current_screen == "running_game":
        player_sprite.update()
        global score, ponds

        stopwatch()
        timer += delta_time

        for pond in ponds:
            pond.center_y -= 1
            if pond.top < 0:
                reset(pond)

        for log in logs:
            log.center_y -= 1
            if log.top < 0:
                reset(log)

        for apple in apples:
            apple.center_y -= 1
            if apple.top < 0:
                reset(apple)

        apples_list = arcade.check_for_collision_with_list(player_sprite, apples)
        for apple in apples_list:
            apple.kill()
            score += 1

        logs_list = arcade.check_for_collision_with_list(player_sprite, logs)
        for log in logs_list:
            log.kill()
            score -= 1

        ponds_list = arcade.check_for_collision_with_list(player_sprite, ponds)
        for _ in ponds_list:
            #exit()
            current_screen = "game_over"

        if int(timer) // 60 == 1:
            current_screen = "success game over"


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    if current_screen == "running_game":
        pond_draw()
        log_draw()
        apple_draw()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    if current_screen == "play falling apples game":
        create_apples()
    
    arcade.run()


def on_draw():
    global player_sprite, red_riding_sprite
    arcade.start_render()
    if current_screen == "menu":
        arcade.draw_texture_rectangle(WIDTH // 2, HEIGHT // 2, WIDTH, HEIGHT, menu_background)
        red_riding_sprite.draw()
        draw_menu()
    elif current_screen == "instructions":
        draw_instructions()
    elif current_screen == "play falling apples game":
        arcade.draw_texture_rectangle(WIDTH // 2, HEIGHT // 2, WIDTH, HEIGHT, background)
        # Timer on screen
        stopwatch()
        # 6 Apples
        for apple in apples_in_trees_list:
            apple.draw()
        # Basket
        basket_sprite.draw()
        # Apple Caught Counter
        apple_counter()
    elif current_screen == "game over falling apples":
        falling_apples_game_over()
    elif current_screen == "success falling apples":
        success()

    if current_screen == "running_game":
        arcade.set_background_color(arcade.color.LIGHT_GREEN)
        pond_draw()
        ponds.draw()
        log_draw()
        logs.draw()
        apple_draw()
        apples.draw()
        player_sprite.draw()
        arcade.draw_text(f"Apples Caught: {int(score)}", 50, 600, arcade.color.ANTIQUE_WHITE, 30)
    elif current_screen == "game_over":
        draw_game_over()
    elif current_screen == "success game over":
        draw_success_apple_run()


if __name__ == '__main__':
    setup()
