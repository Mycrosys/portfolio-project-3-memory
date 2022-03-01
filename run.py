"""
Memory - a simple Memory Card Game
"""
import random   # needed for shuffling of the deck
import os       # needed for clearing the terminal screen


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


def display_memory_field(memory_field):
    """
    Generate a string out of the memory field and
    displays it on the screen
    """
    row = 1
    column = 0
    memory_string = ""
    print("               +---+---+---+---+---+---+")
    print("               |   | A | B | C | D | E |")
    print("               +---+---+---+---+---+---+")
    for memories in memory_field:
        # start of a new row, prints row index then current card
        if column % 5 == 0:
            memory_string += f"               | {row} | {memories} | "
            row += 1
        # prints current card then ends the current row after the 5th card
        elif column % 5 == 4:
            memory_string += f"{memories} |\n"
            memory_string += f"               +---+---+---+---+---+---+\n"
        # prints out current card
        else:
            memory_string += f"{memories} | "
        column += 1

    print(memory_string)


def validate_input(input_str, difficulty):
    """
    Checks if Input is valid
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
    Converts Input into correct Index for List
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

    return index       # returns index number


def splash_title():
    """
    Displays a Splash Screen at the start of the Game
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
    print("Enter 0 for 10 Cards (5 pairs).")
    print("Enter 1 for 20 Cards (10 pairs).")
    print("Enter 2 for 30 Cards (15 pairs).")

    while True:
        difficulty = input("Please choose your difficulty (0/1/2): ")
        # checks if it is exactly 1 character
        if len(difficulty) == 1:
            # checks if it is a digit
            if difficulty.isdigit():
                # checks if it is between 0 and 2
                if int(difficulty) >= 0 and int(difficulty) < 3:
                    break
                else:
                    print("Please enter a value between 0 and 2.")
            else:
                print("Please enter a number.")
        else:
            print("Please enter a correct value.")

    # creates a new instance of MemoryCard, creating the game
    play = MemoryCard(int(difficulty))
    display_memory_field(play.solution)

    while play.score < play.target:
        # starts the first selection of the card
        while True:
            print("Please chose the first Card to reveal in the format")
            print("Column and then Row (e.g 'A1' or 'C2' or 'E3')\n")
            display_memory_field(play.guess)
            cardone_str = input("Which Card do you want to reveal? ")

            # validates if input is in correct format
            if validate_input(cardone_str, play.difficulty):
                print("Your Input was valid!")

                # converts the valid input into an index for the list
                index1 = convert_to_index(cardone_str)

                # exception handling, should never happen
                if index1 == 99:
                    print("You shouldn't be here!")

                # checks if list is already revealed on the field
                elif play.is_revealed(index1):
                    print("The card is already revealed on the field!")

                # tells the player which card he/she revealed
                else:
                    print(f"The Card you reveal is: {play.solution[index1]}")
                    break
            else:
                print("Invalid Input!")

        # starts the second selection of the card
        while True:
            print("Please chose the second Card to reveal in the format")
            print("Column and then Row (e.g 'A1' or 'C2' or 'E3')\n")
            cardtwo_str = input("Which Card do you want to reveal? ")

            # validates if input is in correct format
            if validate_input(cardtwo_str, play.difficulty):
                print("Your Input was valid!")

                # converts the valid input into an index for the list
                index2 = convert_to_index(cardtwo_str)

                # exception handling, should never happen
                if index2 == 99:
                    print("You shouldn't be here!")

                # checks if player chose same card with both inputs
                elif index2 == index1:
                    print("You have to choose 2 different cards to reveal!")

                # checks if list is already revealed on the field
                elif play.is_revealed(index2):
                    print("The card is already revealed on the field!")

                # tells the player which card he/she revealed
                else:
                    print(f"The Card you reveal is: {play.solution[index2]}")
                    break
            else:
                print("Invalid Input!")

        # checks if both revealed cards are the same
        if play.solution[index1] == play.solution[index2]:
            print("You managed to reveal a pair!")

            # updates the guess list with revealed cards
            play.guess[index1] = play.solution[index1]
            play.guess[index2] = play.solution[index2]

            # increases gamescore (correct guesses) by 1
            play.score += 1

        # chosen cards don't match
        else:
            print("The two cards don't match...")

            # increases wrong guesses by 1
            play.fails += 1

        # waits for player to press Enter to continue the game
        input("Press Enter to continue...")

        # clears the gamescreen before the next round
        os.system('cls||clear')

    print("Good Job! You finished the whole Deck!")


main()
