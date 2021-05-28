import re
import re
import mechanicalsoup as ms

class word_check:
    def check_word(word):
        browser = ms.StatefulBrowser(user_agent = "MechanicalSoup")
        browser.open("https://scrabblewordfinder.org/dictionary/" + word)

        return (bool)(re.search("<span class=\"red\">Not a valid word.</span>", str(browser.page)))
