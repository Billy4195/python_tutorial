#reset chapter File to clear all the record
import json
def initChaptersFile():
    chapterContainer = []
    chapterContainer.append({'chapterNum':1,'chapterName':'Variables','sectionName':['Introduction to Variables','Int','Float','String']})
    chapterContainer.append({'chapterNum':2,'chapterName':'Arithmetic and Assignment Operators','sectionName':['+','-','*','/','%','**','//','+= -= *= /= %= //=']})
    chapterContainer.append({'chapterNum':3,'chapterName':'Bitwise Operators','sectionName':['&','|','^','~','<<','>>']})
    chapterContainer.append({'chapterNum':4,'chapterName':'Relational and Logical Operators','sectionName':['> , <','>=','<=','==','!=','not','or','and']})
    chapterContainer.append({'chapterNum':5,'chapterName':'Print','sectionName':['Basic Print','Format Print']})
    chapterContainer.append({'chapterNum':6,'chapterName':'If elif else Statement','sectionName':['if elif else']})
    chapterContainer.append({'chapterNum':7,'chapterName':'While loop','sectionName':['While loop --- multiplication table','Prime number']})
    chapterContainer.append({'chapterNum':8,'chapterName':'For loop','sectionName':['For loop --- multiplication table','Prime number']})
    chapterContainer.append({'chapterNum':9,'chapterName':'Function','sectionName':['Function --- multiplication table']})
    try:
        with open('chapters.txt','w') as chapterFile:
            chapterFile.write(json.dumps(chapterContainer))
            chapterFile.write('\n')
            print("Create chapters.txt successfully")
    except IOError:
        print("File open error: can't not open chapters.txt")
