#load chapters from file and transform to class
import json
from chapter import chapter
def loadChapterFile():
    try:
        with open('chapters.txt','r') as chapterFile:
            jsonchapter = json.loads(chapterFile.read())
            chapterContainer = []
            for index in jsonchapter:
                chapterContainer.append( chapter(index) )
            return chapterContainer
    except IOError:
        print('chapters.txt loading failed')