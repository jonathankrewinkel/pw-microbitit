def on_button_pressed_a():
    while True:
        basic.show_icon(IconNames.HEART)
        basic.show_icon(IconNames.SMALL_HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    """)
    music.play_melody("G C B - - - - - ", 120)
    music.play_melody("G C B - - - - - ", 120)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    if random == 0:
        basic.show_icon(IconNames.SAD)
    if random == 1:
        basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_sound_loud():
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    basic.pause(2000)
    basic.clear_screen()
input.on_sound(DetectedSound.LOUD, on_sound_loud)

random = 0
random = randint(0, 1)