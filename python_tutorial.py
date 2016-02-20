

import os
import json
from loadChapterFile import loadChapterFile
#set foreground and background color
#introdution page 
def main():
    setcolor("8F")
    introductionPage()
    chapterContainer = loadChapterFile()
    clearScreen()
    command = selectchapter(chapterContainer)
    clearScreen()
    if(command != 0):
        sectionPage(chapterContainer[command-1])
    else:
        pass
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

def chapterPage(chapterContainer):
    print("=============================chapter Page=============================")
    for chapter in chapterContainer:
        print("Chapter {0} ------ {1}".format(chapter.chapterNum,chapter.chapterName))

def sectionPage(chapter):
    print("Chapter {0} ------ {1}".format(chapter.chapterNum,chapter.chapterName))
    for sectionName,sectionNum in zip( chapter.sectionName,range(1,len(chapter.sectionName)+1) ):
        print("{0} - {1} ### {2}".format(chapter.chapterNum,sectionNum,sectionName))


def selectchapter(chapterContainer):
    state = None
    EXCEED_MAXIMUM_NUMBER = 1
    INVALID_INPUT = 2
    while True:
        try:
            chapterPage(chapterContainer)
            print("\n\n")
            if(state == EXCEED_MAXIMUM_NUMBER):
                print("chapter number should not be greater than {0}".format(len(chapterContainer)))
            elif state == INVALID_INPUT:
                print("Oops! Please input a number")
            command = int(input("Select chapter to enter( 0 for Back ):"))
            if command > len(chapterContainer):
                state = EXCEED_MAXIMUM_NUMBER
                clearScreen()
                continue
            else:
                return command
        except ValueError:
            state = INVALID_INPUT      
            clearScreen()
main()
