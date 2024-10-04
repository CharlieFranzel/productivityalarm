
create = open('settings.txt','a')  # Creates the settings file if it doesn't exist
settings = open("settings.txt", "a")

with open('settings.txt', 'w') as file: # This clears all old contents
    pass

text1 = str(input('How many questions need to be answered correctly to stop alarm?: '))   # Prompts and writes inputs
settings.write(text1)
settings.write('\n')
text2 = str(input('How many correct answers should the penalty for getting one wrong be?: '))
settings.write(text2)
settings.write('\n')
text3 = str(input('How many minutes until the alrm should shut itself off?: '))
settings.write(text3)
print('Completed Successfully!')

settings.close()
