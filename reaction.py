from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
right_button = Button(15)
left_button = Button(14)

left_name = input('Left player name: ')
right_name = input('Right player name: ')

def play_game():
    led.on()
    sleep(uniform(5, 10))
    led.off()

def pressed(button):
    if button.pin.number == 14:
        print(f"{left_name} won the game!")
    else:
        print(f"{right_name} won the game!")

    right_button.when_pressed = None
    left_button.when_pressed = None

while True:
    right_button.when_pressed = pressed
    left_button.when_pressed = pressed
    play_game()
    sleep(1)
