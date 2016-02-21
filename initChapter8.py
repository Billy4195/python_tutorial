import json

def section1():
    section1 = []
    section1.append('\"for loop\" is also control flow statement')
    section1.append('allows code to be executed repeatedly based on a given condition')
    section1.append('The following is syntax')
    section1.append('for i in range(x,y):')
    section1.append('    code to be excuted when i is in range(x,y)')
    section1.append('The i can be other word it just like a variable')
    section1.append('The i = x when for loop initial and += 1 as the code excute one time')
    section1.append('i will increase from x to y - 1, when i == y is out of range(x,y), ')
    section1.append('then program jump out the for loop')
    section1.append('example:')
    section1.append('>>>for i in range(0,10):\n>>>    print(i)')
    section1.append('0\n1\n2\n3\n4\n5\n6\n7\n8\n9')
    return section1
    
def section2():
    section2 = []
    section2.append('Prime number is number that have no other factor except 1 and itself')
    section2.append('How to check a number N is a prime number is to check from 2 to N-1 ')
    section2.append('whether any factor find in this range')
    return section2
    
def initChapter8(fileName):
    chapter8 = []
    chapter8.append(section1())
    chapter8.append(section2())
    try:
        with open(fileName,'a') as chapterFile:
            chapterFile.write(json.dumps(chapter8))
            chapterFile.write('\n')
    except IOError:
        print(fileName+' open failed')