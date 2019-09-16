from model import Model
from view import View


class HangManGame:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start(self):
        self.view.start_game(str(self.model.lives), self.model.trial)

        while self.model.lives > 0 and not self.model.is_guessed():
            letter = self.view.pass_letter()
            if letter in self.model.already_used:
                self.view.print_already_used(self.model.already_used)
            elif len(letter) not in [1, len(self.model.answer)]:
                self.view.wrong_input()
            elif letter == self.model.answer:
                break
            else:
                if not self.model.process_letter(letter):
                    self.view.wrong_letter(str(self.model.lives))

            self.view.show(self.model.trial)

        self.__end__()

    def __end__(self):
        self.view.end_game(self.model.lives, self.model.answer)

game = HangManGame(Model(), View())
game.start()
