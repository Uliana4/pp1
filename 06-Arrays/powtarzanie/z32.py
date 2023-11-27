def occurs(number, array):
    if number in array:    
        return (f'Number: {number}\nArray: {array}\nResult: number {number} appears in the array')
print(occurs(23, [15, 38, 7, 23, 14]))