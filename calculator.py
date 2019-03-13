from tkinter import *


class Calculator(object):

    def __init__(self):

        self.gui = Tk()
        self.topframe = Frame(self.gui)
        self.topframe.pack()
        self.botframe = Frame(self.gui)
        self.botframe.pack(side=BOTTOM)
        self.button1 = Button(self.topframe, text="Button 1", fg="red")
        self.button2 = Button(self.topframe, text="Button 2", fg="green")
        self.button3 = Button(self.topframe, text="Button 3", fg="blue")
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

        Button()

        self.gui.mainloop()


