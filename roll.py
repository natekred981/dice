import random
def roller():
    roll = random.randint(1,6) #create random number between 1 and 6
    name = input("You got a " + str(roll) +  "\nTo roll again enter y for yes or n for no: ") #query the user for input
    if (name == 'y'):
        roller() #alow user to recursively repeat roll
roller()

#commands to run project
#docker build -t <image> .
#docker run -i -t <image>
