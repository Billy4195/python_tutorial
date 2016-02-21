import json

def section1():
    section1 = []
    section1.append('\"print\" is a function can show something on your screen')
    section1.append('example:')
    section1.append('\t >>>a = 73\n\t >>>b = \"hello\"\n\t >>>c = 16')
    section1.append('\t >>>print(a)\n\t 73\n\t >>>print(b)\n\t hello\n\t >>>print(a,b)\n\t 73 hello')
    section1.append('\t >>>print(a > c)\n\t True')
    return section1
    
def section2():
    section2 = []
    section2.append('\"print\" can print as a flexible format up to the programmer')
    section2.append('\"%d\" means integer')
    section2.append('\"%f\" means float')
    section2.append('\"%s\" means str')
    section2.append('\"\n\" means next line')
    section2.append('example:')
    section2.append('\t >>>a = 73\n\t >>>b = \"hello\"\n\t >>>c = 7.2')
    section2.append('\t >>>print(\"%d\" % (a))\n\t 73\n\t >>>print(\"%s\" % (b))\n\t hello\n\t >>>print(\"%d\\n%s\" % (a,b))\n\t 73\n\t hello')
    section2.append('\t >>>print(\"%f\" % (c))\n\t 7.200000')
    section2.append('\t >>>print(\"%s\" % (12 <15))\n\t True')
    section2.append('\t >>>print(\"%d\" % (12 <15))\n\t 1')
    section2.append('(1 means True in programming language)')
    section2.append('\t >>>print(\"%s world\" % (b))\n\t hello world')
    section2.append('\t >>>print(\"%4d\" % (a))\n\t   73')
    section2.append('\t >>>print(\"%.1f\" % (c))\n\t 7.2')
    section2.append('\t >>>print(\"%.3f\" % (c))\n\t 7.200')
    return section2

def initChapter5(fileName):
    chapter5 = []
    chapter5.append(section1())
    chapter5.append(section2())
    try:
        with open(fileName,'a') as chapterFile:
            chapterFile.write(json.dumps(chapter5))
            chapterFile.write('\n')
    except IOError:
        print(fileName+' open failed')