
x = 1
# Global scope

def My_function1():
    global x
    x = 2
    print(x)

def My_function2():
    print(x)
    # Local (function) scope




My_function1() #2
print(x) #2
My_function2() #2