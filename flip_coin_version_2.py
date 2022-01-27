from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class FLIP_COIN(Canvas):
    def __init__(self):
        super(FLIP_COIN, self).__init__(
            width=300,
            height=300,
            highlightthickness=0
        )

        self.position_coin = [(150, 200)]
        self.message = """Вы не ввели нечего не надо водити буквы а надо водити цифры от 0 до 1""".upper()

        self.load_image()
        self.create_objects()

    def load_image(self):
        try:
            self.vulture = ImageTk.PhotoImage(Image.open("image/vulture_coin.png"))
            self.pajur = ImageTk.PhotoImage(Image.open("image/tails_coin.png"))
        except IOError as error:
            pass
            raise

    def show_coins(self):
        for x, y in self.position_coin:
            self.create_image(x,y, image=self.vulture)

    def show_pajur(self):
        self.create_image(*self.position_coin, image=self.pajur)

    def coin(self):
        if self.user_input.get() == str(0):
            self.show_pajur()

        if self.user_input.get() == str(1):
            self.show_coins()


        if self.user_input.get() == "" or self.user_input.get() > str(0 or 1):
            messagebox.showinfo("предупреждение", f"{self.message} !!")

    def create_objects(self):

        self.user_input = Entry(MAIN_WINDOW, width=20)
        self.user_input.pack()

        self.click_button = Button(MAIN_WINDOW, text="нажмите на меня", command=self.coin)
        self.click_button.pack(padx=20)

        self.button_exit = Button(MAIN_WINDOW, text="выход", command=Close_Window)
        self.button_exit.pack(padx=20)


def Close_Window():
    messagebox.askokcancel("Закрытие окна", "Закрыть окно ?")
    MAIN_WINDOW.destroy()


MAIN_WINDOW = Tk()
MAIN_WINDOW.title("FLIP COIN GAME")
MAIN_WINDOW.protocol("WM_DELETE_WINDOW", Close_Window)
MAIN_WINDOW.wm_attributes("-topmost", 1)
MAIN_WINDOW.resizable(False, False)
board = FLIP_COIN()
board.pack()
MAIN_WINDOW.mainloop()
