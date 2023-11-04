# def function():
#     mb_function = lambda x, y :  x>y
#     if mb_function:
#         return True
#     else:
#         return False
        
# print(function(58, 164))


# def numbers(n1,n2):
#     if n1>n2:
#         return True
#     return False

# print(numbers(34,25))
# print(numbers(19,23))

numbers = lambda a,b : bool(a > b)
  
print(numbers(34,25))
print(numbers(19,23))