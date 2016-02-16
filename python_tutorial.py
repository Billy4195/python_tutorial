

import os
import json
from loadLevelFile import loadLevelFile
#set foreground and background color
#introdution page 
def main():
    setcolor("8F")
    introduction_page()
    levelContainer = loadLevelFile()
    print(levelContainer)
    os.system("pause")

def setcolor(color):
    os.system("color "+color)

def introduction_page():
    print("Hello~\n")
    print("This is a program help you learn python\n")
    print("Enjoy it!  ˊˇˋ\n")
    os.system("pause")


    

main()
