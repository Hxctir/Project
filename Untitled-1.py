
def Twinkle():
    print('Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\t Up above the world so high,\n Like a diamond in the sky.\n\t\t \n Twinkle, twinkle, little star,\n\t How I wonder what you are')
Twinkle()
# \n    أنزل سطر
# \n\t    أزيح الكلام


import sys
print('Python version:\n' , sys.version)
print('Version info:\n' , sys.version_info)


import datetime
print('Date & time now:\n' , datetime.datetime.now())


import math
from math import pi
radius=float(input('Enter radius: '))
if radius>=0:
    area=pi*radius**2
    print('Area of the circle with radius ' + str(radius) + ' is: ' + str(area))


first_name=input('Enter first name: ')
last_name=input('Enter last name: ')
print('Hello! ' + last_name + ' ' + first_name)

