#!/c/Users/Emmanuella/AppData/Local/Microsoft/WindowsApps/python3


import os

# Set variables
os.environ["FAV_NUM"]="4"
os.environ["MAJOR"]="Psychology "
os.environ["YEAR"]="Third"

FAV_NUM=input('What is your favourite number? ')
MAJOR=input('What is your major? ')
YEAR=input('What year are you in University? ')

# Fetch variables
print(os.getenv("FAV_NUM"))
print(os.getenv("MAJOR"))
print(os.getenv('UVA_FIRST_YEAR'))

