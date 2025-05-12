#global variable 
a=20
b=30
def sum():
    #defining a function
    a=10
    #this is local variable
    b=50
    #this is local variable
    e=a+b
    print(e)
sum()
#calling a function
#from this case we get that priority of the local variable is more than that of global variable