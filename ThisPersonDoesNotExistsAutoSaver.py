# pynput module required. Run the this command to install:
# python -m pip install pynput

# Simulate Key Presses in Python tutorial video:
# https://youtu.be/DTnz8wA6wpw

# Full documentation of pynput module.
# https://pynput.readthedocs.io/en/latest/keyboard.html?highlight=f5#pynput.keyboard.Key.f1

# Go to https://thispersondoesnotexist.com/image
# Run the script and click the website where the image is being displayed
# Close terminal to stop script

print('Script will start save loop in 5 seconds.')

from pynput.keyboard import Key, Controller
import time

saved_images_counter = 0

keyboard = Controller()

time.sleep(5) # 5 seconds delay for user to click on the website

print('Script initiated')

def simulate_ctrl_s():
    # Simulates CTRL + S .
    keyboard.press(Key.ctrl)
    keyboard.press('s')
    keyboard.release(Key.ctrl)
    keyboard.release("s")

def simulate_enter():
    # Simulates Enter (saving the image).
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def simulate_f5():
    # Simulates F5. Website refresh to show new image
    keyboard.press(Key.f5)
    keyboard.release(Key.f5)

# Infinite loop to save images
while True:
    simulate_ctrl_s()

    time.sleep(1)

    simulate_enter()

    saved_images_counter += 1
    print('Images saved: ' + str(saved_images_counter))

    time.sleep(1)

    simulate_f5()

    time.sleep(1)
