from airtravel import Flight as fly
from inheritance import *

f = fly("AB001")

print(f.number())

# print(f.__number)

# a = Korea('대한민국')

# print("test:" , a.show())
# print("test:2" , a.show_name())

# print("test3:" , a.capital)

# print("test4: " , a.name)


# 3-1 일반적인 메소드 오버라이딩
print("start")
a = Korea('대한민국', 50000000, '서울')

a.show()