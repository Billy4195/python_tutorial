import json

def section1():
    section1 = []
    section1.append('\">\" is greater than')
    section1.append('\"<\" is less than')
    section1.append('example:')
    section1.append('\t a = 9\n\t b = 12\n\t c = a > b ')
    section1.append('The value store in c is ( 9 > 12 ) False')
    section1.append('\t x = 9\n\t y = 12\n\t z = x < y ')
    section1.append('The value store in z is ( 9 < 12 ) True')
    return section1
    
def section2():
    section2 = []
    section2.append('\">=\" is greater than or equal')
    section2.append('example:')
    section2.append('\t a = 7\n\t b = 10\n\t c = a >= b ')
    section2.append('The value store in c is ( 7 >= 10 ) False')
    return section2
    
def section3():
    section3 = []
    section3.append('\"<=\" is less than or equal')
    section3.append('example:')
    section3.append('\t a = 37\n\t b = 99\n\t c = a <= b ')
    section3.append('The value store in c is ( 37 <= 99 ) True')
    return section3
    
def section4():
    section4 = []
    section4.append('\"==\" is equal to')
    section4.append('example:')
    section4.append('\t a = 37\n\t b = 99\n\t c = a == b ')
    section4.append('The value store in c is ( 37 == 99 ) False')
    return section4
    
def section5():
    section5 = []
    section5.append('\"!=\" is not equal to')
    section5.append('example:')
    section5.append('\t a = 37\n\t b = 99\n\t c = a != b ')
    section5.append('The value store in c is ( 37 != 99 ) True')
    return section5

def section6():
    section6 = []
    section6.append('\"not\" is logical not')
    section6.append('\"not True\" = \"False\"\n\"not False\" = \"True\"')
    section6.append('example:')
    section6.append('\t a = 37\n\t b = 99\n\t c = not ( a > b )')
    section6.append('The value store in c is not ( 37 > 99 ) = not ( False ) = True')
    return section6
    
def section7():
    section7 = []
    section7.append('\"or\" is logical or')
    section7.append('\"True or True\" = \"True\"\n\"True or False\" = \"True\"\n\"False or False\" = \"False\"')
    section7.append('example:')
    section7.append('\t a = ( 37 < 69 ) or ( 51 > 98 )')
    section7.append('The value store in a is ( Ture ) or ( False ) = True')
    return section7
    
def section8():
    section8 = []
    section8.append('\"and\" is logical and')
    section8.append('\"True and True\" = \"True\"\n\"True and False\" = \"False\"\n\"False and False\" = \"False\"')
    section8.append('example:')
    section8.append('\t a = ( 73 < 61 ) and ( 91 > 98 )')
    section8.append('The value store in a is ( False ) and ( False ) = False')
    return section8
    
def initChapter4(fileName):
    chapter4 = []
    chapter4.append(section1())
    chapter4.append(section2())
    chapter4.append(section3())
    chapter4.append(section4())
    chapter4.append(section5())
    chapter4.append(section6())
    chapter4.append(section7())
    chapter4.append(section8())
    try:
        with open(fileName,'a') as chapterFile:
            chapterFile.write(json.dumps(chapter4))
            chapterFile.write('\n')
    except IOError:
        print(fileName+' open failed')
    
