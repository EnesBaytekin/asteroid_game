from msvcrt import getch
from _thread import start_new_thread
from controller.keys import *

class Controller:
    def __init__(self):
        self.key = KEYS.NONE
        self.listening = False
    def update(self):
        key = getch()
        if key in [KEYS.LEFT, KEYS.DOWN, KEYS.RIGHT, KEYS.SHOOT, KEYS.SKILL_1, KEYS.SKILL_2, KEYS.CLOSE]:
            self.key = key
        else:
            self.key = KEYS.NONE
    def listen(self):
        def listen():
            self.listening = True
            while self.listening:
                self.update()
        start_new_thread(listen, ())
    def get(self):
        key = self.key
        self.key = KEYS.NONE
        return key