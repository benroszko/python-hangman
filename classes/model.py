from getpass import getpass


class Model:
    lives = 10
    already_used = []

    def __init__(self):
        self.answer = getpass(prompt="Type answer: ")
        self.trial = len(self.answer) * ["_"]
        self.__swap_sign__(" ")

    def process_letter(self, letter):
        self.already_used += [letter]
        changed = self.__swap_sign__(letter)

        if not changed:
            self.lives -= 1

        return changed

    def __swap_sign__(self, sign, changed=False):
        for i, char in enumerate(self.answer):
            if char == sign:
                self.trial[i] = sign
                changed = True
        return changed

    def is_guessed(self):
        return "_" not in self.trial
