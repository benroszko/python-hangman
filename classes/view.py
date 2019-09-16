class View:
    def start_game(self, lives, trial):
        print("Let's start the game!")
        print(lives + " lives left.")
        self.show(trial)

    def pass_letter(self):
        return input("Enter letter: ")

    def print_already_used(self, already_used):
        print("Input has beeen already used.")
        used_letters = list(
            filter(lambda letter: len(letter) == 1, already_used))
        used_words = list(filter(lambda word: len(word) != 1, already_used))
        self.__print_used__("letters", used_letters)
        self.__print_used__("words", used_words)

    def __print_used__(self, str, used_arr):
        if len(used_arr) != 0:
            print("Used " + str + ": " + ", ".join(used_arr))

    def wrong_input(self):
        print("Wrong input! Input should have length\
             of either 1 character or guessing word.")

    def wrong_letter(self, lives):
        print("Answer does not contain input you used.")
        print(lives + " lives left.")

    def show(self, trial):
        print(" ".join(trial))

    def end_game(self, lives, answer):
        self.__congrats__(answer) if lives > 0 else self.__game_over__(answer)

    def __congrats__(self, answer):
        print("Congratulations! You've guessed the word - " + answer + "!")

    def __game_over__(self, answer):
        print("You've lost the game!")
        print("The answer is: " + answer)
