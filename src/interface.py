from tkinter import Label, Tk, Button, Frame
import game

class Window(Frame):
    welcome_message = "welcome to anagrams"
    instructions = "enter the number of letters you'd like to unscramble (4-9) then press start"
    num_let = 0
    myGame = None
    

    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        self.winfo_toplevel().title("Anagrams")

        welc = Label(text = self.welcome_message, name = "welc")
        inst = Label(text = self.instructions, name = "inst")
        start_but = Button(text = "Start", name = "start_but")
        but_4let = Button(text = "4 Letters", name = "4let_but")
        but_6let = Button(text = "6 Letters", name = "6let_but")
        but_8let = Button(text = "8 Letters", name = "8let_but")

        welc.pack()
        inst.pack()
        start_but.pack()

        self.nametowidget(".start_but").bind("<Button-1>", self.choose_level)

    def choose_level(self, event):
        self.nametowidget(".start_but").pack_forget()
        self.nametowidget(".4let_but").pack()
        self.nametowidget(".6let_but").pack()
        self.nametowidget(".8let_but").pack()

        self.nametowidget(".4let_but").bind("<Button-1>", self.play_game(4))
        self.nametowidget(".6let_but").bind("<Button-1>", self.play_game(6))
        self.nametowidget(".8let_but").bind("<Button-1>", self.play_game(8))

    def play_game(self, level):
        self.num_let = level
        self.myGame = game.Game()
        self.myGame.__init__(self.num_let)
    
    def start_game(self):
        self.myGame.generate_letters()


root = Tk()
app = Window(parent=root)
app.mainloop()
