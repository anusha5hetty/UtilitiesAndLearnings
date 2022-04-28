from tkinter import Button

import random

class Cell:
    all_cells = []
    def __init__(self, row, column, is_mine=False) -> None:
        self.is_mine = is_mine
        self.cell_btn_obj = None
        self.row = row
        self.column = column
        Cell.all_cells.append(self)
        
    def create_btn_obj(self, location):
        def left_func(event):
            print("well it prints!! Great!!")
            
        def right_func(event):
            print("well it prints!! Great!!")
            
        btn = Button(location, text=f"{self.row},{self.column}", width=12, height=4)
        
        # <Button-1> is convension for Left click
        btn.bind('<Button-1>', left_func)
        
        # # <Button-3> is convension for right click
        btn.bind('<Button-3>', right_func)
        self.cell_btn_obj = btn
        return self.cell_btn_obj
    
    def __repr__(self):
        return f'Cell({self.row},{self.column})'
    
    @staticmethod
    def randomize_mines():
        pass