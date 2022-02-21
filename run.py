# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

def generate_memory_field():
    """
    Generates the Memory Card field
    """
    list_dump = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
    random.shuffle(list_dump)
    return(list_dump)

def display_memory_field(memory_field):
    """
    Generate a string out of the memory field and
    displays it on the screen
    """
    row=1
    memory_string=""
    print("  A B C D E")
    for x in range(len(memory_field)):
        if x%5==0:
            memory_string+=f"{row} {memory_field[x]} "
            row+=1
        elif x%5==4:
            memory_string+=f"{memory_field[x]}\n"
        else:
            memory_string+=f"{memory_field[x]} "
    print(memory_string)

def main():
    """
    Runs the application
    """
    print("Welcome to the memory card game!")
    memory = generate_memory_field()
    display_memory_field(memory)

main()