import arcade

WIDTH = 1000
HEIGHT = 650

current_screen = "menu"

ball_x = 0

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


def update(delta_time):
    global ball_x

    if current_screen == "play":
        ball_x += 1


def on_draw():
    arcade.start_render()
    # Draw in here...
    if current_screen == "menu":
        draw_menu()
    elif current_screen == "instructions":
        draw_instructions()
    elif current_screen == "play":
        draw_play()


def on_key_press(key, modifiers):
    if current_screen == "instructions":
        pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global current_screen
    if current_screen == "menu":
        # When play_button is clicked
        if (play_button[play_btn_x] < x < play_button[play_btn_x] + play_button[play_btn_width] and
                play_button[play_btn_y] < y < play_button[play_btn_y] + play_button[play_btn_height]):
            play_button[play_btn_clicked] = True
            #GO TO GAME
        # When instruction_button is clicked
        if (instruction_button[instruction_btn_x] < x < instruction_button[instruction_btn_x] + instruction_button[instruction_btn_width] and
                instruction_button[instruction_btn_y] < y < instruction_button[instruction_btn_y] + instruction_button[
                    instruction_btn_height]):
            instruction_button[instruction_btn_clicked] = True
            current_screen = "instructions"


def on_mouse_release(x, y, button, modifiers):
    global current_screen
    # When you let go of the mouse, all buttons should be set to False.
    if play_button[play_btn_clicked]:
        #Go to game
        play_button[play_btn_clicked] = False

    if instruction_button[instruction_btn_clicked]:
        instruction_button[instruction_btn_clicked] = False


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

    arcade.run()


def draw_menu():
    arcade.set_background_color(arcade.color.WHITE_SMOKE)

    # arcade.draw_text("Main Menu", WIDTH/2, HEIGHT/2 + 100,
    #                  arcade.color.BLACK, font_size=30)
    # arcade.draw_text("Instructions", WIDTH/2, HEIGHT/2-80,
    #                  arcade.color.BLACK, font_size=20)
    # arcade.draw_text("Play", WIDTH/2, HEIGHT/2 - 10,
    #                  arcade.color.BLACK, font_size=20)

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


def draw_play():
    arcade.set_background_color(arcade.color.ORANGE_RED)
    arcade.draw_text("Play", WIDTH/2, HEIGHT/2,
                     arcade.color.BLACK, font_size=30, anchor_x="center")

    arcade.draw_circle_filled(ball_x, 100, 30, arcade.color.WHITE)


if __name__ == '__main__':
    setup()
