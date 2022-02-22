# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

def generate_memory_field():
    """
    Generates the Memory Card field
    """
    list_dump = ["0","0","1","1","2","2","3","3","4","4","5","5","6","6","7","7","8","8","9","9"]
    random.shuffle(list_dump)
    return(list_dump)

class MemoryCard():
    """
    Creates an instance of MemoryCard
    """
    def __init__(self):
        self.solution = generate_memory_field()
        self.guess = ["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"]
        
    def is_revealed(self):
        """
        Checks if the Card is already revealed on the field
        """
        if self.solution == self.guess:
            return True
        else:
            return False

def display_memory_field(memory_field):
    """
    Generate a string out of the memory field and
    displays it on the screen
    """
    row=1
    column=0
    memory_string=""
    print("  A B C D E")
    for memories in memory_field:
        if column%5==0:
            memory_string+=f"{row} {memories} "
            row+=1
        elif column%5==4:
            memory_string+=f"{memories}\n"
        else:
            memory_string+=f"{memories} "
        column+=1

    print(memory_string)
    
def validate_input(input_str):
    """
    Checks if input is valid
    """
    if len(input_str)==2:
        list = [char for char in input_str]
        if list[0].upper()=="A" or list[0].upper()=="B" or list[0].upper()=="C" or list[0].upper()=="D" or list[0].upper()=="E":
            if(list[1].isdigit()):
                if(int(list[1])>0 and int(list[1])<5):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False        

def main():
    """
    Runs the application
    """
    print("Welcome to the memory card game!")
    print("In this Game, you have to find the pair of cards that match.")
    print("Reveal the whole Deck and you win.")
    print("Please chose the first Card to reveal in the format")
    print("Column and then Row (e.g 'A1' or 'C2' or 'E3')\n")
    playthegame = MemoryCard()
    display_memory_field(playthegame.guess)
    cardone_str = input("Which Card do you want to reveal? ")
    if(validate_input(cardone_str)):
        print("Your Input was valid!")
    else:
        print("Invalid Input!")
    

main()