# -*- content: UTF-8 -*-

string = 'O\ns@po\nn#o\tl@v@\to\npé'

string = ' '.join(string.split()).replace('@', 'a').replace("#", "ã")

print(string)