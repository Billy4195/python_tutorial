import json
from level import level
def loadLevelFile():
    try:
        with open('levels.txt','r') as levelFile:
            jsonLevel = json.loads(levelFile.read())
            levelContainer = []
            for index in jsonLevel:
                levelContainer.append( level(index) )
            return levelContainer
    except IOError:
        print('levels.txt loading failed')