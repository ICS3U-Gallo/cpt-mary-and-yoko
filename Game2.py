import random
import arcade
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

# Width and height of the screen
WIDTH = 1000
HEIGHT = 650

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
    3. After every 6 apples, they will fall faster every time
    Level 2: Red Riding Hood is on the run from the Wolf!
    1. Use the arrow keys to move left and right, 
        avoiding the obstacles.
    2. Gain points by collecting apples
    3. Lose points if Red Riding Hood runs into a log.
    4. Red Riding hood will drown 
        if she falls into the water, and the game will end.
        
    Press Enter to continue...''',
                     WIDTH / 2, HEIGHT / 2, arcade.color.BLACK, font_size=20, anchor_x="center", anchor_y="center")


# If player does not catch 50 apples in 60 seconds, the game is over and this function displays a message
def falling_apples_game_over():
    arcade.draw_texture_rectangle(WIDTH // 2, HEIGHT // 2, WIDTH, HEIGHT, background)
    wolf_sprite.draw()
    arcade.draw_text('''
                    Game Over :( 
                    
                    You fell into the river and 
                    drowned. The wolf came and ate you.
                    
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
    arcade.draw_texture_rectangle(WIDTH // 2, HEIGHT // 2, WIDTH, HEIGHT, background)
    wolf_sprite.draw()
    arcade.draw_text('''
                    Game Over :( 
                    
                    You fell into the river and 
                    drowned. The wolf came and ate you.
                    
                    Press ESC to go back.''',
                     WIDTH / 2 - 100, HEIGHT / 2 + 100, arcade.color.BLACK, font_size=20, anchor_x="center", anchor_y="center")
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



def on_key_press(key, modifiers):
    global current_screen
    if current_screen == "instructions":
        instructions_keybinds(key, modifiers)

    #For level 2 game
    if current_screen == "running_game":
        if key == arcade.key.LEFT:
            player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            player_sprite.change_x = PLAYER_MOVEMENT_SPEED


def instructions_keybinds(key, modifiers):
    global current_screen
    if key == arcade.key.ENTER:
        current_screen = "running_game"

def on_key_release(key, modifiers):      
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
    global current_screen,
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

        if int(timer) % 60 == 2:
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
    if current_screen == "running_game":
        arcade.set_background_color(arcade.color.LIGHT_GREEN)
        ponds.draw()
        logs.draw()
        apples.draw()
        player_sprite.draw()
        arcade.draw_text(f"Apples Caught: {int(score)}", 50, 600, arcade.color.ANTIQUE_WHITE, 30)
    elif current_screen == "game_over":
        draw_game_over()
    elif current_screen == "success game over":
        draw_success_apple_run()


if __name__ == '__main__':
    setup()
