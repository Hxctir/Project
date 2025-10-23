#-------------------------------------------------------------------------
# [1] → print:
#-------------------------------------------------------------------------

print('Hello')

#-------------------------------------------------------------------------
# [2] → Types of data:
#-------------------------------------------------------------------------

print('Mohamed')   # string (str)

print(7)           # integer (int)

print(1.5)         # float

print(10==10)      # Boolean (bool)

print([1,2,3,4,5])      # List

print((1,2,3,4,5))       # Tuble 

print({'One':1,'Two':2,"Three":3})        # Dict

# to detect → type()
print(type(10))
print(type(1.5))
print(type('Stop'))
print(type([2,3,4,5]))
print(type((2,3,4,5)))

#-------------------------------------------------------------------------
# [3] → Variables:
#-------------------------------------------------------------------------

myname='Mohamed'    # str
print(myname)
# myname => normal
# myName => camelCase
# my_name => snake_case

age=20            # int
print(age)

gpa=2.7           # float
print(gpa)

x=10
x="Hello"
print(x)      # [will print Hello not 10]

a,b,c=1,2,3
print(a,b,c)  # [will print: 1 2 3]

# No special charactars.
# No numbers as a fisrt character.
# Can't put the variable under the print code.
# Can't use the already used python keywords, to know the python keywords:
help('keywords')

#-------------------------------------------------------------------------
# [4] → Escape sequences characters:
#-------------------------------------------------------------------------

# [ \b ] => to backspace (delete a letter)  
print('Hello \b World')

# [ \n ] => New line
print('Hello \n World')

# [ \t ] => Tab
print('Hello \t World')

# [ \r ] => Carriage return
print('123456 \r abc')

# [ \ ] => Escape space
print('Hello '\
'World')

# [ \\ ] => to add back slash in the output
print('New \\ Old')

# [ \'...\' ] => to add single & double quotes in the output
print('Go \'to\' ')

#-------------------------------------------------------------------------
# [5] → Concatenation:
#-------------------------------------------------------------------------

n1='I love'
n2='Python'

print(n1 + ' ' + n2)
# or
n3= n1 + ' ' + n2
print(n3)

a='I want to say that '
print(a + n3)

print(a + "I'm " + str(20) + " years old" )







# 3 → Math
print(1+1)
print(1-1)
print(1*1)
print(1/1)
print(1%1)
# أكبر - أصغر - يساوي
print(1>1)
print(1<1)
print(1<=1)
print(1>=1)
print(1==1)
# إختصارات
x=10
x+=2       # x=x+2
print(x)
x-=1
print(x)   # x=x-1


# 4 → input
name=input('1. Type your name: ')
print('Your name is: '+ name)
age=input('2. Type your age: ')
print('Your age is: '+str(age))
gpa=input('3. Type your gpa: ')
print('Your gpa is: '+str(gpa))


# 5 → and, or & not
# and
print(10==10 and 10>9)   # Both true → True
# or
print(5<6 or 8>7)    # One true → True
# not
print(not True)
print(not(10>3))   # True → False


# 6 → if, elf, else & nested if
username=input('Enter your usernsme: ')
password=input('Enter your password: ')
# if
if username=='ahmed' and password=='123':
    print('Login successful')
# elif
elif username=='ahmed' or password=='123':
    print('wrong username or password')
#else
else:
    print('wrong username and password')

# nested if
drink=input('What do you want to drink? ')
if drink=='tea':
    sugar=input('With or without sugar? ')
    if sugar=='with'or'without':
        print('Your tea is coming')
if drink=='coffee':
    sugar=input('With or without sugar? ')
    if sugar=='with'or'without':
         print('Your coffee is coming')


# 7 → List
names=['Ahmed','Ali','Mohamed']
print(names[0]) #or print(name[-3])
print(names[1]) #or print(name[-2])
print(names[2]) #or print(name[-1])
# 8 → Tools:    
names.append('Hossam')
names.insert(0,'Seif')
names.remove('Ali')
del names[0]
names.pop(2)


# 9 → Loops (For/While)  التكرار
                         # for .. in range()
for name in range(8):
    print('Smart')
word='python'
for letter in word:
    print(letter)
                         # while ..
i=1
while i<=5:
    print('Mohamed')
    i+=1

# List + Loops
name=['N','V','G']
for S in name:
    print(S)

grades=[24,56,78,98,43,78,95]
no_of_students=0
for b in grades:
    if b>=50:
        no_of_students+=1
print('No. of students passed '+str(no_of_students))

new_grades=[]
for gra in grades:
    bonus=gra+5
    new_grades.append(bonus)
print('New grades= ' + str(new_grades))

# break/continue
i=0
while i<10:
    i+=1
    if i==3:
        continue
    if i==7:
        break
    print('i= ', i)


# 10 → Functions (def)
def greet():
    print('Welcome')
greet()

def n(name,age):
    print('hello',name)
    print('your age is', age)
n('Ahmed',23)

def average(n1,n2,n3):
    total=n1+n2+n3
    ave=total/3
    print('Average is ',ave)
average(30,40,50)

# return
def age():
    return 9
number=age()
print(number) 