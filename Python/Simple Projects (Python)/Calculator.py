# Calculator project

def Calculator():
    
   print('#'*25)
   print('###### Calculator #######'.center(20))
   print('#'*25)

   while True:

     try:
      First_Number = float(input('\nEnter first number: '))

      Operator = (input('Enter operator (+ - * / % ** //): '))
      Operators = ['+' , '-' , '*' , '/' , '%' ,'**' , '//' ]
      if Operator not in Operators:
         print('Invalid operation, please enter a valid operator.')
         continue

      Seconed_Number = float(input('Enter second number: '))
      
      if Operator in ['//','%','/'] and Seconed_Number == 0:
         print('Error, you can\'t divide by 0')
         continue
     
     except ValueError:
      print('Invalid operation, Please enter numbers only.')
      continue
     
     print('-'*20)

     if Operator == '+':
        print(f'Result = {First_Number + Seconed_Number:.2f}')

     elif Operator == '-':
        print(f'Result = {First_Number - Seconed_Number:.2f}')

     elif Operator == '*':
        print(f'Result = {First_Number * Seconed_Number:.2f}')

     elif Operator == '/':
        print(f'Result = {First_Number / Seconed_Number:.2f}')
        
     elif Operator == '%':
        print(f'Result = {First_Number % Seconed_Number:.2f}')

     elif Operator == '**':
        print(f'Result = {First_Number ** Seconed_Number:.2f}')

     elif Operator == '//':
        print(f'Result = {First_Number // Seconed_Number:.2f}')
     
     print('-'*20)

     Calculate_again = input('\nCalculate again? (y/n)\n').lower()

     if Calculate_again == 'y':
        continue
    
     elif Calculate_again == 'n':
        break
     
     else:
        print('Invalid input, Exiting..')
        break

Calculator()