from model import Model
from view import View


class HangManGame:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start(self):
        self.view.start_game(str(self.model.lives), self.model.trial)

        while self.model.lives > 0 and not self.model.is_guessed():
            input_value = self.view.pass_input_value()
            if input_value in self.model.already_used:
                self.view.print_already_used(self.model.already_used)
            elif input_value == self.model.answer:
                break
            elif len(input_value) not in list(map(lambda word: len(word), self.model.words)) + [1, len(self.model.answer)]:
                self.view.wrong_input_len()
            else:
                if not self.model.process_input_value(input_value):
                    self.view.wrong_input_value(str(self.model.lives))

            self.view.show(self.model.trial)

        self.__end__()

    def __end__(self):
        self.view.end_game(self.model.lives, self.model.answer)

game = HangManGame(Model(), View())
game.start()
