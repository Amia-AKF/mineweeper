from tkinter import *
from grid import matrix


BACKGROUND_COLOR = "#FFFFFF"
SPACE_SIZE = 50


class Game:
    def __init__(self , home: Tk , x, y ,count):
        self.home = home
        self.home.withdraw()

        self.x = x
        self.y = y
        self.count = count

        self.game = Tk()
        self.game.title("mine weeper")
        self.game.resizable(False, False)

        self.game_canvas = Canvas(self.game, bg=BACKGROUND_COLOR, height= y * SPACE_SIZE, width = x * SPACE_SIZE)
        self.game_canvas.pack()

        self.game_restart_bt = Button(self.game, width=10, text="포기", overrelief="solid", command = self.game_restart)
        self.game_restart_bt.pack()

        self.game.update()

        self.center_windwow()

        self.game.bind("<Button-1>", lambda event: self.matrix.left_click(event))
        self.game.bind("<Button-3>", lambda event: self.matrix.right_click(event))



        self.grid_set_up()

    def game_restart(self):
        self.game.destroy()
        self.home.deiconify()
    
    def grid_set_up(self):
        self.matrix = matrix(self.x ,self.y , self.count, self.game_canvas)



    def center_windwow(self):

        window_width = self.game.winfo_width()
        window_height = self.game.winfo_height()
        screen_width = self.game.winfo_screenwidth()
        screen_height = self.game.winfo_screenheight()

        x = int((screen_width/2) - (window_width/2))
        y = int((screen_height/2) - (window_height/2))

        self.game.geometry(f"{window_width}x{window_height}+{x}+{y}")