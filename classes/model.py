class Model:
    lives = 10
    answer = "ananas"
    already_used = []
    trial = len(answer) * ["_"]

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
