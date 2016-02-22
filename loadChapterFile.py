#load chapters from file and transform to class
import json
from chapter import chapter
def loadChapterFile(fileName):
    try:
        with open(fileName,'r') as chapterFile:
            lines = chapterFile.readlines()
            jsonchapter = json.loads(lines[0])
            chapterContainer = []
            for index in jsonchapter:
                chapterContainer.append( chapter(index) )
            for line,chapter_ in zip(lines[1:],chapterContainer):
                chapter_.setSection(json.loads(line))
            return chapterContainer
    except IOError:
        print(fileName+' loading failed')