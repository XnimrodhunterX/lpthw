from sys import argv
script, filename = argv

file = open(filename, 'r')

print("here is the content of {}".format(filename), "\n\n")

print(file.read())