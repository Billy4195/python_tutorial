import json
def loadLevelFile():
    try:
        with open('levels.txt','r') as levelFile:
           return json.loads(levelFile.read())
    except IOError:
        print('levels.txt loading failed')