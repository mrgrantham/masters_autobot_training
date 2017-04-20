import os
import sys

print os.path.realpath(__file__)

path = os.path.dirname(os.path.realpath(__file__)) + '/hallways'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, 'hallway_' + str(i)+ '.jpg'))
    i = i+1