import math


print("Hello Worlid")

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

print((50 - 5*6) // 4)

print(5 ** 2)  # 5 squared

print(2 ** 7 ) # 2 to the power of 7

print(4 * 3.2 - 1)

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print(3 * 'un' + 'ium')

print('Py' 'thon')


py = 'Py' 
th ='thon'

print(py + th)


text = ('Put several strings within parentheses '
        'to have them joined together.')

print(text)

print(text[0])
print(text[-1])
print(text[-2])
print(text[0:5])
print(text[0:5] + text[7:9])

print(text[1:])
print(text[:2])
print(text[:-2])
print(text[-2:])


python = "Python";
print(len(python[5:6]))
print(len(python))

print('%(language)s has %(number)03d quote types.' %
      {'language': "Python", "number": 2})


print('%(language)s has %(number)06d num : %(num)0.2f quote types.' %
      {'language': "Python", "number": 2,"num" : 0.2})

squares = [1, 4, 9, 16, 25]
print(squares)
squares = squares + [36, 49, 64, 81, 100]

squares.append(121)

squares.extend([144, 169])

squares.insert(0, 13)
print(squares)

rgb = ["Red", "Green", "Blue"]

rgba = rgb

print(id(rgb) == id(rgba))



rgba.append("Alph")

print(rgb)

correct_rgba = rgba[:]

correct_rgba[-1] = "Alpha"

print(correct_rgba)


print(id(rgb))
print(id(correct_rgba))

print(id(rgb[0]))
print(id(correct_rgba[0]))

rgba[0] = "Good"
print(rgb[0])
print(rgba[0])
print(correct_rgba[0])

a = [1, 2, 3, 4, 5]
b = a

a[1] = 999
print(f'a의 값은 : {a}')
print(f'b의 값은 : {b}')


a1 = [1, [2, 3], 4, 5]
b1 = a1[:]

a1[1][0] = 999

print(f'a1의 값은 : {a1}')
print(f'b1의 값은 : {b1}')

NoneTest = None


if(NoneTest == True):
    print("True")
elif(NoneTest == False):
    print("False")
else:
    print("None")




    c = 5
    while c != 0:
        print(c)
        c -= 1 

    print("Done!")




while True:
    #line = input('숫자를 입력하세요')
    line = 10
    if int(line) % 10 == 0:
        print('10으로 나누어 보니 결과는 0입니다.')
        break # continue 도 있음 Java와 동일



# 8. String

multiLine = """ '이것은
멀티
라
인
입니다.
"""

print(multiLine)

a = 1

a = "q"
a = "이스케이프 문자 \n 라인이 바뀜 \\ 쌍따옴표를 또 쓰기 \"\" "
print(a)


s = 'abcdef'

print(s[3])


print(type(s))

if isinstance(s, str):
    print("s is string")

joiStr = 'Is'.join(['a','b','cde'])

print(joiStr)

splitStr = 'a,b,cde'.split(',')
print(splitStr)


formatStr = "Name: {}, Age: {}".format("철수", 13)

print(formatStr)


mathStr = '수학에서 파이= {m.pi:.3f}'.format(m=math)
print(mathStr)


mathStr = ' aaa수학에서 파이= %(m)0.3f          ' % {'m':math.pi}


print(mathStr)

mathStr = mathStr.strip()
print(mathStr)

mathStr = mathStr.capitalize()
print(mathStr)



# 9. Bytes

b = b'abcde'
print(b)


s = 'Vi er så glad for å høre og lære om Python!'


b = s.encode('utf-8')
print(b)
b = b.decode('utf-8')
print(b)