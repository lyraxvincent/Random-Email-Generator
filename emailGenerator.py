import numpy as np
import io

names_list = io.open("names.txt", "r").readlines()

def generate_emails(names=[]):

    email_list = []

    for nm in names:
        email_list.append(
            nm.strip().split('\n')[0] + '{}{}'.format(np.random.randint(1, 99), '@gmail.com')
        )

    return email_list

print(generate_emails(names_list))