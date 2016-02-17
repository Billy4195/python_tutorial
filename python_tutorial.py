

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
    selectLevel(levelContainer)
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

def selectLevel(levelContainer):
    state = None
    EXCEED_MAXIMUM_NUMBER = 1
    INVALID_INPUT = 2
    while True:
        try:
            levelPage(levelContainer)
            print("\n\n")
            if(state == EXCEED_MAXIMUM_NUMBER):
                print("Level number should not be greater than {0}".format(len(levelContainer)))
            elif state == INVALID_INPUT:
                print("Oops! Please input a number")
            command = int(input("Select Level to enter( 0 for Back ):"))
            if command > len(levelContainer):
                state = EXCEED_MAXIMUM_NUMBER
                clearScreen()
                continue
        except ValueError:
            state = INVALID_INPUT      
            clearScreen()
main()
