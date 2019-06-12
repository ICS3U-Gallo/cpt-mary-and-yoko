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
score = 0
player_sprite = arcade.Sprite('images/girl.png', CHARACTER_SCALING, center_x=WIDTH/6, center_y=HEIGHT/4,)


apples = arcade.SpriteList()
logs = arcade.SpriteList()
ponds = arcade.SpriteList()


def positions():
    global score
    for i in range(3):
        pond = arcade.Sprite('images/pond.png', pond_scale)
        pond.center_x = random.randrange(WIDTH)
        pond.center_y = random.randrange(HEIGHT)
        ponds.append(pond)

    for i in range(5):
        log = arcade.Sprite('images/logs.png', log_Scale)
        log.center_x = random.randrange(WIDTH)
        log.center_y = random.randrange(HEIGHT)
        logs.append(log)

    for i in range(50):
        apple = arcade.Sprite('images/845418.png', apple_Scale)
        apple.center_x = random.randrange(WIDTH)
        apple.center_y = random.randrange(HEIGHT)
        apples.append(apple)

    for apple in apples:
        if apple.center_y == 0:
            apple.center_y = random.randrange(HEIGHT)
            apple.center_x = random.randrange(WIDTH)

def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.LIGHT_GREEN)
    arcade.schedule(update, 1/60)

    window = arcade.get_window()
    positions()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    arcade.run()



def update(delta_time):
    player_sprite.update()

    for apple in apples:
        apple.center_y -= 2


    for log in logs:
        log.center_y -= 2

    for pond in ponds:
        pond.center_y -=2

    global score
    apples_list = arcade.check_for_collision_with_list(player_sprite, apples)
    for apple in apples_list:
        apple.kill()
        score += 1

    logs_list = arcade.check_for_collision_with_list(player_sprite, logs)
    for log in logs_list:
        log.kill()
        score -=1


    print(score)

def on_draw():
    arcade.start_render()
    # Draw in here...

    ponds.draw()



    apples.draw()

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
