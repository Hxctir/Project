# Temperature converter project

def Temperature_Converter():

    print('#'*30)
    print('### Temperature converter ####'.center(25))
    print('#'*30)

    while True:
     
     print('-'*30)

     print('1. Celsius to Fahrenheit')
     print('2. Celsius to Kelvin')
     print('3. Fahrenheit to Celsius')
     print('4. Fahrenheit to Kelvin')
     print('5. Kelvin to Celsius')
     print('6. Kelvin to Fahrenheit')
     print('7. Exit')

     print('-'*30)

     try:
      User_operation = int(input('Choose operation: (1 , 2 , 3 , 4 , 5 , 6 , 7 ):\n'))
     
      if User_operation == 7:
        print('Goodbye!')
        break
      
      elif User_operation > 7:
        print('Invalid operation, Please enter numbers between (1-7)')
        continue

      User_temperature = float(input('Enter temperature to convert ( Celsius / Fahrenheit / Kelvin ):\n'))
     except ValueError:
       print('Invalid operation, Please enter numbers only')
       continue
     
     print('-'*30)

     if User_operation == 1:
        print(f'{User_temperature} °C = {(User_temperature * 9/5) + 32:.2f} °F.')

     elif User_operation == 2:
        print(f'{User_temperature} °C = {User_temperature + 273.15:.2f} K.')

     elif User_operation == 3:
        print(f'{User_temperature} °F = {(User_temperature - 32) * 5/9} °C.')

     elif User_operation == 4:
      print(f'{User_temperature} °F = {(User_temperature - 32) * 5/9 + 273.15:.2f} K.')

     elif User_operation == 5:
      print (f'{User_temperature} K = {User_temperature - 273.15:.2f} °C.')

     elif User_operation == 6:
       print(f'{User_temperature} K = {(User_temperature - 273.15) * 9/5 + 32:.2f} °F.')
    
     print('-' * 30)

     Restart_program = input('\nDo want to do another operation? (y/n)\n')
     if Restart_program == 'y':
        continue
     if Restart_program =='n':
        break
     
Temperature_Converter()
     

