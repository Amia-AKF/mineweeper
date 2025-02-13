import tkinter.messagebox as msgbox
from tkinter import *
import random

HOME_WIDTH = 300
HOME_HEIGHT = 0
BACKGROUND_COLOR = "#FFFFFF"
SPACE_SIZE = 30
CLOSED_COLOR1 = "#dbfaac"
CLOSED_COLOR2 = "#aced4a"
MINE_COLOR = "#ff0000"

class MainHome:
    def __init__(self):

        self.home = Tk()
        self.grid = NONE

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
        if self.get_mine_count() == False or self.get_xy() == False:
            msgbox.showerror("오류", "입력하신 값이 틀렷습니다.")
        else:
            self.setup_grid()
            self.setup_game()



    def game_restart(self):
        self.game.destroy()
        self.home.deiconify()


    def center_windwow(self):
        
        self.home.update()
        
        window_width = self.home.winfo_width()
        window_height = self.home.winfo_height()
        screen_width = self.home.winfo_screenwidth()
        screen_height = self.home.winfo_screenheight()

        x = int((screen_width/2) - (window_width/2))
        y = int((screen_height/2) - (window_height/2))

        self.home.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def get_mine_count(self):
        count = self.mine_entry.get()
        try:
            count = int(count)
            if count >= 0:
                return count
            else:
                msgbox.showerror("오류", "1 이상의 숫자를 입력해주세요")
                return False
        except ValueError:
            msgbox.showerror("오류", "숫자를 입력해주세요")
            return False
    
    def get_xy(self):
        cordinate = self.xy_entry.get()
        try:
            x, y = map(int, cordinate.split())
            if  x > 1 and y > 1:
                return x, y
            else:
                msgbox.showerror("오류", "2 이상의 숫자를 입력해주세요")
                return False
        except ValueError:
            msgbox.showerror("오류", "x y 좌표 형식으로 입력해주세요")
            return False


    def setup_game(self):
        self.home.withdraw()

        self.game = Tk()
        self.game.title("mine weeper")
        self.game.resizable(False, False)
    
        x, y = self.get_xy()

        
        self.game_canvas = Canvas(self.game, bg=BACKGROUND_COLOR, height= y * SPACE_SIZE, width = x * SPACE_SIZE)
        for i in range(y):
            for j in range(x):
                self.game_canvas.create_rectangle(j * SPACE_SIZE, i * SPACE_SIZE, (j + 1) * SPACE_SIZE, (i + 1) * SPACE_SIZE, fill= CLOSED_COLOR1)
        self.game_canvas.pack()

        self.game_restart_bt = Button(self.game, width=10, text="포기", overrelief="solid", command = self.game_restart)
        self.game_restart_bt.pack()

        self.game.update()

        window_width = self.game.winfo_width()
        window_height = self.game.winfo_height()
        screen_width = self.game.winfo_screenwidth()
        screen_height = self.game.winfo_screenheight()

        x = int((screen_width/2) - (window_width/2))
        y = int((screen_height/2) - (window_height/2))

        self.game.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.game.bind("<Button-1>", lambda event: self.on_left_click(event))

        self.game.mainloop()

    def setup_grid(self):
        x, y = self.get_xy()
        self.grid = [[{} for col in range(x)] for row in range(y)]
        mine_list = self.set_mine()
        index = 0
        print(mine_list)
    
        for i in range(y):
            for j in range(x):
                self.grid[i][j] = {
                    'index': index,
                    'status': 'closed',
                    'mine' : True if index in mine_list else False
                }
                index += 1

    def set_mine(self):
        mine_count = self.get_mine_count()
        x, y = self.get_xy()
        grid = x * y
        num_list = []

        for i in range(grid):
            num_list.append(i)
    
        mine_list = random.sample(num_list, mine_count)

        return mine_list
    
    def on_left_click(self, event: Event):
        x = int(event.x / SPACE_SIZE) * SPACE_SIZE
        y = int(event.y / SPACE_SIZE) * SPACE_SIZE

        if self.grid[int(y/ SPACE_SIZE)][int(x/ SPACE_SIZE)]['mine'] == True:
            self.game_canvas.create_rectangle(x  , y, x + SPACE_SIZE, y + + SPACE_SIZE, fill= MINE_COLOR)
        else:
            self.game_canvas.create_rectangle(x  , y, x + SPACE_SIZE, y + + SPACE_SIZE, fill= "#FFFFFF")


if __name__ == "__main__":
    MainHome()