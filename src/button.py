from gpiozero import LED, Button

led = LED(20)
led.on()

button = Button(25)

button.when_pressed = led.off
button.when_released = led.on   

input("Press ENTER to exit..")


