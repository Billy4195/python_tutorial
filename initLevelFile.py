#reset Level File to clear all the record
import json
levelContainer = []
levelContainer.append({'levelNum':1,'levelName':'Variables'})
levelContainer.append({'levelNum':2,'levelName':'Arithmetic and Assignment Operators'})
levelContainer.append({'levelNum':3,'levelName':'Bitwise Operators'})
levelContainer.append({'levelNum':4,'levelName':'Relational and Logical Operators'})
levelContainer.append({'levelNum':5,'levelName':'Print'})
levelContainer.append({'levelNum':6,'levelName':'If elif else Statement'})
levelContainer.append({'levelNum':7,'levelName':'While loop'})
levelContainer.append({'levelNum':8,'levelName':'For loop'})
levelContainer.append({'levelNum':9,'levelName':'Function'})
try:
    with open('levels.txt','w') as levelFile:
        levelFile.write(json.dumps(levelContainer))
except IOError:
    print("File open error: can't not open levels.txt")
