def f(number1, number2, operator):
   if "+" in operator:
      return number1 + number2
   elif "-" in operator:
      return number1 - number2
   elif "*" in operator:
      return number1 * number2
   elif "%" in operator :
      return number1 % number2
   elif "**" in operator:
      return number1 ** number2

print(f(2,3, "+"))
print(f(2,3, "%"))
print(f(15,3, "-"))
