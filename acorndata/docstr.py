from words import fetch_words

# Docstring - 문서화

print(help(fetch_words))
print(fetch_words.__doc__)

def air_line(departure, arrival, flighttime):
     print('출발지는 : ', departure)
     print('도착지는 : ', arrival)
     print('비행시간은 :', flighttime)
 
myflight = {'departure':'서울', 'arrival':'LA', 'flighttime':'10시간'}

print(air_line(**myflight))