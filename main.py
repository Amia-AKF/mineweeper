import tkinter.messagebox as msgbox
from tkinter import *
from game import Game


HOME_WIDTH = 300
HOME_HEIGHT = 0
BACKGROUND_COLOR = "#FFFFFF"




class Main_home:
    def __init__(self):
        self.home = Tk()

        self.home.title("mine weeper")
        self.home.resizable(False, False)

        self.mine_label = Label( self.home , text="지뢰 개수")
        self.mine_label.pack()

        self.mine_entry = Entry(self.home, width = 30)
        self.mine_entry.pack()

        self.xy_label = Label( self.home , text="x칸 y칸")
        self.xy_label.pack()

        self.xy_entry = Entry(self.home, width = 30)
        self.xy_entry.pack()

        self.start_button = Button(self.home, width=10, text="시작", overrelief="solid", command = self.check_value)
        self.start_button.pack()

        self.home_canvas = Canvas(self.home, bg=BACKGROUND_COLOR, height=HOME_HEIGHT, width=HOME_WIDTH)
        self.home_canvas.pack()

        self.home.update()

        self.center_windwow()

        self.home.mainloop()

    def check_value(self):
        count = self.get_mine_count()
        x, y = self.get_xy()
        
        if count == False or x == False:
            msgbox.showerror("오류", "숫자를 입력해주세요")
            return
        elif count < 0:  # 나중에 1로 수정
            msgbox.showerror("오류", "1 이상의 숫자를 입력해주세요")
            return False
        elif x < 1 or y < 1:
            msgbox.showerror("오류", "2 이상의 숫자를 입력해주세요")
            return False
        else:
            self.start_game()

    def start_game(self):
        count = self.get_mine_count()
        x, y = self.get_xy()
        Game(self.home , x, y , count)

    def get_mine_count(self):
        count = self.mine_entry.get()
        try:
            count = int(count)
            return count
        except ValueError:
            return False

    def get_xy(self):
        cordinate = self.xy_entry.get()
        try:
            x, y = map(int, cordinate.split())
            return x, y
        except ValueError:
            return False

    def center_windwow(self):
        self.home.update()
        
        window_width = self.home.winfo_width()
        window_height = self.home.winfo_height()
        screen_width = self.home.winfo_screenwidth()
        screen_height = self.home.winfo_screenheight()

        x = int((screen_width/2) - (window_width/2))
        y = int((screen_height/2) - (window_height/2))

        self.home.geometry(f"{window_width}x{window_height}+{x}+{y}")

if __name__ == "__main__":
    Main_home()