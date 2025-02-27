from tkinter import *
from cell import Cell
import random

SPACE_SIZE = 50
CLOSED_COLOR = "#dbfaac"
MINE_COLOR = "#ff0000"

class matrix:
    def __init__(self, x,y, mine_count, game_canvas: Canvas):
        self.x = x
        self.y = y
        self.mine_count = mine_count
        self.game_canvas = game_canvas
        self.grid = [[Cell() for _ in range(x)] for _ in range(y)]
        self.set_mine()
        self.get_adjacent_mines()

    def draw_mine(self):
        mine_count = self.mine_count
        grid = self.x * self.y
        num_list = []

        for i in range(grid):       # 2차원 배열의 index는 0부터 시작
            num_list.append(i)
    
        mine_list = random.sample(num_list, mine_count)

        return mine_list
    
    def set_mine(self):
        self.mine_list = self.draw_mine()
        index = 0
        print(self.mine_list)
    
        for i in range(self.y):
            for j in range(self.x):
                self.grid[i][j].is_mine = True if index in self.mine_list else False
                self.grid[i][j].cell = self.game_canvas.create_rectangle(j * SPACE_SIZE, i * SPACE_SIZE, (j + 1) * SPACE_SIZE, (i + 1) * SPACE_SIZE, fill= CLOSED_COLOR)
                index += 1

    def left_click(self, event:Event):
        grid_x = int(event.x / SPACE_SIZE)
        grid_y = int(event.y / SPACE_SIZE)
        try:
            if (self.grid[grid_y][grid_x].is_open == False):
                if self.grid[grid_y][grid_x].is_mine:
                    for i in self.mine_list:
                        self.game_canvas.itemconfig(i + 1, fill = MINE_COLOR)
                    self.game_canvas.itemconfig(self.grid[grid_y][grid_x].cell, fill = MINE_COLOR)
                else:
                    self.chain_open_cell(grid_x, grid_y)
        except IndexError:
            return

    def right_click(self, event: Event):
        grid_x = int(event.x / SPACE_SIZE)
        grid_y = int(event.y / SPACE_SIZE)
        try: 
            if (self.grid[grid_y][grid_x].is_open == False):
                if (self.grid[grid_y][grid_x].is_flagged == False):
                    self.grid[grid_y][grid_x].is_flagged = True
                    self.write_flag(grid_x, grid_y)
                else:
                    self.grid[grid_y][grid_x].is_flagged = False
                    self.game_canvas.delete(self.grid[grid_y][grid_x].text)
        except IndexError:
            return

    def write_mine(self, grid_x, grid_y):
        if self.grid[grid_y][grid_x].is_open == False:
            x = grid_x  * SPACE_SIZE + (SPACE_SIZE / 2)
            y = grid_y  * SPACE_SIZE + (SPACE_SIZE / 2)
            if not self.grid[grid_y][grid_x].adjacent_mines == 0:
                self.game_canvas.create_text(x, y , text= self.grid[grid_y][grid_x].adjacent_mines, fill="black", font = ("Arial", 15))

    def write_flag(self, grid_x, grid_y):
        x = grid_x  * SPACE_SIZE + (SPACE_SIZE / 2)
        y = grid_y  * SPACE_SIZE + (SPACE_SIZE / 2)
        self.grid[grid_y][grid_x].text  = self.game_canvas.create_text(x, y , text= "X", fill="black", font = ("Arial", 15))

    def get_adjacent_mines(self):
        for grid_y in range(self.y):
            for grid_x in range(self.x):
                mine = 0
                for i in range(-1, 2):
                    if grid_y + i >= 0 and grid_y + i <= self.y - 1:
                        for j in range(-1, 2):
                            if i == 0 and j == 0:
                                continue
                            if grid_x + j >= 0  and grid_x + j <= self.x -1:
                                if self.grid[grid_y + i][grid_x + j].is_mine:
                                    mine += 1
                self.grid[grid_y][grid_x].adjacent_mines = mine

    def chain_open_cell(self, grid_x, grid_y):
        if not self.grid[grid_y][grid_x].is_open:
            if not self.grid[grid_y][grid_x].is_mine:
                for i in range(-1, 2):
                    if grid_y + i >= 0 and grid_y + i <= self.y - 1:
                        for j in range(-1, 2):
                            if grid_x + j >= 0  and grid_x + j <= self.x -1:
                                self.game_canvas.itemconfig(self.grid[grid_y][grid_x].cell, fill = "#FFFFFF")
                                self.write_mine(grid_x, grid_y)
                                self.grid[grid_y][grid_x].is_open = True
                                if self.grid[grid_y][grid_x].adjacent_mines == 0:
                                    self.chain_open_cell(grid_x + j, grid_y + i)

    def gameover():
        pass
