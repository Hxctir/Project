print('Hello')


# Variables
#1
A='yes'
print(A)
B='no'
print(B)
#2
name="Mohamed"
nickname="Tarek"
print(name)
print(nickname)
#3
name_of_student='Ahmed'
print(name_of_student)


# Comments:
# زي كدة


# Inetger (int) أرقام صحيحة
age=20
print(age)
# Float أرقام كسرية
gpa=2.7
print(gpa)
# String (str) نصوص
name='\'Mohamed\''      #  " \"Mohamed\" " = "Mohamed"
print('Hello',name)
print('my age is',age)
print('Hello\n My name is Mohamed')      #  /n  قبل الكلمة بتنزلها سطر 
# Boolean
result1=(10==10)   #   ==
result2=(20>30)   #   >
result3=(30>=20) #   >=
result4=(10!=3)  #   !=
print(result1)


# معاملات حسابية
X=1
Y=2
print(X+Y)
print(X-Y)
print(X*Y)
print(X/Y)
print(X%Y) #   % = modulus
print(10%10) # 0
print(10%20) # الصغير
print(20%10) # 20-10=10 , 10-10=0


name='Mohamed'
age=20
gpa=2.7
print('My name is ' + name.upper() , ', my age is '+ str(age), '& my gpa is '+ str(gpa) )
# .type()
# .str()
# .upper()
# .lower()
# .title()
# .capitalize()


# تحكم المستخدم
print('Enter your name')
User=input()
print("Your name is "+User)

print('Enter your age')
User2=int(input())
print('Your age is '+ str(User2))

print('Enter your gpa')
gpa = float(input())
print('Your gpa is '+ str(gpa))


# إختصارات في العمليات الحساسبية
x=10
x+=10
print(x)
x-=20
print(x)


# and
# or
# not
print(10>=10 and 10>5)
print(10>11 or 5>6)
print(not True)
print(not(10>3))


# if
password=input('Enter your password\n')
if password==12345:
    print('Your password is true')
else:
    print('Your password is wrong')
# elif
# else
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


username=input('Enter your usernsme: ')
password=input('Enter your password: ')

if username=='ahmed' and password=='123':
    print('Login successful')
elif username=='ahmed' or password=='123':
    print('wrong username or password')
else:
    print('wrong username and password')

# List
names=['Ahmed','Ali','Mohamed']
print(names[0]) #or print(name[-3])
print(names[1]) #or print(name[-2])
print(names[2]) #or print(name[-1])

# Tools:    
names.append('Hossam')
names.insert(0,'Seif')
names.remove('Ali')
del names[0]
names.pop(2)

