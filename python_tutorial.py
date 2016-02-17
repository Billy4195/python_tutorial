

import os
import json
from loadLevelFile import loadLevelFile
#set foreground and background color
#introdution page 
def main():
    setcolor("8F")
    introductionPage()
    levelContainer = loadLevelFile()
    clearScreen()
    levelPage(levelContainer)
    os.system("pause")

def setcolor(color):
    os.system("color "+color)

def clearScreen():
    os.system('cls')
    
def introductionPage():
    print("Hello~\n")
    print("This is a program help you learn python\n")
    print("Enjoy it!  ˊˇˋ\n")
    os.system("pause")

def levelPage(levelContainer):
    print("=============================Level Page=============================")
    for level in levelContainer:
        print("Level {0} ------ {1}".format(level.levelNum,level.levelName))



main()
