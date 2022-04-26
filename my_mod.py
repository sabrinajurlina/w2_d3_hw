from math import pi

def square_footage():
    length = input("What is the length of your house? ")
    width = input("What is the width of your house? ")
    area = int(length) * int(width)
    return area
print(f'Your house is: {square_footage()} square feet')

def circumference():
    r = input("What is the radius of your circle? ")
    C = 2*pi*int(r)
    return C
print(f'The circumference of your circle is: {circumference()}')

