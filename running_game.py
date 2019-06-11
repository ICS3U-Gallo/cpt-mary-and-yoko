import os
import arcade
import random

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

WIDTH = 1000
HEIGHT = 650
CHARACTER_SCALING = 0.08
PLAYER_MOVEMENT_SPEED = 5
apple_Scale = 0.03
log_Scale = 0.2
pond_scale = 0.2

player_sprite = arcade.Sprite('images/girl.png', CHARACTER_SCALING, center_x=WIDTH/6, center_y=HEIGHT/4,)


apples = arcade.SpriteList()
logs = arcade.SpriteList()
pond = arcade.SpriteList()


apples_x_positions = []
apples_y_positions = []
logs_x_positions = []
logs_y_positions = []
pond_x_positions = []
pond_y_positions = []


def positions():
    for _ in range(3):
        x = random.randrange(0, WIDTH)
        y = random.randrange(HEIGHT, HEIGHT * 2)
        pond_x_positions.append(x)
        pond_y_positions.append(y)

    for _ in range(1):
        x = random.randrange(0, WIDTH)
        y = random.randrange(HEIGHT, HEIGHT * 2)
        logs_x_positions.append(x)
        logs_y_positions.append(y)

    for _ in range(20):
        x = random.randrange(0, WIDTH)
        y = random.randrange(HEIGHT, HEIGHT * 2)
        apples_x_positions.append(x)
        apples_y_positions.append(y)


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.LIGHT_GREEN)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    positions()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    arcade.run()


def update(delta_time):
    score = 0
    # By default, adds the sprite's speed to its location
    # creating movement.
    player_sprite.update()
    for index in range(len(apples_y_positions)):
        apples_y_positions[index] -= 2

        if apples_y_positions[index] < 0:
            apples_y_positions[index] = random.randrange(HEIGHT, HEIGHT+50)
            apples_x_positions[index] = random.randrange(0, WIDTH)

    for index in range(len(logs_y_positions)):
        logs_y_positions[index] -= 2

        if logs_y_positions[index] < 0:
            logs_y_positions[index] = random.randrange(HEIGHT, HEIGHT+50)
            logs_x_positions[index] = random.randrange(0, WIDTH)

    for index in range(len(pond_y_positions)):
        pond_y_positions[index] -= 2

        if pond_y_positions[index] < 0:
            pond_y_positions[index] = random.randrange(HEIGHT, HEIGHT+50)
            pond_x_positions[index] = random.randrange(0, WIDTH)

def on_draw():
    arcade.start_render()
    # Draw in here...
    for x, y in zip(pond_x_positions, pond_y_positions):
        pond = arcade.Sprite('images/pond.png', pond_scale, center_y=y, center_x=x)
        pond.draw()

    for x, y in zip(apples_x_positions, apples_y_positions):
        apples = arcade.Sprite('images/845418.png', apple_Scale, center_y=y, center_x=x)
        apples.draw()

    for x, y in zip(logs_x_positions, logs_y_positions):
        logs = arcade.Sprite('images/logs.png', log_Scale, center_y=y, center_x=x)
        logs.draw()
    player_sprite.draw()


def on_key_press(key, modifiers):
    if key == arcade.key.LEFT:
        player_sprite.change_x = -PLAYER_MOVEMENT_SPEED

    elif key == arcade.key.RIGHT:
        player_sprite.change_x = PLAYER_MOVEMENT_SPEED


def on_key_release(key, modifiers):
    if key == arcade.key.LEFT:
        player_sprite.change_x = 0

    elif key == arcade.key.RIGHT:
        player_sprite.change_x = 0


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()
