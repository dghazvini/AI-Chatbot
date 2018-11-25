import random
#import tensorflow as tf
#import numpy as np
import re
import sys

GREETINGS_INPUT = ("hi", "hello", "hey")
GREETINGS_OUTPUT = ["Hello there!", "Hi!", "What's up?", "Greetings!"]
FAREWELLS_INPUT = ("quit", "bye", "goodbye", "exit", "terminate")
FAREWELLS_OUTPUT = ["See ya!", "Goodbye!", "Farewell!", "Sayonara!"]

# Generic greetings
def checkGreetings(userInput):
    for word in userInput.split():
        if word.lower() in GREETINGS_INPUT:
            print(random.choice(GREETINGS_OUTPUT))
            return

# Quit program if user specifices
def checkFarewells(userInput):
    for word in userInput.split():
        if word.lower() in FAREWELLS_INPUT:
            print(random.choice(FAREWELLS_OUTPUT))
            sys.exit()

#def train():


# Main method
def main():
    # Load data
    lines = open('movie_lines.txt', encoding='utf-8', errors='ignore').read().split('\n')
    conv_lines = open('movie_conversations.txt', encoding='utf-8', errors='ignore').read().split('\n')

    # The sentences that we will be using to train our model.
    lines[:10]

    # The sentences' ids, which will be processed to become our input and target data.
    conv_lines[:10]

    # Create a dictionary to map each line's id with its text
    id2line = {}
    for line in lines:
        _line = line.split(' +++$+++ ')
        if len(_line) == 5:
            id2line[_line[0]] = _line[4]

   # Create a list of all of the conversations' lines' ids.
    convs = [ ]
    for line in conv_lines[:-1]:
        _line = line.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","")
        convs.append(_line.split(',')) 

    # Sort the sentences into questions (inputs) and answers (targets)
    questions = []
    answers = []

    for conv in convs:
        for i in range(len(conv)-1):
            questions.append(id2line[conv[i]])
            answers.append(id2line[conv[i+1]])

    # Check if we have loaded the data correctly
    limit = 0
    for i in range(limit, limit+5):
        print(questions[i])
        print(answers[i])
        print()
    
    # Compare lengths of questions and answers
    print(len(questions))
    print(len(answers))

    # Clean the data
    # clean_questions = []
    # for question in questions:
    #     clean_questions.append(clean_text(question))
    
    # clean_answers = []    
    # for answer in answers:
    #     clean_answers.append(clean_text(answer))
    
    # Take a look at some of the data to ensure that it has been cleaned well.
    # limit = 0
    # for i in range(limit, limit+5):
    #     print(clean_questions[i])
    #     print(clean_answers[i])
    #     print()

    userInput = input("Hello there, what can I do?\n")

    while True:
        checkGreetings(userInput)
        checkFarewells(userInput)
        userInput = input()

def clean_text(text):
    '''Clean text by removing unnecessary characters and altering the format of words.'''

    text = text.lower()
    
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"it's", "it is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "that is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"how's", "how is", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"n't", " not", text)
    text = re.sub(r"n'", "ng", text)
    text = re.sub(r"'bout", "about", text)
    text = re.sub(r"'til", "until", text)
    text = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", text)
    
    return text

main()