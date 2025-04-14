from gpiozero import LED

led = LED(20)
led.blink()
input("Press ENTER to exit..")
