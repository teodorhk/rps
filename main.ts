let result = 0
input.onGesture(Gesture.Shake, function () {
    result = randint(1, 3)
    if (result == 1) {
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
    } else {
        if (result == 2) {
            basic.showLeds(`
                . . . . .
                . # # # .
                . # # # .
                . # # # .
                . . . . .
                `)
        } else {
            basic.showLeds(`
                . # . # .
                . . # . .
                . # . # .
                # # . # #
                # # . # #
                `)
        }
    }
    basic.pause(1000)
    basic.clearScreen()
})
basic.forever(function () {
    basic.pause(5000)
})
