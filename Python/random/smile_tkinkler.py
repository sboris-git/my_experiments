from tkinter import *
tk = Tk()
canvas = Canvas(tk, width = 500, height= 500)
canvas.pack()
canvas.create_oval(150, 150, 350, 350, fill='yellow')
canvas.create_oval(235, 235, 200, 200, fill='black', tags='left')
canvas.create_oval(304, 235, 270, 200, fill='black', tags='right')
canvas.create_arc(200, 275, 304, 315, extent=-180, width=5, fill='white', tags='mouth')