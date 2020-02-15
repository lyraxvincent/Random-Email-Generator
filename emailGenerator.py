import numpy as np

names_list = []
with open('/home/lyrax/Documents/names.txt') as txt: #path of text file containing random names
    for name in txt:
        names_list.append(name)

arr_lst = np.array(names_list) #array list of names

new_lst = []
for i in arr_lst:
    i = i.split('\n')[0]  #cleaning the names in the array list
    new_lst.append(i)

email_list = []
for j in new_lst:
    j = j + '{}{}'.format(np.random.randint(1,99), '@gmail.com') #general format of email address
    email_list.append(j)

np.savetxt('/home/lyrax/Documents/emails.txt', email_list, fmt='%s') #path to save the generated email list