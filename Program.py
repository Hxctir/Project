# 1 → print
print('Hello')


#2 → variables
name='Mohamed'    # str
print(name)
age=20            # int
print(age)
gpa=2.7           # float
print(gpa)


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


# 9 → Loops  التكرار
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

