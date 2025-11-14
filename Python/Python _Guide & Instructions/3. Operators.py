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
