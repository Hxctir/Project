#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
########################################################################## [1] print #################################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

print('Hello Python!')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
######################################################################## [2] Variables #################################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

My_Variable = 'Hello Python!'
print(My_Variable)

# [1] Can include and start with upper (A-Z) and lower (a-z) cases or underscore (_)
# [2] Can include but can't start with numbers (0-9)
# [3] Can't include any special cases (!#$%^&*)
# [4] Cases are sensitive
# [5] Can't use the already used python keywords as a variable name, to know the python keywords:
help('keywords')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
###################################################################### [3] Types of data ##############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# [1] String (str):
My_String = 'Hello Python!'

# [2] Integer (int)
My_Integer = 7

# [3] Float
My_Float = 1.5

# [4] Boolean (bool)
My_Boolean= 1 == 1

# [5] List
My_List = [ 'Python' , 3 , 1.5 ]

# [6] Tuble
My_Tuble = ( 'Python' , 3 , 1.5 )

# [7] Set
My_Set = { 'Python' , 3 , 1.5 }

# [8] Dictionary (dict)
My_Dictionary = {
    'Name':'Osama',
    'Age':'36',
    'Country':'Egypt',
}

# To detect the type of data:
print(type())

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
############################################################################## [4] String ##############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
My_String = 'I love Python'
print(My_String)

# [1] Indexing:
print(My_String[0]) # I
print(My_String[2]) # l
print(My_String[-1]) # n
print(My_String[-2]) # o
# [2] Slicing:
print(My_String[0:7]) # I love
print(My_String[:7]) # I love
print(My_String[7:]) # Python
print(My_String[0:]) # I love Python
print(My_String[:]) # I love Python
print(My_String[0::2]) # Ilv yhn

# To revrse string characters:
print(My_String[::-1]) # nohtyP evol I

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
######################################################################### [5] String methods ###########################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
len() # Count the number of characters
str.title() # Uppercase first character of every word
str.capitalize() # Uppercase first letter of the first word only
str.upper() # Uppercase all characters
str.lower() # Lowercase all characters
str.swapcase() # Swap cases; every uppercase swapped to lowercase and vice versa
str.split() # Split every word in string in form of list
str.splitlines() # Split lines in string in form of list
str.strip() # Delete tabs from both sides (or any special characters added to the brackets)
str.rstrip() # Delete tabs from right side
str.lstrip() # Delete tabs from left side
str.center(10) # Center the string
str.replace('','')
str.count('Python') # Count the number of times that the added word is repeated
str.startswith('P') # Answer by true or false if the added character is the first character or not
str.endswith('n')  # Answer by true or false if the added character is the last character or not
str.index('P') # Search for the order of the addeed character in string (Gives error if not found)
str.find('P') # Search for the order of the added character in string (Doesn't give error if not found, Gives -1)
str.rjust(10,'Python') # Add the added string to your variable from right
str.ljust(10,"Python") # Add the added string to your variable from left
str.expandtabs(2) # Control tabs number
str.isspace()
str.islower()
str.istitle() # Answer by True or False if the selected is title or not
str.isidentifier()
str.isalpha()
str.isalnum()
str.zfill(3) # Puts zeros you choose in front of the number
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#################################################################### [6] Escape sequences characters ###################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# [1] \n
print('I love \n Python')

# [2] \t
print('I \t\t love \t Python') # I         love   Python

# [3] \b
print('I lovee\b\b\b\b\b Python') # I Python

# [4] \r
print('I love \r Python') # Python

# [5] \
print('I love \
 Python') # I love Python

# [6] \\
print('I love Python\\Java') # I love Python\Java

# [7] \"...\"
print('I love \"Python\"') # I love 'Python'

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ###################################################################### [7] Concatenation #############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Concatenation is to add a string to a string using +

My_String1='I love'
My_String2='Python'
print( My_String1 + ' ' + My_String2 )

My_Name='Mohamed'
print('My name is:' + ' ' + My_Name )

My_Age=20
print('My age is:' + ' ' + str(My_Age) )

