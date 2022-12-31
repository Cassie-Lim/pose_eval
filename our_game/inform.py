import threading
import time
import tkinter
import tkinter.simpledialog


from pacman_main import myGame
import share_var

inform_limit = 10


class inform_you(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.mailbox = queue
    def run(self):
        global inform_limit
        keep_time = 0
        print("Ready to inform you now")
        while(1):
            time.sleep(1)
            a = share_var.getMotionData()
            if(a[1] > 0.1):
                print("呀，怎么头低下去这么多~")
                keep_time = keep_time + 1
            if(keep_time > inform_limit):
                keep_time = 0
                print("Ready to start a game now?[Y/N]")
                reply = tkinter.messagebox.askyesno("低头太久啦，来伸展一下颈椎？")
                if(reply):
                    game = myGame("game", self.mailbox)
                    game.start()
                    game.join()