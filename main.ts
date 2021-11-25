radio.onReceivedNumber(function (receivedNumber) {
    received_number = receivedNumber
    if (received_number == 1) {
        basic.showLeds(`
            . . # . .
            . # . # .
            # # # # #
            # . . . #
            # . . . #
            `)
        strip.setPixelColor(counter, neopixel.colors(NeoPixelColors.Red))
        strip.show()
        basic.pause(100)
        Rainbow()
        counter = counter + received_number
    } else if (received_number == -1) {
        basic.showLeds(`
            # # # # .
            # . . . #
            # # # # .
            # . . . #
            # # # # .
            `)
        counter = counter + received_number
        strip.setPixelColor(counter, neopixel.colors(NeoPixelColors.Yellow))
        strip.show()
        basic.pause(100)
        Rainbow()
    } else if (received_number == 99) {
        basic.showLeds(`
            # # . # #
            # # . # #
            # # # # #
            . # # # .
            . . # . .
            `)
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
        strip.show()
        basic.pause(100)
        counter = 0
    } else {
    	
    }
})
function Rainbow () {
    strip.showRainbow(1, 360)
    strip.show()
    basic.pause(200)
    index = counter
    while (index <= 23) {
        strip.setPixelColor(index + 1, neopixel.colors(NeoPixelColors.Black))
        strip.show()
        index = index + 1
    }
}
let index = 0
let counter = 0
let received_number = 0
let strip: neopixel.Strip = null
radio.setGroup(33)
strip = neopixel.create(DigitalPin.P11, 24, NeoPixelMode.RGB)
strip.setBrightness(50)
strip.showColor(neopixel.colors(NeoPixelColors.Black))
strip.show()
basic.forever(function () {
	
})
