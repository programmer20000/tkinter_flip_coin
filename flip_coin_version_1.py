from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class FLIP_COIN(Canvas):
    def __init__(self):
        super(FLIP_COIN, self).__init__(
            width=300,
            height=400,
            highlightthickness=0
        )

        self.position_coin = [(150, 200)]

        self.load_image()
        self.create_objects()
        self.random_coins()

    def load_image(self):
        try:
            self.vulture = ImageTk.PhotoImage(Image.open("image/vulture_coin.png"))
            self.tails = ImageTk.PhotoImage(Image.open("image/tails_coin.png"))
        except IOError as error:
            pass
            raise

    def show_coins(self):
        for x, y in self.position_coin:
            self.create_image(x,y, image=self.vulture)

    def show_tails(self):
        self.create_image(*self.position_coin, image=self.tails)

    def random_coins(self):
        self.random_coin = random.choice([0, 1])

    def coin(self):
        self.random_coins()

        if self.random_coin == 0:
            self.show_tails()

        if self.random_coin == 1:
            self.show_coins()


    def create_objects(self):

        self.click_button = Button(MAIN_WINDOW, text="press me", command=self.coin)
        self.click_button.pack(padx=20)

        self.button_exit = Button(MAIN_WINDOW, text="exit", command=Close_Window)
        self.button_exit.pack(padx=20)


def Close_Window():
    messagebox.askokcancel("Close Window", "Close Window ?")
    MAIN_WINDOW.destroy()


MAIN_WINDOW = Tk()
MAIN_WINDOW.title("FLIP COIN GAME")
MAIN_WINDOW.protocol("WM_DELETE_WINDOW", Close_Window)
MAIN_WINDOW.wm_attributes("-topmost", 1)
MAIN_WINDOW.resizable(False, False)
board = FLIP_COIN()
board.pack()
MAIN_WINDOW.mainloop()
