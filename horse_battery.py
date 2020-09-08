import random
import secrets
# output from list of random words a
seperators = ["-","_"," ","."]

jargon_file = open("jargon.txt")
word_file = open("wordlist.txt")
my_list = []
for line in jargon_file:
    my_list = line.split(",")
for line in word_file:
    word_list = line.split(",")
r = random.randint(0,100)
s = len(my_list)
t = len(word_list)
h = len(seperators)
answer_list = []
for x in range (1,5):
    w = secrets.choice(word_list)
    if x == 1:
        w = w.capitalize()
    answer_list.append(w)
answer_list.append(str(secrets.randbelow(100)))
g = random.randint(0,h-1)
sep = seperators[g]
print(sep.join(answer_list))
