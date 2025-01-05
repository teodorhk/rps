result = 0

def on_gesture_shake():
    global result
    result = randint(1, 3)
    if result == 1:
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
    else:
        if result == 2:
            basic.show_leds("""
                . . . . .
                . # # # .
                . # # # .
                . # # # .
                . . . . .
                """)
        else:
            basic.show_leds("""
                . # . # .
                . . # . .
                . # . # .
                # # . # #
                # # . # #
                """)
    basic.pause(1000)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    basic.pause(1000)
    basic.show_icon(IconNames.HEART)
    basic.pause(100)
    basic.clear_screen()
basic.forever(on_forever)
