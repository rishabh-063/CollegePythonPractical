# Word count using command line arguments

from sys import argv
argv = argv[1].split()
dict = {}
for word in argv:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
print(dict)
print(len(argv))