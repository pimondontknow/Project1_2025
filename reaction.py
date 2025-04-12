from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)

right_button = Button(15)
left_button = Button(14)

left_name = input('Left player name: ')
right_name = input('Right player name: ')

 def play_round():
    global  game_active, round_count
    round_count += 1
    
    print(f"\n--- Round {round_count}/5 ---")
    
    led.on()
    sleep(uniform(5, 10))
    led.off()

    game_active = True

def pressed(button):
    global  game_active
    if not game_active:
        return

    game_active = False 
if button.pin.number == 14:
        print(f"{left_name} won the game!")
    else:
        print(f"{right_name} won the game!")

right_button.when_pressed = pressed
left_button.when_pressed = pressed

for _ in range(5):
    play_round()
    while game_active: 
        sleep(0.1)
    sleep(1)

led.off()
right_button.close()
left_button.close()
