from random_word import RandomWords
import random


# Initialize variables
r = RandomWords()
chars = '!@#$%'

# Cycle and create passwords
for i in range(100):
    rndint = str(random.randint(100, 1000))
    rndword = str(r.get_random_word())
    rndchar = str(chars[random.randint(0, 4)])

    hat = [rndint, rndword, rndchar]
    random.shuffle(hat)
    password = ''.join(hat)

    print(password)
