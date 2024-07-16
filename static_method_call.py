from static_method import CustomClass
from language import *

print(CustomClass.add_instance_method(None, 3,5))

print(CustomClass.add_class_method( 3, 5))

a = CustomClass()

print(a.add_class_method( 1, 5))
print(a.add_static_method(2,5))
print(a.add_class_method(3,5))

a = KoreanLanguage.static_my_language()
b = KoreanLanguage.class_my_language()
a.print_language()
b.print_language()