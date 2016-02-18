#reset Level File to clear all the record
import json
levelContainer = []
levelContainer.append({'levelNum':1,'levelName':'Variables','chapterName':['Introduction','Int','Float','String']})
levelContainer.append({'levelNum':2,'levelName':'Arithmetic and Assignment Operators','chapterName':['+','-','*','/','%','**','//','+= -= *= /= %= //=']})
levelContainer.append({'levelNum':3,'levelName':'Bitwise Operators','chapterName':['&','|','^','~','<<','>>']})
levelContainer.append({'levelNum':4,'levelName':'Relational and Logical Operators','chapterName':['> , <','>=','<=','==','!=','not','or','and']})
levelContainer.append({'levelNum':5,'levelName':'Print','chapterName':['Basic Print','Format Print']})
levelContainer.append({'levelNum':6,'levelName':'If elif else Statement','chapterName':['if elif else']})
levelContainer.append({'levelNum':7,'levelName':'While loop','chapterName':['While loop --- multiplication table','Prime number']})
levelContainer.append({'levelNum':8,'levelName':'For loop','chapterName':['For loop --- multiplication table','Prime number']})
levelContainer.append({'levelNum':9,'levelName':'Function','chapterName':['Function --- multiplication table']})
try:
    with open('levels.txt','w') as levelFile:
        levelFile.write(json.dumps(levelContainer))
except IOError:
    print("File open error: can't not open levels.txt")
