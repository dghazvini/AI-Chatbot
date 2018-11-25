import random
#import tensorflow as tf
#import numpy as np
#import re

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

#def train():


# Main method
def main():
  #  userInput = input("Hello there\n")
  #  checkGreetings(userInput)
  #  checkFarewells(userInput)
    # Load data
    lines = open('movie_lines.txt', encoding='utf-8', errors='ignore').read().split('\n')
    conv_lines = open('movie_conversations.txt', encoding='utf-8', errors='ignore').read().split('\n')
    # The sentences that we will be using to train our model.
    lines[:10]
    # The sentences' ids, which will be processed to become our input and target data.
    conv_lines[:10]
    
main()