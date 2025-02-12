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



def get_mine_count():
    count = mine_entry.get()
    try:
        count = int(count)
        return count
    except ValueError:
        msgbox.showerror("오류", "숫자를 입력해주세요")

def get_xy():
    cordinate = xy_entry.get()
    try:
        x, y = map(int, cordinate.split())
        return x, y
    except ValueError:
        msgbox.showerror("오류", "x y 좌표 형식으로 입력해주세요")

def setup_grid():
    x, y = get_xy()
    global grid
    grid = [[{} for col in range(x)] for row in range(y)]
    mine_list = set_mine()
    index = 0
    print(mine_list)
    
    for i in range(y):
        for j in range(x):
            grid[i][j] = {
                'index': index,
                'status': 'closed',
                'mine' : True if index in mine_list else False
            }
            index += 1

    return grid

def game_start():
    home.withdraw()
    setup_grid()
    setup_game()

def game_restart():
    game.destroy()
    home.deiconify()

def setup_game():
    global game
    game = Tk()
    game.title("mine weeper")
    game.resizable(False, False)
    
    x, y = get_xy()

    game_canvas = Canvas(game, bg=BACKGROUND_COLOR, height= y * SPACE_SIZE, width = x * SPACE_SIZE)
    for i in range(y):
        for j in range(x):
            game_canvas.create_rectangle(j * SPACE_SIZE, i * SPACE_SIZE, (j + 1) * SPACE_SIZE, (i + 1) * SPACE_SIZE, fill= CLOSED_COLOR1)
    game_canvas.pack()

    game_restart_bt = Button(game, width=10, text="포기", overrelief="solid", command = game_restart)
    game_restart_bt.pack()

    game.update()

    window_width = game.winfo_width()
    window_height = game.winfo_height()
    screen_width = game.winfo_screenwidth()
    screen_height = game.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    game.geometry(f"{window_width}x{window_height}+{x}+{y}")

    game.bind("<Button-1>", lambda event: on_r_click(event, game_canvas))

    game.mainloop()

def set_mine():
    mine_count = get_mine_count()
    x, y = get_xy()
    grid = x * y
    num_list = []

    for i in range(grid):
        num_list.append(i)
    
    mine_list = random.sample(num_list, mine_count)

    return mine_list

def on_r_click(event: Event, game_cavas: Canvas):
    x = int(event.x / SPACE_SIZE) * SPACE_SIZE
    y = int(event.y / SPACE_SIZE) * SPACE_SIZE

    if grid[int(y/ SPACE_SIZE)][int(x/ SPACE_SIZE)]['mine'] == True:
        game_cavas.create_rectangle(x  , y, x + SPACE_SIZE, y + + SPACE_SIZE, fill= MINE_COLOR)
    else:
        game_cavas.create_rectangle(x  , y, x + SPACE_SIZE, y + + SPACE_SIZE, fill= "#FFFFFF")




home = Tk()
home.title("mine weeper")
home.resizable(False, False)


mine_label = Label( home , text="지뢰 개수")
mine_label.pack()

mine_entry = Entry(home, width = 30)
mine_entry.pack()

xy_label = Label( home , text="x칸 y칸")
xy_label.pack()


xy_entry = Entry(home, width = 30)
xy_entry.pack()

start_button = Button(home, width=10, text="시작", overrelief="solid", command = game_start)
start_button.pack()

home_canvas = Canvas(home, bg=BACKGROUND_COLOR, height=HOME_HEIGHT, width=HOME_WIDTH)
home_canvas.pack()

home.update()


window_width = home.winfo_width()
window_height = home.winfo_height()
screen_width = home.winfo_screenwidth()
screen_height = home.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

home.geometry(f"{window_width}x{window_height}+{x}+{y}")

home.mainloop()
