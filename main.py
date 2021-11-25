def on_received_number(receivedNumber):
    global received_number, counter
    received_number = receivedNumber
    basic.show_number(receivedNumber)
    basic.pause(100)
    if received_number == 1:
        basic.show_leds("""
            . . # . .
                        . # . # .
                        # # # # #
                        # . . . #
                        # . . . #
        """)
        strip.set_pixel_color(counter, neopixel.colors(NeoPixelColors.RED))
        strip.show()
        basic.pause(500)
        Rainbow()
        counter = counter + received_number
    elif received_number == -1:
        basic.show_leds("""
            # # # # .
                        # . . . #
                        # # # # .
                        # . . . #
                        # # # # .
        """)
        counter = counter + received_number
        strip.set_pixel_color(counter, neopixel.colors(NeoPixelColors.YELLOW))
        strip.show()
        basic.pause(500)
        Rainbow()
    elif received_number == 99:
        basic.show_leds("""
            # # . # #
                        # # . # #
                        # # # # #
                        . # # # .
                        . . # . .
        """)
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        strip.show()
        basic.pause(500)
        counter = 0
    else:
        pass
radio.on_received_number(on_received_number)

def Rainbow():
    strip.show_rainbow(1, 360)
    strip.show()
    basic.pause(500)
    index = 0
    while index <= counter:
        strip.set_pixel_color(index, neopixel.colors(NeoPixelColors.BLACK))
        strip.show()
        index += 1
counter = 0
received_number = 0
strip: neopixel.Strip = None
radio.set_group(33)
strip = neopixel.create(DigitalPin.P11, 24, NeoPixelMode.RGB)
strip.set_brightness(50)
strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
strip.show()

def on_forever():
    pass
basic.forever(on_forever)
