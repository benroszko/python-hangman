class View:
    def start_game(self, lives, trial):
        print("Let's start the game!")
        print(lives + " lives left.")
        self.show(trial)

    def pass_input_value(self):
        return input("Enter letter: ")

    def print_already_used(self, already_used):
        print("Input has beeen already used.")
        used_letters = [letter for letter in already_used if len(letter) == 1]
        used_words = [word for word in already_used if len(word) != 1 and " " not in word]
        used_phrases = [phrase for phrase in already_used if phrase not in used_letters+used_words]
        self.__print_used__("letters", sorted(used_letters))
        self.__print_used__("words", sorted(used_words))
        self.__print_used__("phrases", sorted(used_phrases))

    def __print_used__(self, str, used_arr):
        if len(used_arr) != 0:
            print("Used " + str + ": " + ", ".join(used_arr))

    def wrong_input_len(self):
        print("Wrong input! Input should have length of 1 letter, 1 word or guessing phrase.")

    def wrong_input_value(self, lives):
        print("Answer does not contain input you used.")
        print(lives + " lives left.")

    def show(self, trial):
        print(" ".join(trial))

    def end_game(self, lives, answer):
        self.__congrats__(answer) if lives > 0 else self.__game_over__(answer)

    def __congrats__(self, answer):
        print("Congratulations! You've guessed the answer - " + answer + "!")

    def __game_over__(self, answer):
        print("You've lost the game!")
        print("The answer is: " + answer)
