"""
Memory - a simple Memory Card Game
"""
import random   # needed for shuffling of the deck
import os       # needed for clearing the terminal screen


class MemoryCard():
    """
    Creates an instance of MemoryCard
    """
    def __init__(self):
        self.score = 0     # keeps track of the score, 10=all cards revealed
        self.fails = 0     # keeps track of unsuccessful tries
        self.solution = ["0", "0", "1", "1", "2", "2", "3", "3", "4", "4",
                         "5", "5", "6", "6", "7", "7", "8", "8", "9", "9"]
        self.guess = ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X",
                      "X", "X", "X", "X", "X", "X", "X", "X", "X"]
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
    print("  A B C D E")
    for memories in memory_field:
        # start of a new row, prints row index then current card
        if column % 5 == 0:
            memory_string += f"{row} {memories} "
            row += 1
        # prints current card then ends the current row after the 5th card
        elif column % 5 == 4:
            memory_string += f"{memories}\n"
        # prints out current card
        else:
            memory_string += f"{memories} "
        column += 1

    print(memory_string)


def validate_input(input_str):
    """
    Checks if Input is valid
    """
    # checks if input lenght is exactly 2
    if len(input_str) == 2:
        # splits the string into 2 elements
        chars = [char for char in input_str]
        # makes the first letter uppercase
        chars[0] = chars[0].upper()

        # checks if first letter is between A and E
        if (
                chars[0] == "A" or chars[0] == "B" or chars[0] == "C" or
                chars[0] == "D" or chars[0] == "E"
           ):

            # checks if second letter is a digit
            if chars[1].isdigit():

                # checks if between 1 and 4
                if(int(chars[1]) > 0 and int(chars[1]) < 5):
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
    characters = [char for char in input_str]
    index = 0
    # increments the index for columns
    if characters[0].upper() == "A":
        index += 0
    elif characters[0].upper() == "B":
        index += 1
    elif characters[0].upper() == "C":
        index += 2
    elif characters[0].upper() == "D":
        index += 3
    elif characters[0].upper() == "E":
        index += 4
    else:
        # returns 99 in case of an exception
        return 99

    # increments index for rows (row 1=0, row 2=5, row 3=10 and row 4=15)
    index += (int(characters[1])-1)*5

    return index       # returns index number


def main():
    """
    Runs the application
    """
    # Welcome message and instructions
    print("Welcome to the memory card game!")
    print("In this Game, you have to find the pair of cards that match.")
    print("Reveal the whole Deck and you win.")

    # creates a new instance of the class, creating the game
    play = MemoryCard()
    display_memory_field(play.solution)

    while play.score < 10:
        # starts the first selection of the card
        while True:
            print("Please chose the first Card to reveal in the format")
            print("Column and then Row (e.g 'A1' or 'C2' or 'E3')\n")
            display_memory_field(play.guess)
            cardone_str = input("Which Card do you want to reveal? ")

            # validates if input is in correct format
            if validate_input(cardone_str):
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
            if validate_input(cardtwo_str):
                print("Your Input was valid!")

                # converts the valid input into an index for the list
                index2 = convert_to_index(cardtwo_str)

                # exception handling, should never happen
                if index2 == 99:
                    print("You shouldn't be here!")

                # checks if player chose same card with both inputs
                elif index2 == index1:
                    print("You have to chose 2 different cards to reveal!")

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

        # clears the gamescreen before the next round, this prevents the player
        # from scrolling up and looking for old reveals
        os.system('cls||clear')

    print("Good Job! You finished the whole Deck!")


main()
