from tkinter import Label, Tk, Button, Frame, Entry, END, constants
import random
import string

class Game():
    level = 0
    anagram = ""
    words = {}

    def __init__(self, level):
        self.level = level
    
    def generate_letters(self) -> string:
        vowels = "aeiouy"
        consonants = "bcdfghjklmnpqrstvwxz"
        lets = ""

        # need at least 2 vowels and 2 consonants
        lets += random.choice(vowels) + " "
        lets += random.choice(vowels) + " "
        lets += random.choice(consonants) + " "
        lets += random.choice(consonants) + " "

        # make the rest random based on the level
        for i in range(self.level - 4):
            lets += random.choice(string.ascii_lowercase) + " "
        
        return lets