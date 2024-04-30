from time import time, sleep
from ui import *
from controller import *
from game import Game

class Program:
    def __init__(self):
        self.screen = Screen(30, 25)
        self.game = Game()
        self.controller = Controller()
        self.running = False
    def mainloop(self):
        self.controller.listen()
        now = time()
        last_now = now
        self.running = True
        self.game.start_level(now)
        while self.running:
            sleep(1/60)
            last_now = now
            now = time()
            dt = now-last_now
            # get key
            key = self.controller.get()
            if key == KEYS.CLOSE:
                self.running = False
                break
            # update
            self.game.update(now, dt, key, self.screen)
            # draw
            self.screen.clear()
            self.screen.draw_background(now)
            self.game.draw(self.screen)
            self.screen.update()
            # draw properties
            S1cd = min(max(now-self.game.player.skill1_duration-self.game.player.skill1_started_at, 0), self.game.player.skill1_cooldown)/self.game.player.skill1_cooldown
            S2cd = min(max(now-self.game.player.skill2_duration-self.game.player.skill2_started_at, 0), self.game.player.skill2_cooldown)/self.game.player.skill2_cooldown
            bar_length = 20
            S1amount = int(S1cd*bar_length)
            S2amount = int(S2cd*bar_length)
            S1bar = f"["+S1amount*"/"+(bar_length-S1amount)*"."+"]"
            S2bar = f"["+S2amount*"/"+(bar_length-S2amount)*"."+"]"
            if S1amount == bar_length: S1bar = "["+"@"*bar_length+"]"
            if S2amount == bar_length: S2bar = "["+"@"*bar_length+"]"
            time_passed = int(now-self.game.started_at)
            properties = f"S1: {S1bar}\nS2: {S2bar}\n"
            properties += f"score: "+str(self.game.player.score).ljust(12)+"time: "+str(time_passed)
            print(properties)
