number = int(input(" Enter number : "))
def decimalToBinary(number):
    return bin(number).replace("0b", "") 
def decimalToHexadecimal(number):
    return hex(number).replace("0x", "")
print(f" Binary number: {decimalToBinary(number)} \n Hexadecimal number: {decimalToHexadecimal(number)}")