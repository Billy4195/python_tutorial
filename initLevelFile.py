import json
import os
levelContainer = []
levelContainer.append({'levelNum':1,'name':'Variables'})
levelContainer.append({'levelNum':2,'name':'Arithmetic and Assignment Operators'})
levelContainer.append({'levelNum':3,'name':'Bitwise Operators'})
levelContainer.append({'levelNum':4,'name':'Relational and Logical Operators'})
levelContainer.append({'levelNum':5,'name':'Print'})
levelContainer.append({'levelNum':6,'name':'If elif else Statement'})
levelContainer.append({'levelNum':7,'name':'While loop'})
levelContainer.append({'levelNum':8,'name':'For loop'})
levelContainer.append({'levelNum':9,'name':'Function'})
print(json.dumps(levelContainer))
try:
    with open('levels.txt','w') as levelFile:
        levelFile.write(json.dumps(levelContainer))
except IOError:
    print("File open error: can't not open levels.txt")
os.system("pause")