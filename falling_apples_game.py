import random
import arcade
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

timer = 0.0

WIDTH = 1000
HEIGHT = 650

apple_scale = 0.02
basket_scale = 0.2

basket_sprite = arcade.Sprite('images/basket.png', basket_scale, center_x=WIDTH/2, center_y=HEIGHT/2)

BASKET_MOVEMENT_SPEED = 10
APPLE_MOVEMENT_SPEED = 2

apples_in_trees_list = arcade.SpriteList()
fallen_apples_list = arcade.SpriteList()

fallen_apples_counter = 0
apple_caught_counter = 0

i = 0

apple_spawn_counter = 0


def stopwatch():
    minutes = int(timer) // 60
    seconds = int(timer) % 60
    output = f"Time: {minutes:02d}:{seconds:02d}"
    arcade.draw_text(output, 50, 20, arcade.color.BLACK, 30)


def create_apples():
    for _ in range(6):
        apple_sprite = arcade.Sprite('images/apple1.png', apple_scale)
        apple_sprite.center_x = random.randint(5, 998)
        apple_sprite.center_y = random.randint(400, 640)
        apples_in_trees_list.append(apple_sprite)


def apple_counter():
    global fallen_apples_counter, i
    try:
        #apple_falling()
        falling_apple = apples_in_trees_list[i]
        if falling_apple.center_y < 0:
            i += 1
            fallen_apples_counter += 1
            falling_apple.kill()
        # elif falling_apple.center_y == basket_sprite.center_y and falling_apple.center_x == basket_sprite.center_x:
        #     i += 1
        #     fallen_apples_counter += 1
    except IndexError:
        pass


def apple_falling():
    try:
        falling_apple = apples_in_trees_list[i]
        falling_apple.center_y -= APPLE_MOVEMENT_SPEED
    except IndexError:
        pass


def catch_apple():
    global apple_caught_counter
    try:
        falling_apple = apples_in_trees_list[i]
        apples_list = arcade.check_for_collision(basket_sprite, falling_apple)
        if apples_list:
            falling_apple.kill()
            #fallen_apples_list.append(falling_apple)
            apple_caught_counter += 1
    except IndexError:
        pass


def apple_spawn():
    global apple_spawn_counter, i
    i = 0
    create_apples()
    apple_spawn_counter += 1


def apple_falling_speed_increase():
    global APPLE_MOVEMENT_SPEED
    if apple_spawn_counter:
        APPLE_MOVEMENT_SPEED += 5


def on_draw():
    arcade.start_render()
    # Timer on screen
    stopwatch()
    #apple_counter()

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
    apple_counter()
    if not apples_in_trees_list:
        apple_spawn()
    #apple_falling_speed_increase()


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
