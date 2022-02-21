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


def main():
    """
    Runs the application
    """
    print("Welcome to the memory card game!")
    memory = generate_memory_field()
    print(memory)

main()