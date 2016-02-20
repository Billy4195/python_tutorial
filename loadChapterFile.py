#load chapters from file and transform to class
import json
from chapter import chapter
def loadChapterFile(fileName):
    try:
        with open(fileName,'r') as chapterFile:
            jsonchapter = json.loads(chapterFile.read())
            chapterContainer = []
            for index in jsonchapter:
                chapterContainer.append( chapter(index) )
            return chapterContainer
    except IOError:
        print(fileName+' loading failed')