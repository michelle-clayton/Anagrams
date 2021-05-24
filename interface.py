from tkinter import Label, Tk, Button, Frame, Entry, END

class Window(Frame):
    welcome_message = "welcome"
    instructions = "instructions"

    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        self.winfo_toplevel().title("Anagrams")
        welc = Label(text = self.welcome_message)
        inst = Label(text = self.instructions)
        start_but = Button(text = "Start")
        welc.pack()
        inst.pack()
        start_but.pack()

root = Tk()
wind = Window(root)
root.mainloop()