# write
f = open('test.txt', mode='wt', encoding='utf-8')
f.write('Hello World!')
f.write('newline 문자로 개행해봅니다.\n')
f.write('개행 ok?')
f.close()

# read

try:
    r = open('test.txt',mode='rt',encoding='utf-8')
    print(r.read(10))
    print(r.read(10))
    r.seek(0)
    print(r.read(10))
    r.seek(0)
    print(r.readline())
    r.seek(0)

    for line in r:
        print(line)
except FileNotFoundError as e:
    print(e)
finally:
    r.close()


a = open('test.txt', mode='at', encoding='utf-8')
a.writelines(['hi','bye'])
a.close()


with open('test1.txt', mode='wt', encoding='utf-8') as f:
    f.write('파이썬으로 파일을 작성하고 있습니다.')
    f.write('newline 문자로 개행해봅니다.\n')
    f.write('개행이 잘되었나요?')
