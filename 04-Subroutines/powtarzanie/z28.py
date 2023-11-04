# def f(binary_number):
#     for i in binary_number:
#         if i=="0" or i=="1":
#             return True
#         else:
#             return False

def f(binary_number):
   for i in binary_number:
      if i not in "01":
         return False
   return True
   
print(f("101101")) 
print(f("1111"))
print(f("001"))
print(f("1311a0100"))