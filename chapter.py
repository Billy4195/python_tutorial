from section import section
class chapter:
    def __init__(self,jsonchapter):
        self.chapterName = jsonchapter['chapterName']
        self.chapterNum = jsonchapter['chapterNum']
        self.sectionName = jsonchapter['sectionName']
    def setSection(self,introductions):
        self.sections = []
        for index in range(0,len(introductions)):
            self.sections.append(section(introductions[index]))