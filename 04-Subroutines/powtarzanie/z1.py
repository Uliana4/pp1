#1
# a = "computer science"
# print(len(a))
# 2
# a = str(5068)
# print(type(a))
# 3
# print(min(4,7,2,3,9,8))
# print(round(1.5))
# stri = "I always want to be there"
# print(sorted( stri, key=str.lower))
# import math
# a = 10
# b =4.8
# print(math.ceil(a))    # возвращает самое ближнее цклое число
# print(math.floor(a))   # возврат самого близкого меньшего числа
# print(math.fabs(a))  #возврат абсолют знач
# print(math.factorial(a))
# print(math.fmod(a, b))    #возврат а%б но для дробный
# print(math.isqrt(a))


# mb_function = lambda x, y : x / (y**2)
# print(mb_function(58, 164))

import platform

x = dir(platform)
y = platform.system()
print(x)
print(y)
