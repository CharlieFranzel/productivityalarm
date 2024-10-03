
fileS = open('settings.txt','r')
linesS = fileS.readlines()
fileQ = open('questions.txt','r')
linesQ = fileQ.readlines()
fileO = open('options.txt', 'r')
linesO = fileO.readlines()

correct_counter = 0
threshhold = int(linesS[0].strip())    # Determines how many questions need to be answer correctly; configure in settings
question_counter = 0
options_counter = 0

while correct_counter != threshhold:

    if correct_counter < 0:            # Stops the correct counter from going below 0
        correct_counter = 0
    print(linesQ[question_counter].strip())
    print(linesO[options_counter + 1].strip())   # Prints the option for A
    print(linesO[options_counter + 2].strip())   # Prints the option for B
    print(linesO[options_counter + 3].strip())   # Prints the option for C
    print(linesO[options_counter + 4].strip())   # Prints the option for D
    user_answer = input('> ')  # Prompts the user to give an answer
    if user_answer == (linesQ[question_counter + 1].strip()):
        print('Correct!')
        correct_counter += 1
    else:
        print('Incorrect! Correct Answer: ' + (linesQ[question_counter + 1].strip()))
        correct_counter -= int(linesS[1])
    question_counter += 2         # Moves to next question
    options_counter += 5

    if question_counter >= len(linesQ):    # Prevents list from going out of range
        question_counter = 0
        options_counter = 0

    
fileS.close()
fileQ.close()
fileO.close()