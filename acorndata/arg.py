# 27. 함수 인자(Arguments)
# 29. 변수 scope
ttt = 0
i = 1
def foo():
    j = 0
    i = 5
    print(i," in foo()")
 
foo()
print(i," in foo()")




print(locals())

#print(globals())