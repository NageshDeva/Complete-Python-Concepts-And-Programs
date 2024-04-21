#DECORATOR
'''Decorator is a function which takes a function as argument and extend its functionality
and returns modified function with extended functionality'''


'''The main objective of decorator function we extend functionality of existing functions without modifies that function.'''
def division(a,b):
    print(a/b)


def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div = smart_div(division)
div(2,4)

#login Required!!

def login_required(func):      #decorator function with func parameter & it can be any calling function

    def inner(name,is_login):     #implementing new functionality
        if is_login == False:
            print("please Login!")
            return
        return func(name, is_login)      
    return inner

@login_required                  #decorator
def home(name,is_login):
    print("welcome to home page of our website!")

@login_required                   #decorator
def orders(name,is_login):
    print("welcome to orders page of our website")

def about():
    print("welcome to about section of our website")



home("Deva",False)      #calling function
orders("deva",True)    
about()
