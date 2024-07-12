# 35. List Comprehesions(리스트 표현식)

import os
import glob
from pprint import pprint as pp


words = "나는 파이썬을 공부하고 있습니다. 파이썬은 무척 심플하고 명료합니다.".split()

# 1. 리스트 표현식 for 문
# 간단하게
length  = [len(word) for word in words]
print(length)

# origin
length = []
for word in words:
    length.append(len(word))

print(length)


temp = [len(word) for word in words if len(word) > 3]

print (temp)


if type(temp) == list:
    print('list')



# 36. Set Comprehesions(Set 표현식)

words = "나는 파이썬을 공부하고 있습니다. 파이썬은 무척 심플하고 명료합니다.".split()
settemp = {len(word) for word in words}
print(settemp)

settemp = {len(word) for word in words if len(word)> 3}



country_capital = {'대한민국':'서울',
                     '영국' :'런던',
                     '미국' :'워싱턴',
                     '일본' :'도쿄'}

capital_country = {capital: country for country, capital in country_capital.items()}

print(capital_country)


file_info = {os.path.realpath(p) : os.stat(p).st_size for p in glob.glob('*.*')}

pp(file_info)

dd = {os.path.split(key)[-1] : value for key, value in file_info.items() if os.path.splitext(key)[-1]=='.py'}

print(dd)