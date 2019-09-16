from getpass import getpass


class Model:
    lives = 10
    already_used = []

    def __init__(self):
        self.answer = getpass(prompt="Type answer: ")
        self.trial = len(self.answer) * ["_"]

    def process_letter(self, letter):
        self.already_used += [letter]
        changed = False

        for i, char in enumerate(self.answer):
            if char == letter:
                self.trial[i] = letter
                changed = True

        if not changed:
            self.lives -= 1

        return changed

    def is_guessed(self):
        return "_" not in self.trial