My_GPA=3.5
print('My GPA is:' + ' ' + str(My_GPA) )

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
####################################################################### [8] String formatting ###########################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# [1] Old formating:

My_Name='Mohamed'
My_Age=20
My_GPA=3.5
print('My Name is: %s, and My Age is: %d, and My GPA is: %f' % ( My_Name , My_Age , My_GPA ))
print('My Name is: %.7s, and my GPA is: %.2f' % (My_Name , My_GPA))

# [2] New formating :

My_Name='Mohamed'
My_Age=20
My_GPA=3.5
print('My Name is: {:s}, and My Age is: {:d}, and My GPA is: {:f}'.format(( My_Name , My_Age , My_GPA )))
print('My Name is: {:7s}, and my GPA is: {:2f}' .format(( My_Name , My_GPA )))

My_Money=1000000
print('I have {:,} dollars in my wallet'.format( My_Money )) # 1,000,000

A,B,C='One','Two',"Three"
print('Hello {}, {}, {}'.format(A,B,C)) # Hell0 One, Two, Three
print('Hello {}, {}, {}'.format(B,A,C)) # Hello Two, One, Three
print('Hello {2}, {0}, {1}'.format(A,B,C)) # Hello Three, One, Two 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

My_Name='Mohamed'
My_Age=20
My_GPA=3.5
print(f'My Name is: {My_Name}, and My Age is: {My_Age}, and My GPA is: {My_GPA}')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
###################################################################### [9] Arithmetic operators ########################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
print(1+1) # 2
print(1-1) # 0
print(1*1) # 1
print(1/1) # 1
print(1%1) # 1
print(2**2) # 8
print(100//20) # 5
print(1>1) # False
print(1<1) # False
print(1<=1) # True
print(1>=1) # True
print(1==1) # True
print(10!=10) # False
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
############################################################################# [10] List ###############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
My_List=['Ahmed','Ali','Mohamed',200,1.5,True]
#Indexing:
print(My_List[0]) # Ahmed
print(My_List[1]) # Ali
print(My_List[2]) # Mohamed
print(My_List[-1]) # True
print(My_List[-2]) # 1.5
# Slicing:
print(My_List[1:4]) # ['Ali','Mohamed','200']
print(My_List[::2]) # ['Ahmed','Mohamed',1.5]
# Editing:
My_List[1]='Adham'
print(My_List[0:])
# Deleting:
My_List[0:2]=[]
print(My_List)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
######################################################################### [11] List methods ###########################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

list.append() # Add the inputed item, if you added a whole list it will be added as a one
list.remove() # Delete the inputed item in the list
list.extend() # Add the inputed item, if you added a whole list it will not be added as a one
list.insert(0,0) # Add the inputed item and insert object
list.sort() # Rarrange the listed numbers or strings from small to large or vice versa
list.reverse() # Reverse list order
list.clear() # Remove all items from list
list.copy() # Make a shallow copy of the inputed list
A = [1,2,3,4,5]
B = A.copy()
print(B)
list.count() # Count number of times of inputed item
list.index() # Count the order of inputed item
list.pop()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
############################################################################# [12] Tuple ###############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
My_Tuble=(1,2,3,4,5)
print(My_Tuble[0]) # 1
print(My_Tuble[3]) # 4
print(My_Tuble[-2]) # 4
# Can't add or delete unlike lists
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
######################################################################## [13] Tuple methods ############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
############################################################################# [14] Set #################################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
My_Set={'L','N','D'}
# Can't index & can't slice
# Items must be unique
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
######################################################################## [15] Set methods ##############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
######################################################################## [15] Dictionary ##############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

User= {
    'Name':'Osama',
    'Age':'36',
    'Country':'Egypt',
    'Skills': ['Python','JavaScript','Java']
}
print(User)

print(User.keys())
print(User.values())
print(User.get('Age'))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
######################################################################## [16] Boolean ##################################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# You ask... and Boolean answer by True or False.

print(bool(1==1)) # True
print(bool(20>10)) # True
print(bool(True)) # True
print(bool('Python')) # True
print(bool([1,2,3])) # True
print(bool((1,2,3))) # True
print(bool({1,2,3})) # True

print(1!=1) # False
print(bool(10>20)) # False
print(bool(0)) # False
print(bool(False)) # False
print(bool('')) # False
print(bool([])) # False
print(bool(())) # False
print(bool({})) # False

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
################################################################### [17] Boolean operators ############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# [1] and :
Name='Mohamed'
Age=20
print(Name=='Mohamed' and Age>18) # True
print(Name=='Mohamed' and Age>30) # False
print(Name=='Omar' and Age>18) # False
print(Name=='Omar' and Age>30) # False

# [2] or :
Name='Mohamed'
Age=20
print(Name=='Mohamed' or Age>18) # True
print(Name=='Mohamed' or Age>30) # True
print(Name=='Omar' and Age>18) # True
print(Name=='Omar' and Age>30) # False

# [3] not :
print(not True) # False
print(not False) # True
ame='Mohamed'
Age=20
print(not Name=='Mohamed' and Age>18) # False
print(not Name=='Mohamed' or Age>30) # False
print(not Name=='Omar' and Age>18) # True
print(not Name=='Omar' and Age>30) # True

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
############################################################### [18] Assginment operators ##############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
x = 10
y = 20

# [1] +=
x = x + y
x += y
print(x) # 30

# [2] -=
x = x - y
y -= x 
print(x) # 10

# [3] *=
x = x * y
y *= x # 10
print(x)

# [4] /=
x = x / y
y /= x # 10
print(x)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
############################################################### [19] Comparison operators ##############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# [1] ==
print(100==100)

# [2] !=
print(100!=100)

# [3] > & <
print(200>100)
print(200<100)

# [4] >= & <=
print(200>=100) 
print(200<=100)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
################################################################# [20] Type conversion #################################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

My_String = 'Python'
My_List = [ 1 , 2 , 3 ]
My_Tuple = ( 1 , 2 , 3 )
My_Set = { 1 , 2 , 3 }
My_Dictionary = { 'One' : 1 , 'Two' : 2 , 'Three' : 3 }

# List
print(list(My_String))
print(list(My_Tuple))
print(list(My_Set))
print(list(My_Dictionary))

# Tuple
print(tuple(My_String))
print(tuple(My_List))
print(tuple(My_Set))
print(tuple(My_Dictionary))

# Set
print(set(My_String))
print(set(My_List))
print(set(My_Tuple))
print(set(My_Dictionary))

# Dict
print(dict(My_String))
print(dict(My_List))
print(dict(My_Tuple))
print(dict(My_Set))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
##################################################################### [21] input #############################################################################@#########
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

First_Name=input('Type your firat name: ').strip().capitalize()
Middle_Name=input('Type your middle name: ').strip().capitalize()
Last_Name=input('Type your last name: ').strip().capitalize()
print(f'Hello {First_Name} {Middle_Name:.1s}. {Last_Name} ! Welcome to our program.')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
##################################################################### [22] Email slicing ###############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

First_Name=input('Type your firat name: ').strip().capitalize()

Email='Mohamed@gmail.com'
print(Email[:Email.index('@')])

Name=input('What\'s your name? ').strip().capitalize()
The_Email=input('What\'s your Email? ').strip().capitalize()
Username=The_Email[:The_Email.index('@')].strip().capitalize()
Domain=The_Email[The_Email.index('@')+1:].strip().capitalize()
print(f'Hello {Name} \n your Email is {The_Email} \n Your Username is {Username} \n your Domain is {Domain}.')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
########################################################### [23] Full age calculator program ###########################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Age=int(input('What\'s your age? ').strip())
Months = Age * 12
Weeks = Months * 4
Days = Age * 365
Hours = Days * 24
Minutes = Hours * 60
Seconds = Minutes * 60

print(f'You lived for: \n {Months:,} months \n {Weeks:,} weeks \
\n {Days:,} days \n {Hours:,} hours \n {Minutes:,} minutes \
\n {Seconds:,} seconds'.title())

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
######################################################## [24] if, elif, else & nested if ###############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

User = input('Username: ').strip().capitalize()
Continent = input('Enter your continent: ').strip()
Product = 'Python course'
Price = 100

print(f'Hello {User}, the course "{Product}" costs ${Price}.')
if Continent == 'Africa' or Continent == 'Asia' :
    IsStudent = input('Are you a student? (Yes/No) ')
    if IsStudent == 'Yes':
       print(f'You have got a 50% Discount (${Price * 0.50})')
    elif IsStudent != 'No':
        print(f'You have got a 30% Discount (${Price * 0.30})')

elif Continent == 'Europe':
    print(f'You have got a 15% Discount (${Price * 0.15})')

else:
    print('No Discount')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
######################################################## [25] Ternary conditional operator #############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

MovieRate = '18'
Age=int(input('Enter your age: '))

print('You are not allowed to watch' if Age < MovieRate else 'You are allowed to watch')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#################################################### [26] Full age calculator program (Advanced) #######################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

print('#'*70)
print(' AGE CALCULATOR '.center(70,'#'))
print('#'*70)

Age=int(input('What\'s your age? ').strip())
Choose=input('What do you want to calculate? \n ( Months / Weeks / Days / Hours / Minutes / Seconds ) ').strip().capitalize()

Months = Age * 12
Weeks = Months * 4
Days = Age * 365
Hours = Days * 24
Minutes = Hours * 60
Seconds = Minutes * 60

print(f'You have lived for "{Months:,}" months.' if Choose == 'Months' else '')
print(f'You have lived for "{Weeks:,}" weeks.' if Choose == 'Weeks' else '')
print(f'You have lived for "{Days:,}" days.' if Choose == 'Days' else '' )
print(f'You have lived for "{Hours:,}" hours.' if Choose == 'Hours' else '' )
print(f'You have lived for "{Minutes:,}" minutes.' if Choose == 'Minutes' else '')
print(f'You have lived for "{Seconds:,}" seconds.' if Choose == 'Seconds'  else '' )

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
############################################################ [27] Membership operators #################################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# if ... in ...:

countries_1 = ['Egypt', 'KSA', 'Palstine','Kuwait']
countries_2 = ['USA', 'Italy','Germany']

Price=100
Discount1 = Price*0.50
Discount2 = Price*0.30

selection = input('Select a country: ')

if selection in countries_1:
    print(f'You got a ${Discount1} discount')

elif selection in countries_2:
    print(f'You got a ${Discount2} discount')

#----------------------------------------------------------------------------------------------------------------

Admins = ['Ahmed', 'Mohamed', 'Osama', 'Mahmoud', 'Rawan','Sama']

Name=input('Please enter your Admin name: ').strip().capitalize()

# VALID name
if Name in Admins:
    print(f'Welcome back {Name}!')
    ChangeName=input('Do you want to update or delete your Admin name? ( update (u) / delete (d) ) = ').strip().capitalize()
    
    # UPDATE option
    if ChangeName == 'Update' or ChangeName == 'U':
        NewName=input('Enter your new Admin name: ')
        print(f'All done! your new Admin name now is "{NewName}"')
        # UPDATING
        Admins[Admins.index(Name)] = NewName
        print(Admins)
    
    # Delete option
    elif ChangeName == 'Delete' or ChangeName == 'D':
        Delete=input('Enter your Admin name to delete: ')
    
        if Delete in Admins:
            print('Admin name is deleted')
            # DELETING
            Admins.remove(Name)
            print(Admins)

        elif Delete not in Admins:
            print('Invalid name, try again')
            
    # No update or delete
    else:
        print('Invalid input')

# INVALID name
elif Name not in Admins:
    Adding=input('You are not an Admin, Do want to add your name as an Admin? ( yes / no ) = ').strip().capitalize()
    if Adding == 'Yes':
        NewAddedName=input('Enter your new name: ')
        print(f'Welcome to Admins "{NewAddedName}"!')
        Admins.append(NewAddedName)
        print(Admins)

    elif Adding == 'No':
        print('No problem')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
########################################################################## [28] Loops: while ###########################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Example 1
Number = 0
while Number < 10: 
    print(Number) # 9
    Number += 1
else: print('Loop is done')

# Example 2
List=[ 'Ahmed' , 'Osama' , 'Hatem' , 'Fares' ]
A = 0
while A < len(List): # 4
    print(f' #{str(A+1).zfill(2)} {List[A]}')
    A += 1

# Example 3
My_Favourite_Webs = []

Maximum_Webs = 5
A = 0
while Maximum_Webs > 0:
    Selected_Web = input('Enter your favourite webs: \n\n https://')
    print(' ')
    My_Favourite_Webs.append(f'https://{Selected_Web.strip().lower()}')
    print(f' #{A+1}: https://{Selected_Web}'.strip().lower())
    print(' ')
    print(f'{Maximum_Webs} place(s) left')
    print(' ')
    A += 1
    Maximum_Webs -= 1

print('Places are full')
print(' ')
if len(My_Favourite_Webs) > 0:
    My_Favourite_Webs.sort()

    index = 0
    while index < len(My_Favourite_Webs):
        print(f'Your favourite web is: {My_Favourite_Webs[index]}')
        index +=1

# Example 4:
Main_Password = 'd'
Input_Password = input('Enter your password: ')
Tries = 5

while Input_Password != Main_Password:
 Tries -= 1
 print(f"{ 'Last' if Tries == 0 else Tries} tries are left.")
 Input_Password = input('Enter your password: ')
 if Tries ==0:
  break  # stop loop
else:
    print('Enter')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
########################################################################## [29] Loops: for #############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Example 1:
numbers = [1,2,3,4,5,6,7,8]
for number in numbers:
    print(number)

# Example 2:
numbers = [1,2,3,4,5,6,7,8]
for number in numbers:
    if number % 2 == 0:
        print(f'{number} is Even')
    elif number % 2 != 0:
        print(f'{number} is odd')

# Example 3:
name = 'Osama'
for letter in name:
    print(letter)

# Example 4:
myRange = range(1,101)
for number in myRange:
    print(number)

# Example 5:
grades = {
    'Ahmed' : 90,
    'Osama' : 80,
    'Mostafa' : 60,
    'Mohamed' : 70,
}
for grade in grades:
    print(f'{grade} : {grades[grade]}')
# or
for key, value in grades.items():
    print(f'{key} : {value}')

# Example 6:
skills = {
    'Skill 1' : input('Enter your skill: ') ,
    'Skill 2' : input('Enter your skill: ') ,
    'Skill 3' : input('Enter your skill: ') ,
}
for skill in skills:
    print(f'{skill} : {skills[skill]}')

# Example 7:
people = ['Ahmed','Farah','Kamel']
skills = ['Html', 'CSS','Java']
for name in people:
    print(f'{name} has skilsl in: ')
    for skill in skills:
        print(f'- {skill}')

# Example 8:
people = {
    'Osama' : {
        'Html' : '70%',
        'JS' : '60%',     
    },
    'Ahmed' : {
        'Html' : '40%',
        'JS' : '20%',
    },
}
for name in people:
    print(f'{name} has skills of:')
    for skill in people[name]:
        print(f'{skill} : {people[name][skill]}')
# or
for key1,value1 in people.items():
    print(f'{key1} :')
    for key2, value2 in value1.items():
        print(f'- {key2} => {value2}')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
########################################################################## [30] continue, break & pass ###############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# continue:
numbers = [1,2,3,5,7,8,9]
for number in numbers:
    if number == 5:
        continue
    print(number)

# break:
numbers = [1,2,3,5,7,8,9]
for number in numbers:
    if number == 5:
        break
    print(number)

numbers = [1,2,3,5,7,8,9]
for number in numbers:
    print(number)
    if number == 5:
        break

# pass:
numbers = [1,2,3,5,7,8,9]
for number in numbers:
    pass

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
########################################################################## [31] Function ###############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def                        => Function keyword (Define)
# Say_Hello                  => Function name
# Name                       => Parameter
# print(f'Hello {name}')     => Task 
# 'Ahmed'                    => Argument

def Say_Hello(name):

    print(f'Hello {name}')

Say_Hello('Ahmed')

# Example 2:
def Adition(A,B):
    
    return A + B

print(Adition(2,1))

# Example 3:
def full_name(first,middle,last):

    print(f'Hello {first} {middle:.1s}. {last}!')

full_name('Mohamed','Tarek','Badran')

# Example 4:
def addition(X,Y):

    if type(X) != int or type(Y) != int:
      print('Only integer allowed')
    else:
      print(int(X)+int(Y))

addition(5,6)

# Example 5:
def show_skills(*skills):

    for skill in skills:
     print(f'your skill are {skill}')

show_skills('g','h','d')


# Default parameters:
def my_function( name , age = '"Unkown"' , country = '"Unkown"' ):
    print(f'Hello {name}, your age is {age} & your country is {country}')

my_function('Mohamed',18)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#################################################################### [32] Function: Args ###############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# *

def my_function(*skills):
    for skill in skills.items():
        print(f'Your skills are: \n {skill}')

my_function( 'Html' , 'CSS' , 'Python')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
################################################################## [33] Function: KWArgs ###############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# **

def my_function(**skills):    
    for key,value in skills.items():
        print(f'Your skills are: \n {key} => {value}')

my_function( Html = '50%' ,  CSS = '40%' , Python = '20%' )

# Args + KWArgs

def show_skills(name, *skills, **skillsW_pro):

     print(f'Hello {name} and your skills are: ')
     for skill in skills:
      print(f'- {skill}')

     print(f'\n Skills with progress are:')
     for key,value in skillsW_pro.items():
         print(f'- {key} => {value}')

show_skills('Mohamed', 'CSS', 'JS', Python = '40%' , Java = '50%')

# Example on simple printing:
myT = ('s','f','k')
myD = { 
 'G':'4',
 'd':'2'
}
print(**myD)
print(*myT)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
################################################################## [34] Function: global & scope #######################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

x = 1
# Global scope

def My_function1():
    print(x)
    # Local (function) scope

def My_function2():
    x = 3
    print(x)
    # Local (function) scope

print(x) #1
My_function1() #1
My_function2() #2


def My_function1():
    global x
    x = 2
    print(x)

def My_function2():
    print(x)
    # Local (function) scope

print(x) #1
My_function1() #2
My_function2() #2


My_function1() #2
print(x) #2
My_function2() #2

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
################################################################## [35] Function: recursion ############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

word = input('Please enter a word: ').lower()

def My_Recursion(word):
    # 1
    if len(word) == 1:
        return word
    # 2
    if word[0] == word[1]:
        return My_Recursion(word[1:])
    # 3
    return word[0] + My_Recursion(word[1:])

print(My_Recursion(word))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
######################################################### [36] Anonoymous function (lambda) ############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Give_name = lambda name : f'Hello "{name}"!'

print(Give_name('Ahmed'))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
######################################################### [37] File handling ############################################################################
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# open():
file = open('File','Mode')

file = open('Mohamed.txt','r') # r = read => default
file = open('Mohamed.txt','w') # w = write
file = open('Mohamed.txt','c') # c = create
file = open('Mohamed.txt','a') # a = append (add values in it)


file = open('Mohamed.txt') # read

# Absolute path : the path from the root of the file to the file spot.
file = open(r'C:\Users\eleman\Mohamed.txt')
# Relative path : the current working directory, the path which Python is standing on.
file = open(r'Mohamed.txt')

#-------------------------------------------------------------------------------------

import os # operating system

print(os.getcwd()) # current working directory, Python location. 

print(os.path.dirname(__file__)) # folder path of searched file

print(os.path.abspath(__file__)) # full root path of searched file

os.chdir() # changes the current working directory
# so:
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())