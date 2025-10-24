#-------------------------------------------------------------------------
# [1] → print:
#-------------------------------------------------------------------------
print('Hello')
#-------------------------------------------------------------------------
# [2] → Types of data:
#-------------------------------------------------------------------------
print('Mohamed') # String (str)
print(7) # Integer (int)
print(1.5) # Float
print(10==10) # Boolean (bool)
print([1,2,3,4,5]) # List
print((1,2,3,4,5)) # Tuble 
print({'One':1,'Two':2,"Three":3}) # Dict

# To detect the type of data:
print(type(10))
print(type(1.5))
print(type('Stop'))
#-------------------------------------------------------------------------
# [3] → Variables:
#-------------------------------------------------------------------------
myname='Mohamed' # str
print(myname)
# myname => normal
# myName => camelCase
# my_name => snake_case

age=20 # int
print(age)

gpa=2.7 # float
print(gpa)

x=10
x="Hello"
print(x) # [will print Hello not 10]

a,b,c=1,2,3
print(a,b,c) # [will print: 1 2 3]

# Note: Can't use the already used python keywords as a variable, to know the python keywords:
help('keywords')
#-------------------------------------------------------------------------
# [4] → Escape sequences characters:
#-------------------------------------------------------------------------
print('Hello \b World') # To backspace (delete a letter)

print('Hello \n World') # New line

print('Hello \t World') # Tab

print('123456 \r abc') # Carriage return

print('Hello \
World') # Escape space

print('New \\ Old') # To add back slash in the output

print('My name is \"Mohamed\"') # To add single & double quotes in the output
            # Or
print('My name is "Mohamed"')

print('''My
name
is
Mohamed''') # To put every word under each other
#-------------------------------------------------------------------------
# [5] → String methods:
#------------------------------------------------------------------------
print(len('My name is Mohamed')) # Count the number of characters
print('My name is Mohamed'.title()) # Uppercase 1st letter of every word
print('My name is Mohamed'.upper()) # Uppercase all letters
print('My name is Mohamed'.lower()) # Lowercase all letters
print('my name is Mohamed'.capitalize()) # Uppercase 1st letter only
print('My name is Mohamed'.swapcase()) # Swap cases, upper to lower and lower to upper
print('My name is Mohamed'.split()) # Split every word in a form of list
print('   My name is Mohamed   '.strip()) # Delete tabs or any special characters added
print('My name is Mohamed'.center(25)) # Center the string 
print('My name is Mohamed'.count('name')) # Count number of times that the selected word is repeated
print('My name is Mohamed'.startswith()) # Answer by true or false if the inputed letter if the first or not
print('My name is Mohamed'.endswith())  # Answer by true or false if the inputed letter if the last or not
print('1'.zfill(3)) # Puts zeros in front of the number in string
#-------------------------------------------------------------------------
# [6] → String indexing & slicing:
#------------------------------------------------------------------------
# [1] Indexing (Acessing single items):
print('Mohamed'[0]) # M
print('Mohamed'[1]) # o
print('Mohsmed'[-1]) # d

# [2] Slicing (Multible acessing single items):
print('Mohamed'[0:5]) # Moha
print('Mohamed'[:6]) # Moha
print('Mohamed'[0:]) # Mohamed
print('Mohamed'[:]) # Mohamed
print('Mohamed'[0:8:2]) # Mhmd (:2 → number of steps)
#-------------------------------------------------------------------------
# [7] → Concatenation:
#-------------------------------------------------------------------------
word1='I love'
word2='Python'
print(word1+' '+word2)

age=20
print('Your age is: '+str(age))









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