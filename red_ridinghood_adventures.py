import random
import arcade
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

WIDTH = 1000
HEIGHT = 650

"Main Menu"
current_screen = "menu"
# play button
play_btn_x = 0
play_btn_y = 1
play_btn_width = 2
play_btn_height = 3
play_btn_clicked: int = 4
play_btn_colour = 5
play_btn_clicked_colour = 6

play_button = [WIDTH/2 - 125, HEIGHT/2, 250, 50, False, arcade.color.BRICK_RED, arcade.color.CADMIUM_RED]

# instruction button
instruction_btn_x = 0
instruction_btn_y = 1
instruction_btn_width = 2
instruction_btn_height = 3
instruction_btn_clicked = 4
instruction_btn_colour = 5
instruction_btn_clicked_colour = 6

instruction_button = [WIDTH/2 - 125, HEIGHT/2 - 100, 250, 50, False, arcade.color.BRICK_RED, arcade.color.CADMIUM_RED]

"Falling Apples Game"
background = arcade.load_texture('images/background.png')

timer = 0.0

apple_scale = 0.02
basket_scale = 0.2

basket_sprite = arcade.Sprite('images/basket.png', basket_scale, center_x=WIDTH/2, center_y=HEIGHT/2)

BASKET_MOVEMENT_SPEED = 50
APPLE_MOVEMENT_SPEED = 2

apples_in_trees_list = arcade.SpriteList()

fallen_apples_counter = 0
apple_caught_counter = 0

i = 0

apple_spawn_counter = 0


"Falling Apples Game Functions"


def stopwatch():
    minutes = int(timer) // 60
    seconds = int(timer) % 60
    output = f"Time: {minutes:02d}:{seconds:02d}"
    arcade.draw_text(output, 50, 20, arcade.color.BLACK, 30)


def create_apples():
    for _ in range(6):
        apple_sprite = arcade.Sprite('images/apple1.png', apple_scale)
        apple_sprite.center_x = random.randint(5, 998)
        apple_sprite.center_y = random.randint(500, 640)
        apples_in_trees_list.append(apple_sprite)


def apple_falling():
    global i
    try:
        falling_apple = apples_in_trees_list[i]
        falling_apple.center_y -= APPLE_MOVEMENT_SPEED
    except IndexError:
        i = 0


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


def apple_spawn():
    global apple_spawn_counter
    create_apples()
    apple_spawn_counter += 1


def apple_falling_speed_increase():
    global APPLE_MOVEMENT_SPEED
    APPLE_MOVEMENT_SPEED += 2


"Menu Functions"


def draw_menu():
    arcade.set_background_color(arcade.color.WHITE_SMOKE)

    if play_button[play_btn_clicked]:
        color = play_button[play_btn_clicked]
    else:
        color = play_button[play_btn_colour]

        # Draw play_button
    arcade.draw_xywh_rectangle_filled(play_button[play_btn_x],
                                      play_button[play_btn_y],
                                      play_button[play_btn_width],
                                      play_button[play_btn_height],
                                      color)

    if instruction_button[instruction_btn_clicked]:
        color = instruction_button[instruction_btn_clicked]
    else:
        color = instruction_button[instruction_btn_colour]

        # Draw instruction_button
    arcade.draw_xywh_rectangle_filled(instruction_button[instruction_btn_x],
                                      instruction_button[instruction_btn_y],
                                      instruction_button[instruction_btn_width],
                                      instruction_button[instruction_btn_height],
                                      color)

    arcade.draw_text("Main Menu", WIDTH / 2, HEIGHT / 2 + 100,
                     arcade.color.BLACK, font_size=30, anchor_x="center")
    arcade.draw_text("Play", WIDTH / 2, HEIGHT / 2 + 15,
                     arcade.color.BLACK, font_size=20, anchor_x="center")
    arcade.draw_text("Instructions", WIDTH / 2, HEIGHT / 2 - 85,
                     arcade.color.BLACK, font_size=20, anchor_x="center")


def draw_instructions():
    arcade.set_background_color(arcade.color.BLUE_GRAY)
    arcade.draw_text("Instructions", WIDTH/2, HEIGHT/2,
                     arcade.color.BLACK, font_size=30)
    arcade.draw_text("ESC to go back", WIDTH/2, HEIGHT/2,
                     arcade.color.BLACK, font_size=20)


def on_draw():
    arcade.start_render()
    if current_screen == "menu":
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
        arcade.draw_text(f"Apple Caught: {int(apple_caught_counter)}", 50, 80, arcade.color.BLACK, 30)


def on_key_press(key, modifiers):
    if key == arcade.key.UP:
        basket_sprite.change_y = BASKET_MOVEMENT_SPEED
    elif key == arcade.key.DOWN:
        basket_sprite.change_y = -BASKET_MOVEMENT_SPEED
    elif key == arcade.key.LEFT:
        basket_sprite.change_x = -BASKET_MOVEMENT_SPEED
    elif key == arcade.key.RIGHT:
        basket_sprite.change_x = BASKET_MOVEMENT_SPEED


def on_key_release(key, modifiers):
    if key == arcade.key.UP:
        basket_sprite.change_y = 0
    elif key == arcade.key.DOWN:
        basket_sprite.change_y = 0
    elif key == arcade.key.LEFT:
        basket_sprite.change_x = 0
    elif key == arcade.key.RIGHT:
        basket_sprite.change_x = 0


def on_mouse_press(x, y, button, modifiers):
    pass


def update(delta_time):
    global timer
    basket_sprite.update()

    stopwatch()
    timer += delta_time

    apple_falling()
    catch_apple()
    if not apples_in_trees_list:
        apple_spawn()
        apple_falling_speed_increase()


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    create_apples()
    arcade.run()


if __name__ == '__main__':
    setup()