from tkinter import *


class Calculator(object):

    def __init__(self):

        self.gui = Tk()
        self.gui.title("Calculator")
        self.frame = Frame(self.gui, width=200, height=600)
        self.initialize_buttons()
        self.gui.mainloop()





        self.gui.mainloop()

    def initialize_buttons(self):

        self.num_buttons = {}

        for i in range(1, 10):
            self.num_buttons[str(i)] = Button(self.gui, text=str(i))
            row = ((i-1)//3)+1
            column = (i+2)%3 +1
            self.num_buttons[str(i)].grid(row=row, column=column)

        self.num_buttons["0"] = Button(self.gui, text="0")
        self.num_buttons["0"].grid(row=4, column=2)