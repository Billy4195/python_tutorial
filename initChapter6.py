import json

def section1():
    section1 = []
    section1.append('\"if elif else\" is conditional statement')
    section1.append('The following is syntax')
    section1.append('if (condition):')
    section1.append('    code to be excuted when the condition is True')
    section1.append('elif (another condition):')
    section1.append('    code to be excuted when the second condition is True')
    section1.append('else:')
    section1.append('    code to be excuted when the above conditions are all False')
    section1.append('example:')
    section1.append('>>>Marry_score = 95')
    section1.append('>>>if (Marry_score > 90):\n>>>    print(\"Good Job!\")\n>>>elif (Marry_score > 60):')
    section1.append('>>>    print(\"Not Bad\")\n>>>else:\n>>>    print(\"Failed\")')
    section1.append('Good Job!')
    return section1
    
def initChapter6(fileName):
    chapter6 = []
    chapter6.append(section1())
    try:
        with open(fileName,'w') as chapter6File:
            chapter6File.write(json.dumps(chapter6))
    except IOError:
        print(fileName+' open failed')