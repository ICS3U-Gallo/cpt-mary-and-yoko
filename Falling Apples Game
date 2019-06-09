import random
import arcade

WIDTH = 1000
HEIGHT = 650

player_x = WIDTH/2
player_y = HEIGHT/2

timer = 0.0

apples_in_trees_list = []
fallen_apples_list = []

fallen_apples_counter = 0
apple_caught_counter = 0

i = 0

# controls
up_is_being_pressed = False
down_is_being_pressed = False
left_pressed = False
right_pressed = False


def stopwatch():
    minutes = int(timer) // 60
    seconds = int(timer) % 60
    output = f"Time: {minutes:02d}:{seconds:02d}"
    arcade.draw_text(output, 300, 300, arcade.color.BLACK, 30)


def create_apples():
    for _ in range(6):
        x = random.randint(5, 998)
        y = random.randint(400, 640)
        apples_in_trees_list.append([x, y])
    #print(apples_in_trees_list)


def apple_counter():
    global fallen_apples_counter, i
    try:
        if apples_in_trees_list[i][1] < 0:
            i += 1
            fallen_apples_counter += 1
        elif apples_in_trees_list[i][1] == player_y and apples_in_trees_list[i][0] == player_x:
            i += 1
            fallen_apples_counter += 1
    except IndexError:
        pass


def apple_falling():
    global fallen_apples_counter
    if fallen_apples_counter == 0:
        apples_in_trees_list[0][1] -= 10
    elif fallen_apples_counter == 1:
        apples_in_trees_list[1][1] -= 10
    elif fallen_apples_counter == 2:
        apples_in_trees_list[2][1] -= 10
    elif fallen_apples_counter == 3:
        apples_in_trees_list[3][1] -= 10
    elif fallen_apples_counter == 4:
        apples_in_trees_list[4][1] -= 10
    elif fallen_apples_counter == 5:
        apples_in_trees_list[5][1] -= 10


def catch_apple():
    global apple_caught_counter, i
    if apples_in_trees_list[i][1] == player_y and apples_in_trees_list[i][0] == player_x:
        apple_caught_counter += 1
        apples_in_trees_list[i][0] = player_x
        apples_in_trees_list[i][1] = player_y

    #print(apple_caught_counter)


def on_draw():
    global apple
    arcade.start_render()
    stopwatch()

    # 6 Apples
    for apple in apples_in_trees_list:
        arcade.draw_circle_filled(apple[0], apple[1], 20, arcade.color.RED)

    # Basket
    arcade.draw_circle_filled(player_x, player_y, 25, arcade.color.BLUE)


def on_key_press(key, modifiers):
    global player_y, player_x, up_is_being_pressed, down_is_being_pressed, left_pressed, right_pressed
    if key == arcade.key.UP:
        up_is_being_pressed = True
    elif key == arcade.key.DOWN:
        down_is_being_pressed = True
    if key == arcade.key.LEFT:
        left_pressed = True
    elif key == arcade.key.RIGHT:
        right_pressed = True


def on_key_release(key, modifiers):
    global player_y, player_x, up_is_being_pressed, down_is_being_pressed, left_pressed, right_pressed
    if key == arcade.key.UP:
        up_is_being_pressed = False
    elif key == arcade.key.DOWN:
        down_is_being_pressed = False
    if key == arcade.key.LEFT:
        left_pressed = False
    elif key == arcade.key.RIGHT:
        right_pressed = False


def on_mouse_press(x, y, button, modifiers):
    pass


def update(delta_time):
    global timer, player_y, player_x, up_is_being_pressed, down_is_being_pressed
    if up_is_being_pressed:
        player_y += 10
    elif down_is_being_pressed:
        player_y -= 10

    if left_pressed:
        player_x -= 10
    elif right_pressed:
        player_x += 10

    #print(player_x)
    #print(player_y)

    stopwatch()
    timer += delta_time

    apple_falling()
    apple_counter()
    print(apples_in_trees_list[0][1])
    catch_apple()


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
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
