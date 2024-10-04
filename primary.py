import random

fileS = open('settings.txt','r')     # Opens all the files and turns them into lists
linesS = fileS.readlines()
fileQ = open('questions.txt','r')
linesQ = fileQ.readlines()
fileO = open('options.txt', 'r')
linesO = fileO.readlines()

correct_counter = 0
threshhold = int(linesS[0].strip())    # Determines how many questions need to be answer correctly; configure in settings
question_counter = 0
options_counter = 0

cache = -1 # Cache makes sure no two questions repeat. Set to -1 at first because that isnt a possible number
random_counter = []    # All this creates a list of numbers for the randomizer to use
num = 0
while len(random_counter) != (len(linesQ))/2:
    random_counter.append(num)
    num += 2
random.shuffle(random_counter)

while correct_counter != threshhold:   # Keeps it cuonting until the ammount of correct answers is equal to the number specified in settings
    random_num = random.choice(random_counter)
    if random_num == cache:
        continue
    options_rng = int(random_num/2)
 
    if correct_counter < 0:            # Stops the correct counter from going below 0
        correct_counter = 0
    print(linesQ[random_num].strip())
    print(linesO[options_rng*5 + 1].strip())   # Prints the option for A
    print(linesO[options_rng*5 + 2].strip())   # Prints the option for B
    print(linesO[options_rng*5 + 3].strip())   # Prints the option for C
    print(linesO[options_rng*5 + 4].strip())   # Prints the option for D
    user_answer = input('> ')  # Prompts the user to give an answer
    if user_answer == (linesQ[random_num + 1].strip()):
        print('Correct!')
        correct_counter += 1  # Adds another number to the ammount correct
    else:
        print('Incorrect! Correct Answer: ' + (linesQ[question_counter + 1].strip()))
        correct_counter -= int(linesS[1])
    question_counter += 2         # Moves to next question
    options_counter += 5
    cache = random_num
    if question_counter >= len(linesQ):    # Prevents list from going out of range
        question_counter = 0
        options_counter = 0

    
fileS.close()
fileQ.close()
fileO.close()

