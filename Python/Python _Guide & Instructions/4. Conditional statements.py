
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
