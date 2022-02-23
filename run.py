# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import os

class MemoryCard():
    """
    Creates an instance of MemoryCard
    """
    def __init__(self):
        self.score = 0                                      # keeps track of the score, 10=all cards revealed
        self.fails = 0                                      # keeps track of unsuccessful tries
        self.solution = ["0", "0", "1", "1", "2", "2", "3", "3", "4", "4", "5", "5",
                 "6", "6", "7", "7", "8", "8", "9", "9"]
        self.guess = ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X",
                      "X", "X", "X", "X", "X", "X", "X", "X", "X"]
        random.shuffle(self.solution)                       # shuffles the list to create a random Card Deck
        
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
        if column % 5==0:                           #start of a new row, prints row index then current card
            memory_string += f"{row} {memories} "
            row += 1
        elif column % 5==4:                         #prints current card then ends the current row after the 5th card
            memory_string += f"{memories}\n"
        else:                                       #prints out current card
            memory_string += f"{memories} "
        column += 1

    print(memory_string)
    
def validate_input(input_str):
    """
    Checks if Input is valid
    """
    if len(input_str) == 2:                         #checks if input lenght is exactly 2
        list = [char for char in input_str]         #splits the string into 2 elements
        list[0] = list[0].upper()                   #makes the first letter uppercase
        
        if list[0] == "A" or list[0] == "B" or list[0] == "C" or list[0] == "D" or list[0] == "E":
            if(list[1].isdigit()):                              #checks if second is a digit and above checks if first is between A and E
                if(int(list[1]) > 0 and int(list[1]) < 5):      #checks if between 1 and 4
                    return True
                else:
                    return False                    #False is returned in all instances of an invalid input
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
    list = [char for char in input_str]             #splits the string into 2 elements
    index = 0
    if list[0].upper() == "A":                      #increments the index for columns
        index += 0
    elif list[0].upper() == "B":
        index += 1
    elif list[0].upper() == "C":
        index += 2
    elif list[0].upper() == "D":
        index += 3
    elif list[0].upper() == "E":
        index += 4
    else:
        return 99                                   #returns 99 in case of an exception

    index += (int(list[1])-1)*5                     #increments index for rows (row 1=0, row 2=5, row 3=10 and row 4=15)

    return index                                    #returns index number


def main():                                         
    """
    Runs the application
    """
    print("Welcome to the memory card game!")                               #Welcome message and instructions
    print("In this Game, you have to find the pair of cards that match.")
    print("Reveal the whole Deck and you win.")
    playthegame = MemoryCard()                                              #creates a new instance of the class, creating the game
    display_memory_field(playthegame.solution)
    
    while playthegame.score < 10:
        while True:                                                             #starts the first selection of the card
            print("Please chose the first Card to reveal in the format")
            print("Column and then Row (e.g 'A1' or 'C2' or 'E3')\n")
            display_memory_field(playthegame.guess)
            cardone_str = input("Which Card do you want to reveal? ")
            if(validate_input(cardone_str)):                                    #validates if input is in correct format
                print("Your Input was valid!")
                index1 = convert_to_index(cardone_str)                           #converts the valid input into an index for the list
                if index1 == 99:                                                 #exception handling, should never happen
                    print("You shouldn't be here!")
                elif playthegame.is_revealed(index1):                            #checks if list is already revealed on the field
                    print("The card is already revealed on the field!")
                else:
                    print(f"The Card you reveal is: {playthegame.solution[index1]}")     #tells the player which card he/she revealed
                    break
            else:
                print("Invalid Input!")
        
        while True:                                                             #starts the second selection of the card
            print("Please chose the second Card to reveal in the format")
            print("Column and then Row (e.g 'A1' or 'C2' or 'E3')\n")
            cardtwo_str = input("Which Card do you want to reveal? ")
            if(validate_input(cardtwo_str)):                                    #validates if input is in correct format
                print("Your Input was valid!")
                index2 = convert_to_index(cardtwo_str)                          #converts the valid input into an index for the list
                if index2 == 99:                                                #exception handling, should never happen
                    print("You shouldn't be here!")
                elif index2 == index1:                                          #checks if player chose same card with both inputs
                    print("You have to chose 2 different cards to reveal!")     
                elif playthegame.is_revealed(index2):                           #checks if list is already revealed on the field
                    print("The card is already revealed on the field!")
                else:
                    print(f"The Card you reveal is: {playthegame.solution[index2]}")    #tells the player which card he/she revealed
                    break
            else:
                print("Invalid Input!")
        
        if playthegame.solution[index1] == playthegame.solution[index2]:        #checks if both revealed cards are the same
            print("You managed to reveal a pair!")
            playthegame.guess[index1] = playthegame.solution[index1]            #updates the guess list with revealed cards
            playthegame.guess[index2] = playthegame.solution[index2]
            playthegame.score += 1                                              #increases gamescore (correct guesses) by 1
        
        else:                                                                   #chosen cards don't match
            print("The two cards don't match...")
            playthegame.fails += 1                                              #increases wrong guesses by 1
        
        input("Press Enter to continue...")                                     #waits for player to press Enter to continue the game
        os.system('cls||clear')                                                 #clears the gamescreen before the next round, this prevents the player
                                                                                #from scrolling up and looking for old reveals
    print("Good Job! You finished the whole Deck!")
main()
