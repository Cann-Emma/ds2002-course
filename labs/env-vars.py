#!/c/Users/Emmanuella/AppData/Local/Microsoft/WindowsApps/python3


import os
FAV_NUM= "4"
MAJOR= "Psychology"
YEAR= "third"

# Set variables
os.environ["FAV_NUM"]= input('What is your favourite number? ')
os.environ["MAJOR"]= input('What is your major? ')
os.environ["YEAR"]= input('What year are you in University? ')

# Fetch variables
print(os.getenv("FAV_NUM"))
print(os.getenv("MAJOR"))
print(os.getenv('YEAR'))

