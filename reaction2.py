from gpiozero import LED, Button
from time import sleep, time
from random import uniform

led = LED(4)
right_button = Button(15)
left_button = Button(14)

left_name = input('Left player name: ')
right_name = input('Right player name: ')
left_score = 0
right_score = 0
round_count = 0
start_time = 0
game_active = False

def play_round():
    global start_time, game_active, round_count
    round_count += 1
    
    print(f"\n--- Round {round_count}/5 ---")
    print(f"{left_name}: {left_score}  {right_name}: {right_score}")
    
    led.on()
    delay = uniform(5, 10)
    sleep(delay)
    led.off()
    
    start_time = time()
    game_active = True

def pressed(button):
    global left_score, right_score, game_active
    if not game_active:
        return
    
    reaction_time = time() - start_time
    game_active = False
    
    if reaction_time < 0:
        print("Invalid press! Pressed too early!")
        return
    
    winner = left_name if button.pin.number == 14 else right_name
    print(f"{winner} wins! Reaction time: {reaction_time:.2f} seconds")
    
    if button.pin.number == 14:
        left_score += 1
    else:
        right_score += 1


right_button.when_pressed = pressed
left_button.when_pressed = pressed

for _ in range(5):
    play_round()
    while game_active: 
        sleep(0.1)
    sleep(1)  

print("\n=== Final Result ===")
print(f"{left_name}: {left_score}  {right_name}: {right_score}")

if left_score > right_score:
    print(f"{left_name} is the ultimate winner!")
elif right_score > left_score:
    print(f"{right_name} is the ultimate winner!")
else:
    print("It's a tie!")

led.off()
right_button.close()
left_button.close()
 
