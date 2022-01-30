# Generating strong random passwords of length 8 characters

import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
punc = ['!', '@', '_', '#', '&']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def generate_passwds(n=1):
    passwds = []

    for i in range(n):
        random.shuffle(alphabets); random.shuffle(punc); random.shuffle(digits)
        passwds.append('{}{}{}{}'.format(''.join(alphabets[:2]), ''.join(alphabets[-2:]).upper(),
                       ''.join(digits[:3]), punc[0]))

    return passwds


print(generate_passwds(3))