import random
import string
with open ('gen.txt', "w") as file:
    for i in range(100):
        file.writelines([''.join(random.choice(string.ascii_letters)
                     for i in range(20)), '\n'])