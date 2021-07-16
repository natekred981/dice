import random
""" Simple dice rolling function """
def roller():
    roll = random.randint(1,6) 
    name = input("You got a " + str(roll) +  "\nTo roll again enter y for yes or n for no: ") 
    if (name == 'y'):
        roller() 
roller()


