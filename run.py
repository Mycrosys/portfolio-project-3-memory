"""
Memory - a simple Memory Card Game
"""
import random   # needed for shuffling of the deck
import os       # needed for clearing the terminal screen
from colorama import Fore, Style  # needed for colored text output


class MemoryCard:
    """
    Creates an instance of MemoryCard
    """
    def __init__(self, difficulty):
        self.difficulty = difficulty    # difficulty (0=10 cards, 1=20, 2=30)
        self.score = 0     # keeps track of the score, 10=all cards revealed
        self.fails = 0     # keeps track of unsuccessful tries
        self.solution = ["0", "0", "1", "1", "2", "2", "3", "3", "4", "4",
                         "5", "5", "6", "6", "7", "7", "8", "8", "9", "9",
                         "a", "a", "b", "b", "c", "c", "d", "d", "e", "e"]
        self.guess = ["ﾛ", "ﾛ", "ﾛ", "ﾛ", "ﾛ", "ﾛ", "ﾛ", "ﾛ", "ﾛ", "ﾛ", "ﾛ",
                      "ﾛ", "ﾛ", "ﾛ", "ﾛ", "ﾛ", "ﾛ", "ﾛ", "ﾛ", "ﾛ", "ﾛ", "ﾛ",
                      "ﾛ", "ﾛ", "ﾛ", "ﾛ", "ﾛ", "ﾛ", "ﾛ", "ﾛ"]

        # sets size of list and with it field size and target score
        if self.difficulty == 0:
            del self.solution[10:30]
            del self.guess[10:30]
            self.target = 5
        elif self.difficulty == 1:
            del self.solution[20:30]
            del self.guess[20:30]
            self.target = 10
        else:
            self.target = 15

        # shuffles the list to create a random Card Deck
        random.shuffle(self.solution)

    def is_revealed(self, index):
        """
        Checks if the Card is already revealed on the field
        """
        if self.solution[index] == self.guess[index]:
            return True
        else:
            return False

    def show_card(self, index):
        """
        Prints the choosen Card to Terminal
        Ascii Art is created by Text to ASCII Art Generator:
        https://patorjk.com/software/taag/
        """
        print(f"""
                        .------.
                        |{self.solution[index]}.--. |
                        | :/\: |
                        | (__) |
                        | '--'{self.solution[index]}|
                        `------'\n""")

    def display_memory_field(self):
        """
        Generate a string out of the revealed memory field
        and displays it on the screen
        """
        row = 1
        column = 0
        memory_string = ""
        print("               +---+---+---+---+---+---+")
        print("               |   | A | B | C | D | E |")
        print("               +---+---+---+---+---+---+")
        for memories in self.guess:
            # start of a new row, prints row index then current card
            if column % 5 == 0:
                memory_string += f"               | {row} | {memories} | "
                row += 1
            # prints current card then ends the current row after the 5th card
            elif column % 5 == 4:
                memory_string += f"{memories} |\n"
                memory_string += "               +---+---+---+---+---+---+\n"
            # prints out current card
            else:
                memory_string += f"{memories} | "
            column += 1

        print(memory_string)

    def get_card(self, other_index):
        """
        Get Player Input for showing a Card
        """
        while True:
            print(Fore.BLUE + "Please chose a Card to reveal in the")
            print("format Column and then Row (e.g 'A1' or 'C2' or 'E1').")
            print(Style.RESET_ALL)
            cardtwo_str = input("Which Card do you want to reveal? ")

            # validates if input is in correct format
            if validate_input(cardtwo_str, self.difficulty):

                # converts the valid input into an index for the list
                index = convert_to_index(cardtwo_str)

                # exception handling, should never happen
                if index == 99:
                    print("You shouldn't be here!")

                # checks if player chose same card with both inputs
                elif index == other_index:
                    print("You have to choose 2 different cards to reveal.")

                # checks if list is already revealed on the field
                elif self.is_revealed(index):
                    print("This card is already revealed on the field.")

                # tells the player which card he/she revealed
                else:
                    print("You reveal a Card!")
                    self.show_card(index)
                    return index
            else:
                print("Invalid Input, please try again.")


def validate_input(input_str, difficulty):
    """
    Checks if Input when choosing a Card is valid
    """
    # calculates the row numbers of cards
    if difficulty == 0:
        rows = 2
    elif difficulty == 1:
        rows = 4
    else:
        rows = 6

    # checks if input lenght is exactly 2
    if len(input_str) == 2:
        # splits the string into 2 elements
        list(input_str)

        # checks if first letter is between A and E
        if (
                input_str[0].upper() == "A" or
                input_str[0].upper() == "B" or
                input_str[0].upper() == "C" or
                input_str[0].upper() == "D" or
                input_str[0].upper() == "E"
           ):

            # checks if second letter is a digit
            if input_str[1].isdigit():

                # checks if between 1 and rows+1
                if int(input_str[1]) > 0 and int(input_str[1]) < rows+1:
                    return True

    # False is returned in all instances of an invalid input

                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def convert_to_index(input_str):
    """
    Converts Input of chosen Card into correct Index for List
    """
    # splits the string into 2 elements
    list(input_str)

    index = 0
    # increments the index for columns
    if input_str[0].upper() == "A":
        index += 0
    elif input_str[0].upper() == "B":
        index += 1
    elif input_str[0].upper() == "C":
        index += 2
    elif input_str[0].upper() == "D":
        index += 3
    elif input_str[0].upper() == "E":
        index += 4
    else:
        # returns 99 in case of an exception
        return 99

    # increments index for rows (row 1=0, row 2=5, row 3=10 and row 4=15)
    index += (int(input_str[1])-1)*5

    return index


