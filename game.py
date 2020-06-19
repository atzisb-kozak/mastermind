from src.mastermind import Mastermind
from tkinter import *

game = Mastermind()

ROOT = Tk()

hs = ROOT.winfo_screenheight()
ws = ROOT.winfo_screenwidth()

ROOT.configure(background = '#050A02')
ROOT.title("Mastermind")
ROOT.geometry('%dx%d' %(ws,hs)) 

Button(ROOT, text = "Test the line", command = game.test_row).place(relx = 0.45, rely = 0.3)
Button(ROOT, text = "Erase the line", command = game.backspace_row).place(relx = 0.45, rely = 0.4)

def define_number() :
    array = []
    for i in range(10) :
        array.append(Canvas(ROOT, background = "#B2C2BB"))
        array[i].place(relx = 0.1, y = 100 + 52 * i, height = 50, width = 50)
        array[i].create_text(25, 25, text = str(game.board_game[i][0]))
    return array


def define_color() :
    array = []
    for i in range(10) :
        array.append([])
        for j in range(4) :
            array[i].append(Canvas(ROOT, background = "#B2C2BB"))
            array[i][j].place(relx = 0.135 + 0.035 * j, y = 100 + 52 * i, height = 50, width = 50)
            array[i][j].create_oval(25+2,25+2,25-2,25-2, fill = "#000000")
    return array

def define_hint() :
    array = []
    for i in range(10) :
        array.append([])
        for j in range(5) :
            if j == 0:
                array[i].append(Canvas(ROOT, background = "#B2C2BB"))
                array[i][j].place(relx = 0.2755, y = 100 + 52 * i, height = 50, width = 50)
            if j == 1:
                array[i].append(Canvas(array[i][0], background = "#B2C2BB"))
                array[i][j].place(x = 0, y = 0, height = 25, width = 25)
                array[i][j].create_oval(12.5+5,12.5+5,12.5-5,12.5-5, fill = "black")
            if j == 2:
                array[i].append(Canvas(array[i][0], background = "#B2C2BB"))
                array[i][j].place(x = 0, y = 25, height = 25, width = 25)
                array[i][j].create_oval(12.5+5,12.5+5,12.5-5,12.5-5, fill = "black")
            if j == 3:
                array[i].append(Canvas(array[i][0], background = "#B2C2BB"))
                array[i][j].place(x = 25, y = 0, height = 25, width = 25)
                array[i][j].create_oval(12.5+5,12.5+5,12.5-5,12.5-5, fill = "black")
            if j == 4:
                array[i].append(Canvas(array[i][0], background = "#B2C2BB"))
                array[i][j].place(x = 25, y = 25, height = 25, width = 25)
                array[i][j].create_oval(12.5+5,12.5+5,12.5-5,12.5-5, fill = "black")
    return array


ROOT.mainloop()

