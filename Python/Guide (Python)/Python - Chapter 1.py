
###############################################################
########################## Chapter 1 ##########################
###############################################################
#--------------------------------------------------------------
# [1] Variables
#--------------------------------------------------------------

#--------------------------------------------------------------
# [2] Data types:
#--------------------------------------------------------------
    # [1] String (str)
         # Text manipulation:
             # Indexing
             # Slicing
             # Escape sequence
             # Concatenation
             # Formatting
             # Methods

    # [2] Integer (int)

    # [3] Float

    # [4] Boolean

    # [5] Collection data:

         # [1] List
             # Methods

         # [2] Tuple
             # Methods

         # [3] Set
             # Methods

         # [4] Dict
             # Methods

#--------------------------------------------------------------
# [3] Opertators:
#--------------------------------------------------------------
     # [1] Arithmetic operators
     # [2] Comparison operators
     # [3] Assignment operators
     # [4] Logical operators
     # [5] Membership operators
     # [6] Identitiy operators

#--------------------------------------------------------------
# [4] Conditional statements:
#--------------------------------------------------------------
     # if / elif / else
     # Nested if
     # Ternary conditional operators

#--------------------------------------------------------------
# [5] Loops:
#--------------------------------------------------------------
     # for / while
     # continue / break / pass
     # Loops + Collection data
     # Nested loop

#--------------------------------------------------------------
# [6] Function:
#--------------------------------------------------------------
     # def
     # return
     # Parameters / Arguments
     # Default / Keyword / Variable-length (*args & **kwargs) Arguments
     # Scope (Local) / Global Variables
     # Lambda function 

#--------------------------------------------------------------

#########################################
############# [1] Variables #############
#########################################

Greet = 'Hello Python!'
print(Greet)

##########################################
############# [2] Data types #############
##########################################

# [1] String (str)
str
String = 'This is a string'

#---------------------------------------------------

# [2] Integer (int)
int
Integer = 10

#---------------------------------------------------

# [3] float
float
Float = 5.5

#---------------------------------------------------

# [4] Boolean (bool)
bool
Boolean = 'House' == 'Mouse'

#---------------------------------------------------

# [5] Collection data:
list
List = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]

tuple
Tuple = ( 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 )

set
Set = { 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 }

dict
Dict = {
    'Name' : 'Mohamed' ,
    'Age' : 20
}

##########################################
############# [3] Opertators #############
##########################################

# [1] Arithmetic operators:
Arithmetic_operators = [ '+' , '-' , '*' , '/' , '%' , '**' , '//'  ]
#---------------------------------------------------
# [2] Comparison operators

Comparison_operators = [ '==' , '!=' , '<' , '>' , '<=' , '>=' ]
#---------------------------------------------------
# [3] Assignment operators

Assignment_operators = [ '=' , '+=' , '-=' , '*=' , '/=' , '%=' , '//='  ]
#---------------------------------------------------
# [4] Logical operators

Logical_operators = [ 'and' , 'or' , 'not' ]
#---------------------------------------------------
# [5] Membership operators

Membership_operators = [ 'in' , 'not in' ]

print('in' in Membership_operators)
print('not in' not in Membership_operators)

# Example:

Countries = ['Spain','England','France','Germany','Italy']
UserCountry = input('Enter your country: ')

if UserCountry in Countries:
    print('You have a discount!')

elif UserCountry not in Countries:
    print('No discount')
#---------------------------------------------------

# [6] Identitiy operators
Identitiy_operators = [ 'is' , 'not is' ]

######################################################
############# [4] Conditional statements #############
######################################################

Variables = [1 , 2 , 3 , 4 , 5]

# [1] if
if Variables[0] == 2:
    print('False')

# [2] elif
elif Variables[1] == 2 :
    print('True')

# [3] else
else:
    print('Variables')

#---------------------------------------------------
# [3] Ternary conditional operators

Required_age = 18
User_age = int(input('Enter your age: '))

print('You can\'t enter the website' if User_age < Required_age else 'You can enter')

#####################################
############# [5] Loops #############
#####################################

# [1] for
Variables = [1 , 2 , 3 , 4 , 5]

for Variable in Variables:
    print(Variable)

# [2] while
Times = 0
while Times < 6:
    print('Ok')
    Times += 1

########################################
############# [6] Function #############
########################################

def Function():
    variable_1 = 'My name is '
    variable_2 = input('Enter your name: ')
    variable_3 = variable_1 + variable_2
    return variable_3

Name = Function()
print(Name)

