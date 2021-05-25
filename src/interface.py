from tkinter import Label, Tk, Button, Frame, Entry
import game

class Window(Frame):
    welcome_message = "welcome to anagrams"
    instructions = "enter the number of letters you'd like to unscramble (4-9) then press start"
    num_let = 0
    my_game = None
    

    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        self.pack()
        self.make_widgets()

    # make the buttons and place in window
    def make_widgets(self):
        self.winfo_toplevel().title("Anagrams")

        welc = Label(text = self.welcome_message, name = "welc")
        inst = Label(text = self.instructions, name = "inst")
        start_but = Button(text = "Start", name = "start_but")
        but_4let = Button(text = "4 Letters", name = "4let_but", command = lambda lev = 4: self.start_game(lev))
        but_6let = Button(text = "6 Letters", name = "6let_but", command = lambda lev = 6: self.start_game(lev))
        but_8let = Button(text = "8 Letters", name = "8let_but", command = lambda lev = 8: self.start_game(lev))

        welc.pack()
        inst.pack()
        start_but.pack()

        self.nametowidget(".start_but").bind("<Button-1>", self.choose_level)

    # show the level buttons    
    def choose_level(self, event):
        self.nametowidget(".start_but").pack_forget()
        self.nametowidget(".4let_but").pack()
        self.nametowidget(".6let_but").pack()
        self.nametowidget(".8let_but").pack()

    # game has started => store user entries
    def play_game(self):
        self.nametowidget(".entry").get()

    # initialize game board 
    def start_game(self, level):
        self.nametowidget(".4let_but").pack_forget()
        self.nametowidget(".6let_but").pack_forget()
        self.nametowidget(".8let_but").pack_forget()

        self.my_game = game.Game(level)
        self.num_let = level
        self.my_game.__init__(self.num_let)
        rand_let = Label(text = self.my_game.generate_letters(), name = "rand_let")
        entry = Entry(name = "entry")

        rand_let.pack()
        entry.pack()
    

root = Tk()
app = Window(parent=root)
app.mainloop()
