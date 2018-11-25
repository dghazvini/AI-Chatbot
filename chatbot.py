import random
#import tensorflow as tf

GREETINGS_INPUT = ("hi", "hello", "hey")
GREETINGS_OUTPUT = ("Hello there!, Hi!")
FAREWELLS_INPUT = ("quit, bye, goodbye, exit, terminate")
FAREWELLS_OUTPUT = ("See ya!, Goodbye!, Sayonara!")

# Generic greetings
def checkGreetings(userInput):
    for word in userInput.words:
        if word.lower() in GREETINGS_INPUT:
            print("HERE")
            print(random.choice(GREETINGS_OUTPUT))

# Quit program if user specifices
def checkFarewells(userInput):
    for word in userInput:
        if word.lower() in FAREWELLS_INPUT:
            print(random.choice(FAREWELLS_OUTPUT))

# Main method
def main():
    userInput = input("Hello there\n")
  #  checkGreetings(userInput)
  #  checkFarewells(userInput)

main()