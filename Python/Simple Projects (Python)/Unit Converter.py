
# Unit Converter project

def User_Choice():
  
  print('-'*30)
  
  Convertions = ['1. Length' ,
                 '2. Weight' ,
                 '3. Temperature']
  
  for Convertion in Convertions: 
    print(Convertion)

  print('-'*30)

  try:

   global User

   User = int(input('\nWhat do you want to convert? (Press "0" if you want to exit)\n'))

  except ValueError:
   print('\nPlease enter numbers only')

###############################################################################################################################

# [1]
def Length_Converter():
    
   while True:
    
    print('-'*30)

    Systems = ['1. Metric system.' ,
               '2. Imperial system (US).']
    
    for System in Systems:
      print(System)

    print('-'*30)

    try:
    
     Choice = int(input('\nWhat system do want? (Press "0" if you want to exit.)\n'))
    
    except ValueError:
      print('Please enter numbers only.')
      continue
   
    if Choice == 1:

     while True:

      print('-'*30)

      Metric_Systems = ['1. Millimeter (mm) → Centimeter (cm).' ,
                        '2. Millimeter (mm) → Meter (m).' ,
                        '3. Millimeter (mm) → Kilometer(km).\n' ,

                        '4. Centimeter (cm) → Millimeter (mm),' ,
                        '5. Centimeter (cm) → Meter (m),' ,
                        '6. Centimeter (cm) → Kilometer(km).\n' ,

                        '7. Meter (m) → Millimeter (mm).' ,
                        '8. Meter (m) → Centimeter (cm).' ,
                        '9. Meter (m) → Kilometer(km).\n' ,

                        '10. Kilometer(km) → Millimeter (mm).' ,
                        '11. Kilometer(km) → Centimeter (cm).' ,
                        '12. Kilometer(km) → Meter (m).']

      for Metric_System in Metric_Systems:
        print(Metric_System)

      print('-'*30)
      
      try:
         Metric_Choice = int(input('\nWhat convertion do you want to do?\n'))
         if Metric_Choice > 12:
           print('Please enter numbers within (1-12).')
           continue

         Enter_Metric_Number = float(input('\nEnter your length:\n'))

      except ValueError:
         print('\nPlease enter numbers only.')
         continue

      if Metric_Choice == 1:
         print(f'{Enter_Metric_Number} mm → {Enter_Metric_Number / 10:.4f} cm.')
        
      elif Metric_Choice == 2:
         print(f'{Enter_Metric_Number} mm → {Enter_Metric_Number / 1000:.4f} m.')
        
      elif Metric_Choice == 3:
         print(f'{Enter_Metric_Number} mm → {Enter_Metric_Number / 1000000:.4f} km.')

      elif Metric_Choice == 4:
         print(f'{Enter_Metric_Number} cm → {Enter_Metric_Number * 10:.4f} mm.')
        
      elif Metric_Choice == 5:
         print(f'{Enter_Metric_Number} cm → {Enter_Metric_Number / 100:.4f} m.')
        
      elif Metric_Choice == 6:
         print(f'{Enter_Metric_Number} cm → {Enter_Metric_Number / 100000:.4f} km.')
   
      elif Metric_Choice == 7:
         print(f'{Enter_Metric_Number} m → {Enter_Metric_Number * 1000:.4f} mm.')
   
      elif Metric_Choice == 8:
         print(f'{Enter_Metric_Number} m → {Enter_Metric_Number * 100:.4f} cm.')
        
      elif Metric_Choice == 9:
         print(f'{Enter_Metric_Number} m → {Enter_Metric_Number / 1000:.4f} km.')

      elif Metric_Choice == 10:
         print(f'{Enter_Metric_Number} km → {Enter_Metric_Number * 1000000:.4f} mm.')

      elif Metric_Choice == 11:
         print(f'{Enter_Metric_Number} km → {Enter_Metric_Number * 100000:.4f} cm.')

      elif Metric_Choice == 12:
         print(f'{Enter_Metric_Number} km → {Enter_Metric_Number * 1000:.4f} m.')

      Restart_Program_1 = input('\nDo you want to enter a new input? (y/n)\n')
      if Restart_Program_1 == 'y':
        continue 
      elif Restart_Program_1 == 'n':
        break

    elif Choice == 2:
   
     while True:

      print('-'*30)
   
      imperial_Systems = ['1. Inch (in) → Foot (ft).' ,
                        '2. Inch (in) → Yard (yd).' ,
                        '3. Inch (in) → Mile (mi).\n' ,

                        '4. Foot (ft) → Inch (in).' ,
                        '5. Foot (ft) → Yard (yd).' ,
                        '6. Foot (ft) → Mile (mi).\n' ,

                        '7. Yard (yd) → Inch (in).' ,
                        '8. Yard (yd) → Foot (ft).' ,
                        '9. Yard (yd) → Mile (mi).\n' ,

                        '10. Mile (mi) → Inch (in).' ,
                        '11. Mile (mi) → Foot (ft).' ,
                        '12. Mile (mi) → Yard (yd).']
            
      for Imperial_System in imperial_Systems:
        print(Imperial_System)

      print('-'*30)

      try:
        Imperial_Choice = int(input('What convertions do you want to do?\n'))
        if Imperial_Choice > 12:
          print('Please enter numbers within (1-12).')
          continue

        Enter_Imperial_Number = float(input('Enter your length:\n'))

      except ValueError:
        print('Please enter numbers.')
        continue
      
      if Imperial_Choice == 1:
         print(f'{Enter_Imperial_Number} in → {Enter_Imperial_Number / 12:.4f} ft.')
        
      elif Imperial_Choice == 2:
         print(f'{Enter_Imperial_Number} in → {Enter_Imperial_Number / 36:.4f} yd.')
        
      elif Imperial_Choice == 3:
         print(f'{Enter_Imperial_Number} in → {Enter_Imperial_Number / 63360:.4f} mi.')

      elif Imperial_Choice == 4:
         print(f'{Enter_Imperial_Number} ft → {Enter_Imperial_Number * 12:.4f} in.')
        
      elif Imperial_Choice == 5:
         print(f'{Enter_Imperial_Number} ft → {Enter_Imperial_Number / 3:.4f} yd.')
        
      elif Imperial_Choice == 6:
         print(f'{Enter_Imperial_Number} ft → {Enter_Imperial_Number / 5280:.4f} mi.')
   
      elif Imperial_Choice == 7:
         print(f'{Enter_Imperial_Number} yd → {Enter_Imperial_Number * 36:.4f} in.')
   
      elif Imperial_Choice == 8:
         print(f'{Enter_Imperial_Number} yd → {Enter_Imperial_Number * 3:.4f} ft.')
        
      elif Imperial_Choice == 9:
         print(f'{Enter_Imperial_Number} yd → {Enter_Imperial_Number / 1760:.4f} mi.')

      elif Imperial_Choice == 10:
         print(f'{Enter_Imperial_Number} mi → {Enter_Imperial_Number * 63360:.4f} in.')

      elif Imperial_Choice == 11:
         print(f'{Enter_Imperial_Number} mi → {Enter_Imperial_Number * 5280:.4f} ft.')

      elif Imperial_Choice == 12:
         print(f'{Enter_Imperial_Number} mi → {Enter_Imperial_Number * 1760:.4f} yd.')

      Restart_Program_2 = input('\nDo you want to enter a new input? (y/n)\n')
      if Restart_Program_2 == 'y':
         continue
      elif Restart_Program_2 == 'n':
         break

    elif Choice == 0:
      break
    
    else:
      print('Please choose within (1-2).')
      continue

# [2]
def Weight_Convertor():
  pass

# [3]
def Temperature_Converter():
    while True:
     
     print('-'*30)

     Choices = ['1. Celsius to Fahrenheit' ,
                '2. Celsius to Kelvin' ,
                '3. Fahrenheit to Celsius' ,
                '4. Fahrenheit to Kelvin' ,
                '5. Kelvin to Celsius' ,
                '6. Kelvin to Fahrenheit' ,
                '7. Exit']
     
     for Choice in Choices:
       print(Choice)

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

###############################################################################################################################

def Unit_Converter():

   while True:

    User_Choice()

    if User == 1:
      Length_Converter()

    elif User == 2:
     pass

    elif User == 3:
     Temperature_Converter()

    elif User == 0:
     break

Unit_Converter()