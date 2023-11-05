def f(detector):
   if "+++" in detector or "++-++" in detector:
      return True
   return False
        

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))