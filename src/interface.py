import threading
from tkinter import *
from game_mechanics import game
import timer

class Window(Frame):
    welcome_message = "welcome to anagrams"
    instructions = "choose how many letters to unscrmable!\nYou have 10 seconds!"
    
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        self.pack()
        self.make_widgets()
        self.num_let = 0
        self.my_game = None
        self.timer = None

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
        self.nametowidget(".entry").bind("<Return>", self.get_word)
        # after 60 seconds
        t = threading.Timer(10, self.game_over)
        t.start()

    def start_time(self):
        time =2
        self.timer = timer.my_thread("timer", time)
        self.timer.setDaemon(True)
        self.timer.start()
        print(threading.active_count())
        while not self.timer.get_time() == time:
            continue
        print(threading.active_count())

    def game_over(self):
        self.get_word
        self.nametowidget(".entry").pack_forget()
        
        self.my_game.check_words()
        valid = self.my_game.get_valid()
        invalid = self.my_game.get_invalid()
        res_str = "Num valid words: " + str(len(valid))
        lab_str = "Valid words: " + str(valid) + "\nInvalid words: " + str(invalid)

        result = Label(text = res_str, name = "score")
        label = Label(text = lab_str, name = "game_over")
        result.pack()
        label.pack()

    # get user word after enter
    def get_word(self, event):
        self.my_game.add_user_word(self.nametowidget(".entry").get())
        self.nametowidget(".entry").delete(0, END)

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

        self.play_game()

root = Tk()
app = Window(parent=root)
app.mainloop()
