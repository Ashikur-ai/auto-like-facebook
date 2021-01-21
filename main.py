from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
time.sleep(5)
while True:
    keyboard.press('j')
    keyboard.release('j')

    keyboard.press('l')
    keyboard.release('l')
    time.sleep(3)
    #press enter
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)