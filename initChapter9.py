import json

def section1():
    section1 = []
    section1.append('Function can simlify programming when some code is frequently used')
    section1.append('put code into function, then simply call the fuction is rather \nthan copy the same code')
    section1.append('The following is syntax')
    section1.append('def function_name(argument):')
    section1.append('    ---function code---')
    section1.append('example:')
    section1.append('>>>def print_num(i):')
    section1.append('>>>    print(i)')
    section1.append('>>>print_num(5)')
    section1.append('>>>5')
    section1.append('>>>print_num(199)')
    section1.append('>>>199')
    return section1
    
def initChapter9(fileName):
    chapter9 = []
    chapter9.append(section1())
    try:
        with open(fileName,'a') as chapterFile:
            chapterFile.write(json.dumps(chapter9))
            chapterFile.write('\n')
    except IOError:
        print(fileName+' open failed')