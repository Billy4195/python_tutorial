import json

def section1():
    section1 = []
    section1.append('\"+\" is like the addition in arithmetic operation')
    section1.append('example:')
    section1.append('\ta = 1\n\tb = 3\n\tc = a + b')
    section1.append('The value store in c is 1 + 3 = 4')
    
def section2():
    section2 = []
    section2.append('\"-\" is like the subtraction in arithmetic operation')
    section2.append('example:')
    section2.append('\ta = 5\n\tb = 3\n\tc = a - b')
    section2.append('The value store in c is 5 - 3 = 2')
    section2.append('\tx = 2\n\ty = 7\n\tz = x - y')
    section2.append('The value store in z is 2 - 7 = -5')
    
def section3():
    section3 = []
    section3.append('\"*\" is like the multiplication in arithmetic operation')
    section3.append('example:')
    section3.append('\ta = 4\n\tb = 3\n\tc = a * b')
    section3.append('The value store in c is 4 * 3 = 12')
    section3.append('\tx = 2\n\ty = 7.1\n\tz = x * y')
    section3.append('The value store in z is 2 * 7.1 = 14.2')
    
def section4():
    section4 = []
    section4.append('\"/\" is like the  division in arithmetic operation')
    section4.append('example:')
    section4.append('\ta = 10\n\tb = 2\n\tc = a / b')
    section4.append('The value store in c is 10 / 2 = 5')
    section4.append('\tx = 3\n\ty = 4\n\tz = x / y')
    section4.append('The value store in z is 3 / 4 = 0.75')
    
def section5():
    section5 = []
    section5.append('\"%\" is like mod in arithmetic operation')
    section5.append('example:')
    section5.append('\ta = 10\n\tb = 2\n\tc = a % b')
    section5.append('The value store in c is 10 % 2 = 0')
    section5.append('\tx = 13\n\ty = 7\n\tz = x % y')
    section5.append('The value store in z is 13 % 7 = 6')
    
def section6():
    section6 = []
    section6.append('\"**\" is like exponent in arithmetic operation')
    section6.append('example:')
    section6.append('\ta = 10\n\tb = 2\n\tc = a ** b')
    section6.append('The value store in c is 10 ** 2 = 100')
    section6.append('\tx = 2\n\ty = 8\n\tz = 512 / x ** y')
    section6.append('The value store in z is 512 / (2 ** 8) = 512 / 256 = 2')
    
def section7():
    section7 = []
    section7.append('\"//\" is like Integer division in arithmetic operation')
    section7.append('example:')
    section7.append('\ta = 13\n\tb = 3\n\tc = a // b')
    section7.append('The value store in c is 13 // 3 = 4')
    section7.append('\tx = 2\n\ty = 8\n\tz = x // y')
    section7.append('The value store in z is 2 // 8 = 0')
    
def section8():
    section8 = []
    section8.append('+= : a += b is equal to a = a + b')
    section8.append('-= : a -= b is equal to a = a - b')
    section8.append('*= : a *= b is equal to a = a * b')
    section8.append('/= : a /= b is equal to a = a / b')
    section8.append('%= : a %= b is equal to a = a % b')
    section8.append('//= : a //= b is equal to a = a // b')
    section8.append('example:')
    section8.append('\ta = 13\n\tb = 7\n\ta += b')
    section8.append('The value store in a is 13 + 7 = 20 now')
    
def initChapter2(fileName):
    chapter2 = []
    chapter2.append(section1())
    chapter2.append(section2())
    chapter2.append(section3())
    chapter2.append(section4())
    chapter2.append(section5())
    chapter2.append(section6())
    chapter2.append(section7())
    chapter2.append(section8())
    try:
        with open(fileName,'w') as chapter2File:
            chapter2File.write(json.dumps(chapter2))
    except IOError:
        print(fileName+' open failed')