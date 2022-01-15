from random import randint
#program create password from 20 letters, it randomly selects a letter from the list 20 times in a row
print(''.join(['0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'[randint(0, 61)] for i in range(20)]))