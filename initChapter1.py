import json

def section1():
    section1 = []
    section1.append('Variable means a space to store something')
    section1.append('variable will be write as following example:')
    section1.append('\ta = 1\n\tb = 100\n\tc = 1.5\n\ts=\"hello\"')
    section1.append('Variable name will be left side of \"=\" ')
    section1.append('The value want to store in variable should be written in right side of \"=\" ')
    section1.append('There are three type of data that can be store in variable.')
    section1.append('\"int\",\"float\" and \"str\"')
    section1.append('Details will be shown in next few section')
    return section1

def section2():
    section2 = []
    section2.append('int means integer number')
    section2.append('int can be used for arithmetic operation')
    section2.append('example:')
    section2.append('\ta = 1\n\tb = 5\n\th = 100\n\tdog = 99')
    return section2
    
def section3():
    section3 = []
    section3.append('float means number with decimal point like 1.0 or 2.3')
    section3.append('float can also be used for arithmetic operation')
    section3.append('example:')
    section3.append('\ta = 1.1\n\tb = 3.5\n\th = 100.0\n\tdog = 9.99')
    return section3
    
def section4():
    section4 = []
    section4.append('str is sentence like')
    section4.append('and string write inside \"\" block')
    section4.append('it can also store just a letter like\n\tdog = \"D\"')
    section4.append('str can\'t be used for arithmetic operation')
    section4.append('example:')
    section4.append('\ta = \"apple\"\n\tb = \"banana\"\n\tyours = \"heart\"\n\tthat = \"dog\"')
    return section4
def initChapter1(fileName):
    chapter1 = []
    chapter1.append(section1())
    chapter1.append(section2())
    chapter1.append(section3())
    chapter1.append(section4())
    try:
        with open(fileName,'w') as chapter1File:
            chapter1File.write(json.dumps(chapter1))
    except IOError:
        print(fileName+' open failed')