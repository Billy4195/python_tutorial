import json

def section1():
    section1 = []
    section1.append('\"while loop\" is control flow statement')
    section1.append('allows code to be executed repeatedly based on a given condition')
    section1.append('The following is syntax')
    section1.append('while (condition):')
    section1.append('    code to be excuted when the condition is True')
    section1.append('example:')
    section1.append('>>>i = 10')
    section1.append('>>>while(i > 0):\n>>>    print(i)\n>>>    i = i - 1\n>>>print(\"Happy New Year!\")')
    section1.append('10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nHappy New Year!')
    return section1
    
def section2():
    section2 = []
    section2.append('Prime number is number that have no other factor except 1 and itself')
    section2.append('How to check a number N is a prime number is to check from 2 to N-1 ')
    section2.append('whether any factor find in this range')
    return section2
    
def initChapter7(fileName):
    chapter7 = []
    chapter7.append(section1())
    chapter7.append(section2())
    try:
        with open(fileName,'w') as chapter7File:
            chapter7File.write(json.dumps(chapter7))
    except IOError:
        print(fileName+' open failed')