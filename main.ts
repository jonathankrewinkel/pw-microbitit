input.onButtonPressed(Button.A, function on_button_pressed_a() {
    while (true) {
        basic.showIcon(IconNames.Heart)
        basic.showIcon(IconNames.SmallHeart)
    }
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showLeds(`
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    `)
    music.playMelody("G C B - - - - - ", 120)
    music.playMelody("G C B - - - - - ", 120)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    if (random == 0) {
        basic.showIcon(IconNames.Sad)
    }
    
    if (random == 1) {
        basic.showIcon(IconNames.Happy)
    }
    
})
input.onSound(DetectedSound.Loud, function on_sound_loud() {
    basic.showLeds(`
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    `)
    basic.pause(2000)
    basic.clearScreen()
})
let random = 0
random = randint(0, 1)
