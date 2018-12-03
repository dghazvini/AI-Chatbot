import random
import re
import sys
import numpy
import Levenshtein

GREETINGS_OUTPUT = ["Hello there!", "Hi!", "What's up?", "Greetings!", "Welcome!"]
FAREWELLS_INPUT = ("quit", "bye", "goodbye", "exit", "terminate")
FAREWELLS_OUTPUT = ["See ya!", "Goodbye!", "Farewell!", "Sayonara!", "Catch ya later!"]

# Global Activation value (Zero by default)
Activation = 0

# Quit program if user specifices
def checkFarewells(userInput):
    if userInput.lower() in FAREWELLS_INPUT:
        print(random.choice(FAREWELLS_OUTPUT))
        sys.exit()

# Neural Net
def NN(m1, m2, w1, w2, b):
    z = m1 * w1 + m2 * w2 + b
    return sigmoid(z)

# Sigmoid normalizing function
def sigmoid(x):
    return 1/(1 + numpy.exp(-x))

# Return the index of the string in the dataset with the lowest Levenshtein Distance and the Levenshtein Distance itself.
def getLevenshteinDist(userInput):
    
    index=0
    minLD=999
    indexOfMinDist=0
    for question in questions:
        LD = Levenshtein.distance(userInput, question.lower())
        if LD < minLD:
            minLD = LD
            indexOfMinDist=index
        index=index+1

    return indexOfMinDist, minLD

# Return the index of the string in the dataset with the lowest Hamming distance and the Hamming Distance itself.
def getHammingDistance(userInput):

    index=0
    distance=0
    minHD=999
    indexOfMinDist=0
    for question in questions:
        if len(userInput) == len(questions[index]):
            distance=0
            for i in range(len(userInput)):
                if(userInput[i] != questions[index][i]):
                    distance=distance+1
            if distance < minHD:
                minHD = distance
                indexOfMinDist = index
        index=index+1
    
    return indexOfMinDist, minHD


# Determine what predefined question is most similar to the user's input based on word match count alone (Runs if Lev. Dist. isn't good enough)
# def getWordMatchValue(userInput):
#     index=0
#     indexOfMaxMatchingWords=0
#     matchingWords=0
#     maxMatchingWords=0
#     for question in questions:
#         for word in userInput.split():
#             if word.lower() in question.lower():
#                 matchingWords=matchingWords+1
#                 if matchingWords > maxMatchingWords:
#                     maxMatchingWords = matchingWords
#                     indexOfMaxMatchingWords = index
#         index=index+1
#         matchingWords=0
    
#     return maxMatchingWords, indexOfMaxMatchingWords

# Function for simply matching number of similar characters. Returns index and # of matching characters. Last resort.
# def getCharMatchValue(userInput):

#     index=0
#     matchingChars=0
#     maxMatchingChars=0
#     for question in questions:
#         for letter in userInput:
#             if letter.lower() in question.lower():
#                 matchingChars=matchingChars+1
#                 if matchingChars > maxMatchingChars:
#                     maxMatchingChars = matchingChars
#                     indexOfMostMatchingChars = index
#         index=index+1
#         matchingChars=0

#     #return(maxMatchingLetters/len(questions[indexofMaxMatchingLetters]))
#     return indexOfMostMatchingChars, maxMatchingChars

def giveResponse(userInput):
 # Generate random weights and bias
    w1 = (numpy.random.randn() * .95)
    w2 = (numpy.random.randn() * .05)
    b = numpy.random.randn()

    if(len(userInput) == 0):
        return

    # Try Hamming distance first
    HDIndex, HD = getHammingDistance(userInput)
    if (HD/len(userInput) <= .25):
        print("("+questions[HDIndex]+")")   # Question that most matches what user inputs
        print(answers[HDIndex])
        print()
        Activation = NN(HD/len(userInput), 0.0, w1, w2, b)
    #    print("Activation is", Activation)
        return

    #print("Trying LD...")
    # Try Levenshtein Distance second
    LDIndex, LD = getLevenshteinDist(userInput)
    print("("+questions[LDIndex]+")")   # Question that most matches what user inputs
    print(answers[LDIndex])
    print()
    Activation = NN(LD/len(userInput), 0.0, w1, w2, b)
 #   print("Activation is", Activation)
    return
    # if (LD/len(userInput) >= .30): 
    #     print("Trying to get CMV...")
    #     CMVIndex, CMV = getCharMatchValue(userInput)
    #     print(answers[CMVIndex])
    #     Activation = NN(CMV, 0.0, w1, w2, b)
    #     print("Activation is", Activation)
    #     return
    # else: # LD is good enough
    #     #print("Good nuff")
    #     print(answers[LDIndex])
    #     Activation = NN(LD/len(userInput), 0.0, w1, w2, b)
    #     print("Activation is", Activation)
    #     return
    

# Standardizes and cleans text a bit to make results more consistent
def clean_text(text):
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
lines[:10]
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

#Check if we have loaded the data correctly (DEBUGGING)
# limit = 0
# for i in range(limit, limit+50):
#     print(questions[i])
#     print(answers[i])
#     print()

# Run the bot
userInput = input(random.choice(GREETINGS_OUTPUT) + "\n")

while True:
    checkFarewells(userInput)
    giveResponse(userInput)
    userInput = input()