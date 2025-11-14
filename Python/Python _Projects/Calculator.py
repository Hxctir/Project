# Calculator project

def lines():
   print('-' * 30)

def Calculator():
    
   print( '#' * 50 )
   print(' CALCULATOR '.center(50,'#'))
   print( '#' * 50 )

   while True:

     try:
      First_Number = float(input('\n- Enter first number: \n').strip())

      Operator = (input('- Enter operator (+ - * / % ** //):\n').strip())

      Operators = ['+' , '-' , '*' , '/' , '%' ,'**' , '//' ]

      if Operator not in Operators:
         print('Invalid operation, please enter a valid operator.')
         continue

      Seconed_Number = float(input('- Enter second number:\n').strip())
      
      if Operator in ['//','%','/'] and Seconed_Number == 0:
         print('Error, Can\'t divide by 0.')
         continue
     
     except ValueError:
      print('Invalid operation, Please enter numbers only.')
      continue
     
     lines()

     if Operator == '+':
        print(f'{First_Number:,} {Operator} {Seconed_Number:,} = {First_Number + Seconed_Number:,.2f}')

     elif Operator == '-':
        print(f'{First_Number:,} {Operator} {Seconed_Number:,} = {First_Number - Seconed_Number:,.2f}')

     elif Operator == '*':
        print(f'{First_Number:,} {Operator} {Seconed_Number:,} = {First_Number * Seconed_Number:,.2f}')

     elif Operator == '/':
        print(f'{First_Number:,} {Operator} {Seconed_Number:,} = {First_Number / Seconed_Number:,.2f}')
        
     elif Operator == '%':
        print(f'{First_Number:,} {Operator} {Seconed_Number:,} = {First_Number % Seconed_Number:,.2f}')

     elif Operator == '**':
        print(f'{First_Number:,} {Operator} {Seconed_Number:,} = {First_Number ** Seconed_Number:,.2f}')

     elif Operator == '//':
        print(f'{First_Number:,} {Operator} {Seconed_Number:,} = {First_Number // Seconed_Number:,.2f}')
     
     lines()

     Calculate_again = input('\n- Calculate again? (y/n)\n').strip().lower()

     if Calculate_again == 'y':
        continue
    
     elif Calculate_again == 'n':
        break
     
     else:
        print('Invalid input, Exiting..')
        break

Calculator()