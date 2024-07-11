import random
number = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
random.shuffle(number)
for password in number:
    print(password, end='')