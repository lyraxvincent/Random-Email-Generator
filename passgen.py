#This is a script for generating strong random passwords
#Length of generated password is 8 characters

import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
punc = ['!', '@', '_', '#', '&']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

random.shuffle(alphabets)
random.shuffle(punc)
random.shuffle(digits)

print('{}{}{}{}'.format(''.join(alphabets[:2]), ''.join(alphabets[-2:]).upper(), ''.join(digits[:3]), punc[0]))

'''
#This is if the user wants to generate several passwords to choose from...

for i in range(5):
    random.shuffle(alphabets)
    random.shuffle(characters)
    random.shuffle(digits)
    print('{}{}{}{}'.format(''.join(alphabets[:2]), ''.join(alphabets[-2:]).upper(), ''.join(digits[:3]), characters[0]))
'''