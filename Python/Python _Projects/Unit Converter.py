# Unit Converter project

def lines():
  
  print ( '-' * 30 )

def User_Choice():
  
  print( '#' * 50 )
  print(' Welcome to UNIT CONVERTER! '.center(50,'#'))
  print( '#' * 50)

  lines()

  Convertions = ['1. Length conversion.' ,
                 '2. Weight conversion.' ,
                 '3. Temperature conversion.']
  
  for Convertion in Convertions: 
    print(Convertion)

  lines()

  try:

   User = int(input('\n - What do you want to convert? (Press "0" to exit)\n').strip())

   return User

  except ValueError:
   print('\nPlease enter numbers only.\n')

###############################################################################################################################

# [1]
def Length_Converter():
    
   while True:
    
    lines()

    Systems = ['1. Metric system.' ,
               '2. Imperial system (US).']
    
    for System in Systems:
      print(System)

    lines()

    try:
    
     Choice = int(input('\n - What system do want? (Press "0" to exit.)\n').strip())

     if Choice > len(Systems):
      print('\nPlease choose within given operations.\n')
      continue

     elif Choice == 0:
       print('\nGoodbye!\n')
       break
    
    except ValueError:
      print('\nPlease enter numbers only.\n')
      continue
   
    if Choice == 1:

     while True:

      lines()

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

      lines()
      
      try:

         Metric_Choice = int(input('\n - Choose an operation (Enter "0" to exit):\n').strip())

         if Metric_Choice > len(Metric_Systems):
           print('\nPlease choose within the given operations.\n')
           continue

         Enter_Metric_Number = float(input('\n - Enter length to convert:\n').strip())

      except ValueError:
         print('\nPlease enter numbers only.\n')
         continue

      lines()

      if Metric_Choice == 1:
         print(f'{Enter_Metric_Number:,} mm → {Enter_Metric_Number / 10:,.4f} cm.')
        
      elif Metric_Choice == 2:
         print(f'{Enter_Metric_Number:,} mm → {Enter_Metric_Number / 1000:,.4f} m.')
        
      elif Metric_Choice == 3:
         print(f'{Enter_Metric_Number:,} mm → {Enter_Metric_Number / 1000000:,.4f} km.')

      elif Metric_Choice == 4:
         print(f'{Enter_Metric_Number:,} cm → {Enter_Metric_Number * 10:,.4f} mm.')
        
      elif Metric_Choice == 5:
         print(f'{Enter_Metric_Number:,} cm → {Enter_Metric_Number / 100:,.4f} m.')
        
      elif Metric_Choice == 6:
         print(f'{Enter_Metric_Number:,} cm → {Enter_Metric_Number / 100000:,.4f} km.')
   
      elif Metric_Choice == 7:
         print(f'{Enter_Metric_Number:,} m → {Enter_Metric_Number * 1000:,.4f} mm.')
   
      elif Metric_Choice == 8:
         print(f'{Enter_Metric_Number:,} m → {Enter_Metric_Number * 100:,.4f} cm.')
        
      elif Metric_Choice == 9:
         print(f'{Enter_Metric_Number:,} m → {Enter_Metric_Number / 1000:,.4f} km.')

      elif Metric_Choice == 10:
         print(f'{Enter_Metric_Number:,} km → {Enter_Metric_Number * 1000000:,.4f} mm.')

      elif Metric_Choice == 11:
         print(f'{Enter_Metric_Number:,} km → {Enter_Metric_Number * 100000:,.4f} cm.')

      elif Metric_Choice == 12:
         print(f'{Enter_Metric_Number:,} km → {Enter_Metric_Number * 1000:,.4f} m.')

      lines()

      Restart_Program_1 = input('\nDo you want to enter a new input? (y/n)\n').strip().lower()
      if Restart_Program_1 == 'y':
        continue 
      elif Restart_Program_1 == 'n':
        break

    elif Choice == 2:
   
     while True:

      lines()
   
      Imperial_Systems = ['1. Inch (in) → Foot (ft).' ,
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
            
      for Imperial_System in Imperial_Systems:
        print(Imperial_System)

      lines()

      try:
        Imperial_Choice = int(input('\n - Choose an operation (Enter "0" to exit):\n').strip())

        if Imperial_Choice > len(Imperial_Systems):
          print('\nPlease choose within the given operations.\n')
          continue

        Enter_Imperial_Number = float(input('\n - Enter length to convert::\n').strip())

      except ValueError:
        print('\nPlease enter numbers only.\n')
        continue
      
      lines()
        
      if Imperial_Choice == 1:
         print(f'{Enter_Imperial_Number:,} in → {Enter_Imperial_Number / 12:,.4f} ft.')
        
      elif Imperial_Choice == 2:
         print(f'{Enter_Imperial_Number:,} in → {Enter_Imperial_Number / 36:,.4f} yd.')
        
      elif Imperial_Choice == 3:
         print(f'{Enter_Imperial_Number:,} in → {Enter_Imperial_Number / 63360:,.4f} mi.')

      elif Imperial_Choice == 4:
         print(f'{Enter_Imperial_Number:,} ft → {Enter_Imperial_Number * 12:,.4f} in.')
        
      elif Imperial_Choice == 5:
         print(f'{Enter_Imperial_Number:,} ft → {Enter_Imperial_Number / 3:,.4f} yd.')
        
      elif Imperial_Choice == 6:
         print(f'{Enter_Imperial_Number:,} ft → {Enter_Imperial_Number / 5280:,.4f} mi.')
   
      elif Imperial_Choice == 7:
         print(f'{Enter_Imperial_Number:,} yd → {Enter_Imperial_Number * 36:,.4f} in.')
   
      elif Imperial_Choice == 8:
         print(f'{Enter_Imperial_Number:,} yd → {Enter_Imperial_Number * 3:,.4f} ft.')
        
      elif Imperial_Choice == 9:
         print(f'{Enter_Imperial_Number:,} yd → {Enter_Imperial_Number / 1760:,.4f} mi.')

      elif Imperial_Choice == 10:
         print(f'{Enter_Imperial_Number:,} mi → {Enter_Imperial_Number * 63360:,.4f} in.')

      elif Imperial_Choice == 11:
         print(f'{Enter_Imperial_Number:,} mi → {Enter_Imperial_Number * 5280:,.4f} ft.')

      elif Imperial_Choice == 12:
         print(f'{Enter_Imperial_Number:,} mi → {Enter_Imperial_Number * 1760:,.4f} yd.')

      lines()

      Restart_Program_2 = input('\n - Do you want to enter a new input? (y/n)\n').strip().lower()
      if Restart_Program_2 == 'y':
         continue
      elif Restart_Program_2 == 'n':
         break

# [2]
def Weight_Converter():
  
  while True:
    
    lines()
    
    Units = [ '1. Milligram (mg) → Gram (g).' ,
              '2. Milligram (mg) → Kilogram (kg).' , 
              '3. Milligram (mg) → Ounce (oz).' , 
              '4. Milligram (mg) → Pound (lb).\n' ,

              '5. Gram (g) → Milligram (mg).' , 
              '6. Gram (g) → Kilogram (kg).' ,
              '7. Gram (g) → Ounce (oz).' ,
              '8. Gram (g) → Pound (lb).\n' ,

              '9. Kilogram (kg) → Milligram (mg).' ,
              '10. Kilogram (kg) → Gram (g).' ,
              '11. Kilogram (kg) → Ounce (oz).' ,
              '12. Kilogram (kg) → Pound (lb).\n' ,

              '13. Ounce (oz) → Milligram (mg).' ,
              '14. Ounce (oz) → Gram (g).' ,
              '15. Ounce (oz) → Kilogram (kg).' ,
              '16. Ounce (oz) → Pound (lb).\n' ,

              '17. Pound (lb) → Milligram (mg).' ,
              '18. Pound (lb) → Gram (g).' ,
              '19. Pound (lb) → Kilogram (kg).' ,
              '20. Pound (lb) → Ounce (oz).']
    
    for Unit in Units:
      print(Unit)

    lines()

    try:

      Choice = int(input('\n - Choose an operation (Enter "0" to exit):\n').strip())

      if Choice > len(Units):
        print('\nPlease choose within the given operations.\n')
        continue

      elif Choice == 0:
        print('\nGoodbye!\n')
        break

      Inputed_Weight = float(input('\n - Enter weight to convert:\n').strip())

    except ValueError:
      print('\nPlease enter number only.\n')
      continue
    
    lines()
    
    if Choice == 1:
      print(f'{Inputed_Weight:,} mg → {Inputed_Weight / 1000:,.4f} g')

    elif Choice == 2:
      print(f'{Inputed_Weight:,} mg → {Inputed_Weight / 1000000:,.4f} kg')

    elif Choice == 3:
      print(f'{Inputed_Weight:,} mg → {Inputed_Weight / 28349.5:,.4f} oz')

    elif Choice == 4:
      print(f'{Inputed_Weight:,} mg → {Inputed_Weight / 453592:,.4f} lb')

    elif Choice == 5:
      print(f'{Inputed_Weight:,} g → {Inputed_Weight * 1000:,.4f} mg')

    elif Choice == 6:
      print(f'{Inputed_Weight:,} g → {Inputed_Weight / 1000:,.4f} kg')

    elif Choice == 7:
      print(f'{Inputed_Weight:,} g → {Inputed_Weight / 28.3495:,.4f} oz')

    elif Choice == 8:
      print(f'{Inputed_Weight:,} g → {Inputed_Weight / 453.595:,.4f} lb')

    elif Choice == 9:
      print(f'{Inputed_Weight:,} kg → {Inputed_Weight * 1000000:,.4f} mg')

    elif Choice == 10:
      print(f'{Inputed_Weight:,} kg → {Inputed_Weight * 1000:,.4f} g')

    elif Choice == 11:
      print(f'{Inputed_Weight:,} kg → {Inputed_Weight * 35.274:,.4f} oz')

    elif Choice == 12:
      print(f'{Inputed_Weight:,} kg → {Inputed_Weight * 2.20462:,.4f} lb')

    elif Choice == 13:
      print(f'{Inputed_Weight:,} oz → {Inputed_Weight * 28349.5:,.4f} mg')

    elif Choice == 14:
      print(f'{Inputed_Weight:,} oz → {Inputed_Weight * 28349.5:,.4f} g')

    elif Choice == 15:
      print(f'{Inputed_Weight:,} oz → {Inputed_Weight / 35.274:,.4f} kg')

    elif Choice == 16:
      print(f'{Inputed_Weight:,} oz → {Inputed_Weight / 16:,.4f} lb')
        
    elif Choice == 17:
      print(f'{Inputed_Weight:,} lb → {Inputed_Weight * 453592:,.4f} mg')

    elif Choice == 18:
      print(f'{Inputed_Weight:,} lb → {Inputed_Weight * 453.592:,.4f} g')

    elif Choice == 19:
      print(f'{Inputed_Weight:,} lb → {Inputed_Weight / 2.20462:,.4f} kg')

    elif Choice == 20:
      print(f'{Inputed_Weight:,} lb → {Inputed_Weight * 16:,.4f} oz')

    lines()

    Restart_program = input('\n - Do want to do another operation? (y/n)\n').strip().lower()
    if Restart_program == 'y':
      continue
    elif Restart_program == 'n':
      break

# [3]
def Temperature_Converter():
    while True:
     
     lines()

     Choices = ['1. Celsius to Fahrenheit' ,
                '2. Celsius to Kelvin' ,
                '3. Fahrenheit to Celsius' ,
                '4. Fahrenheit to Kelvin' ,
                '5. Kelvin to Celsius' ,
                '6. Kelvin to Fahrenheit']
     
     for Choice in Choices:
       print(Choice)

     lines()

     try:
      User_operation = int(input('\n - Choose an operation (Enter "0" to exit):\n').strip())

      if User_operation > 7:
        print('\nPlease choose within the given operations.\n')
        continue
     
      elif User_operation == 0:
        print('\nGoodbye!\n')
        break
      
      User_temperature = float(input('\n - Enter temperature to convert:\n').strip())

     except ValueError:
       print('\nPlease enter numbers only.\n')
       continue
     
     lines()

     if User_operation == 1:
        print(f'{User_temperature:,} °C = {(User_temperature * 9/5) + 32:,.2f} °F.')

     elif User_operation == 2:
        print(f'{User_temperature:,} °C = {User_temperature + 273.15:,.2f} K.')

     elif User_operation == 3:
        print(f'{User_temperature:,} °F = {(User_temperature - 32) * 5/9:,.2f} °C.')

     elif User_operation == 4:
      print(f'{User_temperature:,} °F = {(User_temperature - 32) * 5/9 + 273.15:,.2f} K.')

     elif User_operation == 5:
      print (f'{User_temperature:,} K = {User_temperature - 273.15:,.2f} °C.')

     elif User_operation == 6:
       print(f'{User_temperature:,} K = {(User_temperature - 273.15) * 9/5 + 32:,.2f} °F.')
    
     lines()

     Restart_program = input('\n - Do want to do another operation? (y/n)\n').strip().lower()
     if Restart_program == 'y':
        continue
     if Restart_program =='n':
        break

###############################################################################################################################

def Unit_Converter():

   while True:

    User = User_Choice()

    if User == 1:
      Length_Converter()

    elif User == 2:
      Weight_Converter()
     
    elif User == 3:
     Temperature_Converter()

    elif User == 0:
     break

Unit_Converter()