# This script will print into console all the files and
# directories where you put and run it

import os

path = "./" # Current directory

array = os.listdir(path)

for x in array:
    print(x)