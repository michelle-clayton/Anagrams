from tkinter import Label, Tk, Button, Frame, Entry, END, constants
import random
import string
from game_mechanics import word_checker

class Game():
    def __init__(self, level):
        self.level = level
        self.anagram = ""
        self.anagram_map = {}
        self.words = set()
        self.final = [[], []]
    
    # generate random anagram
    # eventually will make better letters => 1/4 probability for bad consonants?
    def generate_letters(self) -> string:
        vowels = "aeiouy"
        consonants = "bcdfghjklmnpqrstvwxz"

        # need at least 2 vowels and 2 consonants
        self.add_anagram(vowels)
        self.add_anagram(vowels)
        self.add_anagram(consonants)
        self.add_anagram(consonants) 

        # make the rest random based on the level
        for i in range(self.level - 4):
            self.add_anagram(string.ascii_lowercase) 
        
        return self.anagram
    
    # add word user enters
    def add_user_word(self, word: string):
        self.words.add(word)
       # print(self.words)

    # check if word is legal (uses correct letters, is actually word)
    def check_word(self, word: string) -> bool:
        temp_word = word.replace(" ", "")
        checker = word_checker.word_check()
        if len(temp_word) > self.level:
            print(word + " has length issue")
            return False
        elif not self.is_substring(temp_word):
            print(word + " is in wrong subest")
            return False
        elif not checker.check_word(word):
            print(word + " is not real word")
            return False
        return True

    # helper -> adds random letter in s to anagram and map
    def add_anagram(self, set_add):
        add = random.choice(set_add)
        self.anagram += add + " "
        if self.anagram_map.__contains__(add):
            self.anagram_map[add] = self.anagram_map[add] + 1
        else:
            self.anagram_map[add] = 1

    # helper -> checks if word is substring of anagram
    def is_substring(self, word: string) -> bool:
        word_map = {}
        for s in word:
            if word_map.__contains__(s):
                word_map[s] = word_map[s] + 1
            else:
                word_map[s] = 1
        
        for k, v in word_map.items():
            if not self.anagram_map.__contains__(k):
                return False
            elif self.anagram_map[k] < v:
                return False

        return True

    # check all words 
    def check_words(self):
        valid = []
        invalid = []
        for s in self.words:
            if self.check_word(s):
                valid.append(s)
            else:
                invalid.append(s)
        self.final[0] = valid
        self.final[1] = invalid

    # return list of valid words
    def get_valid(self):
        return self.final[0]

    # return list of invalid words
    def get_invalid(self):
        return self.final[1]