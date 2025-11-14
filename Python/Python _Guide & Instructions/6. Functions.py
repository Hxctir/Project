########################################
############# [6] Function #############
########################################

def say_hello(name):
    return f'Hello {name}'

print(say_hello('Mohamed'))

#---------------------------------------------------
# lambda function:

say_hello = lambda name : f'Hello {name}'
print(say_hello('Ahmed'))


#--------------------------------------------------------------
# [1] Built-in functions
#--------------------------------------------------------------

print(dir(__builtins__))

# [1] Number-dealing functions
abs() # الموجب موجب والسالب موجب
round() # لتقريب الأرقام
pow('base','exponent','modulus') # باور
max()
min()
sum()

# [2] String-dealing functions:
len()
str()
format()
chr()
ord()

# [3] Types changing functions:
int()
float()
bool()
list()
tuple()
set()
dict()


# slice()
# range()
# print()
# input()
