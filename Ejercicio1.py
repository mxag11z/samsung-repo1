
from gpiozero import LED, Button

led1 = LED(17)  # verde
led2 = LED(1)   # ambar
led3 = LED(3)   # rojo
button = Button(23)

#array de leds
leds = [led1, led2, led3]
leds[0].on()
led_actual = 0
while True:
    if button.is_pressed:
        leds[led_actual].off()  # Apagar el LED actual
        led_actual = (led_actual + 1) % 3  # Cambiar al siguiente LED
        leds[led_actual].on()
