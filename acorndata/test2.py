# 10. List
import copy
from pprint import pprint as pp
a = [1, 3, 5, 7]

print(type(a))


b = a + [ 2, 7]

print(a)

print(b)

b[0] = 10

print(a)

print(b)

c = list()


c.append("Hello")
c.append("World")

print(c)

#deep copy
b = copy.deepcopy(a)


# 1. list Repetition(리스트 반복)

d = [5, 3]

e = d * 3

d[0] =8
print(d)
print(e)

a = [[2,5]] * 3
print(a)
a[2].append(7)

print(a)


# 2. list 관련 메소드 및 연산

a = ['서울','인천', '대전','제주도','인천']

print(a.index('인천'))

print(a.count('인천'))

print(35 in [1, 35,90,100])

print(11 in [1, 3, 5,10])

print(11 not in [1, 3, 5,10])

a = [1, 2, 3, 4, 5, 6, 7]

del a[1]

a.remove(3)

del a[a.index(7)]

print(a)

a = [1, 10, 5, 7, 6]

a.reverse()

print(a)

a.sort()

print(a)

a.sort(reverse=True)

print(a)

m = '나는 파이썬을 잘하고 싶다'

m = m.split()

print(m)

m.sort(key=len)

print(m)

m.sort(key=len,reverse= True)

print(m)

x = [1 ,11, 2, 3]

y = sorted(x)

print(x)
print(y)



x = [1 ,11, 2, 3]

y = reversed(x)

print(list(y))

# tuple 
l = [1, "korea", 3.5, 1]

print(l)

print(type(l))

t = (1, "korea", 3.5, 1)

print(t)

print(type(t))

for i in t:
    print(i)

    def minmax(items):
        return min(items), max(items)
    
print(minmax([7,5,2,1,11,15,55]))

(a, (b,(c, d))) = (4,(3,(2,1)))
print(a)
print(b)
print(c)
print(d)

a = '감자'

b = '고구마'

a, b  = b, a

print(a)
print(b)


print(tuple([1, 7, 5, 3, 9]))
print(tuple("abcde"))

#dictionary

d = {'one' : 1, 'two' : 2, 'three' : 3}

print(d)

print(d['one'])

d['one'] = 11

print(d)


d['temp'] = "당황"

print(d)

d = {}
l = [1,2,3]
t = (4,5,6)
print(type(d))
print(type(l))
print(type(t))

d['list'] = l
d['tuple'] = t


print(d)

for val in d.values():
    print(val)


for key in d:
    print(key, d[key])

for key, val in d.items():
    print(key, val)

b =  'list' in d
print(b)

#del d['list']

print(d)

pp(d)



# Set
s = {3, 5, 7}

print(type(s))


s = set([1,3,5,7])

print(s)

s.add(11)

print(s)

s.remove(5)

print(s)



print(s)


for se in s:
    print(se)

l = list(range(0,5))
print(l)
print(range(10))

print(range(0,10,2))



