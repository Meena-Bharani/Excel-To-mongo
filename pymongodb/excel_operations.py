import os

def verify_file(filename):
    pass

def loadFile(filename):
    with open(filename,'r') as lines:
        for line in lines:
            print(line)
