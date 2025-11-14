# [1] Loop for Dict:

Grades = {
  'Mohamed' : '70' ,
  'Ahmed' : '80' ,
  'Mahmoud' : '90' ,
  'Rawan' : '95' ,
  'Salma' : '85'
}

for Name, Grade in Grades.items():
  print(f'{Name} : {Grade} ')

print('-'*20)

Grades = {
  'Mohamed' : {
     'Math' : '70' ,
     'Physics' : '70'} ,

   'Ahmed' : {
     'Math' : '80' ,
     'Physics' : '90'}
  }

for Name , Subject_Degree in Grades.items():
  
  for Subject , Grades in Subject_Degree.items():
    print(f' {Name} got {Grades} in {Subject} ')

#---------------------------------------------------------

# [2] Function lambda

say_hello = lambda name : f'Hello {name}'
print(say_hello('Ahmed'))

#---------------------------------------------------------

# [3] Membership operators (in / not in)

#---------------------------------------------------------

# [4] Ternanry Conditional operators

List = [1,2,3,4,5,6,7,8,9]

print('Ok' if 2 in List else '')

#---------------------------------------------------------

# [5] Args (*) & KWArgs (**)

List = [1 , 2 , 3 , 4 , 5 ]
print(*List)

# Args (*): => Tuples
def Hello(*Names):
  
  for Name in Names:
    print(f'Hello {Name}')

Hello('Ahmed','Mohamed','Sami')

# KWArgs (**): => Dicts
def Hello(**Names):
  
  for Name , Skill in Names.items():
    print(f'Hello {Name} you have {Skill} skill.')

Hello( Ahmed ='Python',
       Mohamed ='CSS')

#---------------------------------------------------------

while True:

 first_number = int(input())
 second_number = int(input())

 if type(first_number) != int or type(second_number) != int:
   print('Invalid')
   continue

 else:
   print(first_number + second_number)






# Modules

#import random

#print(f'Random Numbers: {random.random()}')

# To show all functions in a module

# print(dir(random))

#from random import randint , randrange
#print(randint(10,900))
#print(randrange(20,100))

#Numbers = [5,5.48]
#print(sum(Numbers , 20)) 
# 5 + 5 = 10
# 10 + 20 = 30

#print(round(5.51 , 2))

#List = []
#for i in range(2):
    #Numbers = int(input('Enter numbers: '))
 #   List.append(Numbers)

#print(sum(List))

#Names = ['Ahmed', 'Sami']

#from random import choice
#print(choice(Names))


#Lists3 = list(range(1,11))

#for List in Lists3:
    #print(List)

#Numbers = [30 , 40]

#Total = 0
#for Number in Numbers:
   # Total += Number

#print(Total)

# Nu = []

#for i in range(3):
 #   Input = input()
  #  Nu.append(Input)

#print(Nu)

#numbers = []

#for i in range(3):
   # num = int(input("Enter a number: "))
   # numbers.append(num)

#print(numbers)

#print('Hello'  , 'World', sep = '       ')
#print('Hello World', end = '  rrrr ')

def lines():
  
  print ( '-' * 30 )

lines()