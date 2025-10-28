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
#################################################### [27] Full age calculator program (Advanced) #######################################################################
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
############################################################ [28] Membership operators #################################################################################
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




#-------------------------------------------------------------------------
# [ ] → Loops (For/While):
#-------------------------------------------------------------------------
# [1] For:
for number in range(8):
    print(number)  # 0,1,2,3,4,5,6,7,8

word='python'
for letter in word:
    print(letter)

# [2] While:
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