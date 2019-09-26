from getpass import getpass


class Model:
    lives = 10
    already_used = []

    def __init__(self):
        self.answer = getpass(prompt="Type answer: ").lower()
        self.trial = len(self.answer) * ["_"]
        self.__swap_sign__(" ")

    def process_input_value(self, input_value):
        self.already_used += [input_value]
        correct = self.__process_letter__(input_value) if len(input_value) == 1 else self.__process_word__(input_value)
        return correct

    def __process_letter__(self, letter):
        changed = self.__swap_sign__(sign=letter)
        self.__substract_life__(changed)
        return changed

    def __process_word__(self, word, changed=False):
        index = 0

        while word in self.answer[index:]:
            index += self.answer[index:].index(word)
            self.trial = self.__splice__(self.trial, index, index+len(word), list(word))
            index += len(word)+1
            changed = True

        self.__substract_life__(changed)
        return changed

    def __swap_sign__(self, sign, changed=False):
        for i, char in enumerate(self.answer):
            if char == sign:
                self.trial[i] = sign
                changed = True
        return changed

    def __splice__(self, original, index_from, index_to, replacement=None):
        if isinstance(index_from, (list, tuple)):
            return original[:index_from[0]]+index_to+original[index_from[1]:]
        return original[:index_from]+replacement+original[index_to:]

    def __substract_life__(self, changed):
        if not changed:
            self.lives -= 1

    def is_guessed(self):
        return "_" not in self.trial
