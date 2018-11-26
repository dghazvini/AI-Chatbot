import random
import re
import sys
import numpy

GREETINGS_OUTPUT = ["Hello there!", "Hi!", "What's up?", "Greetings!"]
FAREWELLS_INPUT = ("quit", "bye", "goodbye", "exit", "terminate")
FAREWELLS_OUTPUT = ["See ya!", "Goodbye!", "Farewell!", "Sayonara!"]

# Quit program if user specifices
def checkFarewells(userInput):
    if userInput.lower() in FAREWELLS_INPUT:
        print(random.choice(FAREWELLS_OUTPUT))
        sys.exit()

# Neural Net
def NN(m1, m2, w1, w2, b):
    z = m1 * w1 + m2 * w2 + b
    return sigmoid(z)

# Sigmoid function
def sigmoid(x):
    return 1/(1 + numpy.exp(-x))

# Calc Levenshtein Distance
def getLevenshteinDist(userInput):
    return

def giveResponse(userInput):
 # Generate random weights and bias
    w1 = numpy.random.randn()
    w2 = numpy.random.randn()
    b = numpy.random.randn()

    # Determine what predefined input is most similar to the user's input
    index=0
    indexofMaxMatchingWordsQuestion=0
    matchingWords=0
    maxMatchingWords=0
    for question in questions:
        for word in userInput.split():
            if word.lower() in question.lower():
                matchingWords=matchingWords+1
                if matchingWords > maxMatchingWords:
                    maxMatchingWords = matchingWords
                    indexofMaxMatchingWordsQuestion = index
        index=index+1
        matchingWords=0

    # Case for when no words match a question query
    if maxMatchingWords == 0:
        index=0
        for question in questions:
            for letter in userInput:
                if letter.lower() in question.lower():
                    matchingWords=matchingWords+1
                    if matchingWords > maxMatchingWords:
                        maxMatchingWords = matchingWords
                        indexofMaxMatchingWordsQuestion = index
            index=index+1
            matchingWords=0
        print(answers[indexofMaxMatchingWordsQuestion])
    else:
        print(answers[indexofMaxMatchingWordsQuestion])

    print("Activation is ", end=" ")
    print(NN(3, 1.5, w1, w2, b))

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


# *************** PROGRAM STARTS BELOW *****************
# Load conversation data
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

# Check if we have loaded the data correctly (DEBUGGING)
# limit = 0
# for i in range(limit, limit+5):
#     print(questions[i])
#     print(answers[i])
#     print()

# Take a look at some of the data to ensure that it has been cleaned well.
# limit = 0
# for i in range(limit, limit+5):
#     print(clean_questions[i])
#     print(clean_answers[i])
#     print()

userInput = input(random.choice(GREETINGS_OUTPUT) + "\n")

while True:
    checkFarewells(userInput)
    giveResponse(userInput)
    userInput = input()