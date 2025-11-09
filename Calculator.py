# Calculator project

def Calculator():

    while True: # To repeat

     print('#'*20)
     print('Calculator'.center(20))
     print('#'*20)

     print(' \n Enter your operation: ')

     First_Number = float(input())
     Operator = (input())
     Seconed_Number = float(input())

     if Operator == '+':
        print(f' Result = {First_Number + Seconed_Number}')

     elif Operator == '-':
        print(f' Result = {First_Number - Seconed_Number}')

     elif Operator == '*':
        print(f' Result = {First_Number * Seconed_Number}')

     elif Operator == '/':
        if Seconed_Number == 0:
           print(' Result = Mathematical Error')
        else:
           print(f' Result = {First_Number / Seconed_Number}')
        
     elif Operator == '%':
        print(f' Result = {First_Number % Seconed_Number}')

     elif Operator == '**':
        print(f' Result = {First_Number ** Seconed_Number}')

     elif Operator == '//':
        print(f' Result = {First_Number // Seconed_Number}')
    
     else:
        print('Invalid operator')


     Calculate_again = input('Calculate again? (y/n)\n').lower()

     if Calculate_again == 'y':
        continue
    
     elif Calculate_again == 'n':
        break

Calculator()