def splash_title():
    """
    Displays a Splash Screen at the start of the Game.
    This is purely cosmetic.
    Ascii Art is created by Text to ASCII Art Generator:
    https://patorjk.com/software/taag/
    """
    print(r"""
      __  __
     |  \/  |
     | \  / | ___ _ __ ___   ___  _ __ _   _
     | |\/| |/ _ \ '_ ` _ \ / _ \| '__| | | |
     | |  | |  __/ | | | | | (_) | |  | |_| |
     |_|__|_|\___|_| |_| |_|\___/|_|   \__, |
      / ____|            | |            __/ |
     | |     __ _ _ __ __| |           |___/
     | |    / _` | '__/ _` |
     | |___| (_| | | | (_| |
      \_____\__,_|_|  \__,_|
      / ____|
     | |  __  __ _ _ __ ___   ___
     | | |_ |/ _` | '_ ` _ \ / _ \
     | |__| | (_| | | | | | |  __/
      \_____|\__,_|_| |_| |_|\___|""")


def splash_win():
    """
    Displays a Splash Screen when winning the Game.
    This is purely cosmetic.
    Ascii Art is created by Text to ASCII Art Generator:
    https://patorjk.com/software/taag/
    """
    print(r"""
      __     __          __          ___         _
      \ \   / /          \ \        / (_)       | |
       \ \_/ /__  _   _   \ \  /\  / / _ _ __   | |
        \   / _ \| | | |   \ \/  \/ / | | '_ \  | |
         | | (_) | |_| |    \  /\  /  | | | | | |_|
         |_|\___/ \__,_|     \/  \/   |_|_| |_| (_)""")


def main():
    """
    Runs the application
    """
    # Welcome message and instructions
    splash_title()
    print("\nWelcome to the memory card game!")
    print("In this Game, you have to find the pair of cards that match.")
    print("Reveal the whole Deck and you win.\n")
    input("Press Enter to continue!")
    os.system('cls||clear')

    # Choosing the Difficulty
    print(Fore.BLUE + "Enter 0 for 10 Cards (5 pairs).")
    print("Enter 1 for 20 Cards (10 pairs).")
    print("Enter 2 for 30 Cards (15 pairs).")
    print(Style.RESET_ALL)

    difficulty_int = 0

    while True:
        difficulty = input("Please choose your difficulty (0/1/2): ")
        # checks if it is exactly 1 character
        if len(difficulty) == 1:
            # checks if it is a digit
            if difficulty.isdigit():
                try:
                    difficulty_int = int(difficulty)
                    # checks if it is between 0 and 2
                    if difficulty_int >= 0 and difficulty_int < 3:
                        break
                    else:
                        print("Please enter a value between 0 and 2.")

                except UnicodeError as exception_error:
                    print(f"The Decoding failed: {exception_error}")
            else:
                print("Please enter a number.")
        else:
            print("Please enter a correct value.")

    # creates a new instance of MemoryCard, creating the game
    play = MemoryCard(difficulty_int)
    print("\n")

    while play.score < play.target:
        # displays the card field to player
        play.display_memory_field()

        # starts the first selection of the card
        # the value of 95 is given, because this is the first
        # card to reveal this round and a check is made if the
        # first and second chosen card in a given round is the same
        # 95 is an index that will never happen, so that check is ignored
        index1 = play.get_card(95)

        # starts the second selection of the card
        # this time we give the first index number to check
        # if the player is chosing the same card in the same round
        index2 = play.get_card(index1)

        # checks if both revealed cards are the same
        if play.solution[index1] == play.solution[index2]:
            print(Fore.GREEN + "\nYou managed to permanently reveal a pair!")
            print(Style.RESET_ALL)

            # updates the guess list with revealed cards
            play.guess[index1] = play.solution[index1]
            play.guess[index2] = play.solution[index2]

            # increases gamescore (correct guesses) by 1
            play.score += 1

        # chosen cards don't match
        else:
            print(Fore.RED + "\nThe two cards don't match...")
            print(Style.RESET_ALL)

            # increases wrong guesses by 1
            play.fails += 1

        # waits for player to press Enter to continue the game
        input("Press Enter to continue...")

        # clears the gamescreen before the next round
        os.system('cls||clear')

    # Winning message and total tries to win
    splash_win()
    print(f"\nGood Job! You took a total of {play.score+play.fails} tries!")


main()
