from tkinter import *


class Calculator(object):

    def __init__(self):

        self.text = "                        44441"
        self.gui = Tk()
        self.gui.title("Calculator")
        self.calc_text = Label(self.gui, text=self.text, bd=1, relief=SUNKEN, anchor=N)
        self.calc_text.grid(column=1, columnspan=8, row=0)
        self.frame = Frame(self.gui, width=600, height=1800)
        self.initialize_buttons()
        self.gui.mainloop()

    def reset_text(self, x):
        self.text = "                                "
        self.calc_text.destroy()
        self.calc_text = Label(self.gui, text=self.text, bd=1, relief=SUNKEN, anchor=N)
        self.calc_text.grid(column=1, columnspan=8, row=0)
        self.initialize_buttons()

    def initialize_buttons(self):

        # initialize the number buttons
        self.num_buttons = {}
        for i in range(1, 10):
            self.num_buttons[str(i)] = Button(self.gui, text=str(i))
            row = ((i-1)//3)+1
            column = (i+2)%3+1
            self.num_buttons[str(i)].grid(row=row, column=column)
        self.num_buttons["0"] = Button(self.gui, text="0")
        self.num_buttons["0"].grid(row=4, column=2)
        self.num_buttons["0"].bind("<Button-1>", self.button0)
        self.num_buttons["1"].bind("<Button-1>", self.button1)
        self.num_buttons["2"].bind("<Button-1>", self.button2)
        self.num_buttons["3"].bind("<Button-1>", self.button3)
        self.num_buttons["4"].bind("<Button-1>", self.button4)
        self.num_buttons["5"].bind("<Button-1>", self.button5)
        self.num_buttons["6"].bind("<Button-1>", self.button6)
        self.num_buttons["7"].bind("<Button-1>", self.button7)
        self.num_buttons["8"].bind("<Button-1>", self.button8)
        self.num_buttons["9"].bind("<Button-1>", self.button9)

        # add operation buttons
        self.clear_button = Button(self.gui, text="Clear")
        self.clear_button.grid(column=1, row=4, columnspan=3)
        self.clear_button.bind("<Button-1>", self.reset_text)

        self.add_button = Button(self.gui, text="+")
        self.add_button.grid(column=4, row=1)

        self.sub_button = Button(self.gui, text="-")
        self.sub_button.grid(column=4, row=2)

        self.add_button = Button(self.gui, text="+")
        self.add_button.grid(column=4, row=1)

        self.add_button = Button(self.gui, text="+")
        self.add_button.grid(column=4, row=1)

        self.add_button = Button(self.gui, text="+")
        self.add_button.grid(column=4, row=1)


    def button0(self, x):
        self.text = self.text+"0"
        self.calc_text = Label(self.gui, text=self.text, bd=1, relief=SUNKEN)
        self.calc_text.grid(row=0, column=2)


    def button1(self, x):
        self.text = self.text + "1"
        self.calc_text = Label(self.gui, text=self.text, bd=1, relief=SUNKEN)
        self.calc_text.grid(row=0, column=2)

    def button2(self, x):
        self.text = self.text + "2"
        self.calc_text = Label(self.gui, text=self.text, bd=1, relief=SUNKEN)
        self.calc_text.grid(row=0, column=2)

    def button3(self, x):
        self.text = self.text + "3"
        self.calc_text = Label(self.gui, text=self.text, bd=1, relief=SUNKEN)
        self.calc_text.grid(row=0, column=2)

    def button4(self, x):
        self.text = self.text + "4"
        self.calc_text = Label(self.gui, text=self.text, bd=1, relief=SUNKEN)
        self.calc_text.grid(row=0, column=2)

    def button5(self, x):
        self.text = self.text + "5"
        self.calc_text = Label(self.gui, text=self.text, bd=1, relief=SUNKEN)
        self.calc_text.grid(row=0, column=2)

    def button6(self, x):
        self.text = self.text + "6"
        self.calc_text = Label(self.gui, text=self.text, bd=1, relief=SUNKEN)
        self.calc_text.grid(row=0, column=2)

    def button7(self, x):
        self.text = self.text + "7"
        self.calc_text = Label(self.gui, text=self.text, bd=1, relief=SUNKEN)
        self.calc_text.grid(row=0, column=2)

    def button8(self, x):
        self.text = self.text + "8"
        self.calc_text = Label(self.gui, text=self.text, bd=1, relief=SUNKEN)
        self.calc_text.grid(row=0, column=2)

    def button9(self, x):
        self.text = self.text + "9"
        self.calc_text = Label(self.gui, text=self.text, bd=1, relief=SUNKEN)
        self.calc_text.grid(row=0, column=2)