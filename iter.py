# 38. Iterable 과 Iterator


# Iterator

a = [1, 2, 3]

a_iter = iter(a)

type(a_iter)

print(a_iter.__next__())
print(a_iter.__next__())
print(a_iter.__next__())

# 네번째 StopIteration  에러

# print(a_iter.__next__())


def test_generator():
    print('yield 7 전')
    yield 7
    print('yield 8 전')
    yield 8
    print('yield 9 전')
    yield 9
    print('yield 9 후')


gen = test_generator()

print(gen)
print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))


for i in test_generator():
    print(i)

def three_generator():
     a = [1, 2, 3]
     yield from a


gen = three_generator()
print(list(gen))


def infinite_generator():
    count = 0
    while True:
        count+=1
        print(count)
        yield count


gen = infinite_generator()

print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


for i in range(5):
    print(i)

for i in range(5,10):
    print(i)

for i in range(5,10,2):
    print(i)
