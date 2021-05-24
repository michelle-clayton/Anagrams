from tkinter import Label, Tk, Button, Frame, Entry, END, constants
import random
import string

class Game():
    level = 0
    window = None
    anagram = ""
    words = {}

    def __init__(self, level, window):
        self.level = level
        self.window = window
    
    def generate_letters(self):
        vowels = "aeiouy"
        consonants = "bcdfghjklmnpqrstvwxz"
        
        #need at least 2 vowels and 2 consonants
        