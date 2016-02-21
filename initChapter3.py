import json

def section1():
    section1 = []
    section1.append('\"&\" is Binary AND')
    section1.append('example:')
    section1.append('\t a = 3\n\t b = 5\n\t c = a & b')
    section1.append('3 can be written in binary 0011')
    section1.append('5 can be written in binary 0101')
    section1.append('The value store in c is 3 & 5 = 1')
    return section1
    
def section2():
    section2 = []
    section2.append('\"|\" is Binary OR')
    section2.append('example:')
    section2.append('\t a = 9\n\t b = 8\n\t c = a | b')
    section2.append('9 can be written in binary 1001')
    section2.append('8 can be written in binary 1000')
    section2.append('The value store in c is 9 | 8 = 9')
    section2.append('\t1001\n|\t1000\n------------------\n\t1001')
    return section2
    
def section3():
    section3 = []
    section3.append('\"^\" is Binary XOR')
    section3.append('example:')
    section3.append('\t a = 7\n\t b = 11\n\t c = a ^ b')
    section3.append('7 can be written in binary 0111')
    section3.append('11 can be written in binary 1011')
    section3.append('The value store in c is 7 ^ 11 = 12')
    section3.append('\t0111\n^\t1011\n------------------\n\t1100')
    return section3
    
def section4():
    section4 = []
    section4.append('\"~\" is Binary Not')
    section4.append('example:')
    section4.append('\t a = 7\n\t a = ~a')
    section4.append('7 can be written in binary 0111')
    section4.append('~7 can be written in binary 1000')
    section4.append('The value store in a is ~7 = 8 now')
    return section4
    
def section5():
    section5 = []
    section5.append('\"<<\" is Binary left shift')
    section5.append('example:')
    section5.append('\t a = 7\n\t b = a << 1')
    section5.append('7 can be written in binary  0000 0111')
    section5.append('7 << 1 is written in binary 0000 1110')
    section5.append('The value store in b is 7 << 1 = 14')
    return section5
    
def section6():
    section6 = []
    section6.append('\">>\" is Binary right shift')
    section6.append('example:')
    section6.append('\t a = 9\n\t b = a >> 1')
    section6.append('9 can be written in binary  0000 1001')
    section6.append('9 >> 1 is written in binary 0000 0100')
    section6.append('The value store in b is 9 >> 1 = 4')
    section6
    
def initChapter3(fileName):
    chapter3 = []
    chapter3.append(section1())
    chapter3.append(section2())
    chapter3.append(section3())
    chapter3.append(section4())
    chapter3.append(section5())
    chapter3.append(section6())
    try:
        with open(fileName,'a') as chapterFile:
            chapterFile.write(json.dumps(chapter3))
            chapterFile.write('\n')
    except IOError:
        print(fileName+' open failed')