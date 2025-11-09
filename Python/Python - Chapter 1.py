#-------------
# Chapter 1:
#-------------
# [1] Variables
# [2] Data types
# [3] Opertators
# [4] Conditional statements
# [5] Loops
# [6] Function

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

# [2] Comparison operators
Comparison_operators = [ '==' , '!=' , '<' , '>' , '<=' , '>=' ]

# [3] Assignment operators
Assignment_operators = [ '=' , '+=' , '-=' , '*=' , '/=' , '%=' , '//='  ]

# [4] Logical operators
Logical_operators = [ 'and' , 'or' , 'not' ]

# [5] Membership operators
Membership_operators = [ 'in' , 'not in' ]

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

