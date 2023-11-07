def f(n):
   if n == 1:
      return 0
   elif n ==2 or n == 3:
      return 1
   return f(n-1) + f(n-2)
print(f(5))
print(f(9))

# ????? пересмотреть!

# a =0
# b =1
# print(f'{a}\n{b}')
# for i in range(2,21):
#     c = a + b
#     a = b
#     b = c
#     print(c)