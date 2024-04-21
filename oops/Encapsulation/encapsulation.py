#Encapsulation
"""Encapsulation is wrapping up data methods and attributes into a single unit.
(or) combining datamethods and variables into a single class."""
'''it consists of 3 types variables 
public variable it can be accessed any where in the program. Ex: a
protected variable (_a) it can be accessed and modified from outside the class.
private variable (__a) it cannot be accessed or modified outside directly results error.


Encapsulation provides security
we can acheive encapsulation by using Access Specifiers.'''

class Account:
    def __init__(self,mbl_no,acc_no,balance):
        self.mbl_no = mbl_no    # Public attribute (accessible outside the class)
        self._acc_no=acc_no     # Protected attribute (use within the class or subclasses)
        self.__balance=balance  # Private attribute (stronger encapsulation, use with caution)
    def display(self):
        # Print account details in a formatted way (assuming appropriate formatting)
        print(f"Mobile Number: {self.mbl_no}")
        print(f"Account Number: {self._acc_no}")
        print(f"Balance: ${self.__balance:.2f}")  # Format balance with 2 decimal places

obj1=Account(9456,565657567,67)
print(obj1.mbl_no)         
print(obj1._acc_no)
#print(obj1.__balance)
obj1.display()        #by using method we can display the private variable & private variable can only be accessed for the method itself.






#using inheritance
print("-------using inheritance-------")
class account:
    def __init__(self,mbl_no,acc_no,balance):
        self.mbl_no = mbl_no    # Public attribute (accessible outside the class)
        self._acc_no=acc_no     # Protected attribute (use within the class or subclasses)
        self.__balance=balance  # Private attribute (stronger encapsulation, use with caution)
    def display_1(self):
        # Print account details in a formatted way (assuming appropriate formatting)
        print(f"Mobile Number: {self.mbl_no}")
        print(f"Account Number: {self._acc_no}")
        print(f"Balance: ${self.__balance:.2f}")  # Format balance with 2 decimal places
class Bank(account):
    def __init__(self,mbl_no,acc_no,balance):
        super().__init__(mbl_no,acc_no,balance)
    def credit(self):
        super().display_1()
        pass
obj=Bank(9456,565657567,67)
print(obj.mbl_no)         
print(obj._acc_no)         #protected variable can be accessed to inherit.
#print(obj1.__balance)     #private variable cant inherit to next class
obj.display_1()            # we can call the private variable by using the method.




"""We can use setters and getters method to access private methods."""
print("------getters & setters method-------")
class student:
    def __init__(self,name,roll_no,age):
        self.name=name
        self._roll_no=roll_no
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>35:
            print("invalid age given, Age should be less than 35.")
        else:
            self.__age=age
s1=student("nagesh",26,36)
print(s1.name)
print(s1._roll_no)
#print(s1.__age)     #private variable cant be accessed for this we use getters & setters method
s1.set_age(36)
print(s1.get_age())



#private method
class demo:
    def __init__(self,name):
        self.name = name
        self.__display()    #by this way we can access the private method with in the class.
    def __display(self):    #this is a private method we cannot access the method out side the class.
        print(f"Hi, This is my name {self.name}")
d1=demo("Deva")
#d1.__display()

#setter & getter method
print("-----var example-------")
"""Private variables & methods can be used within the class but cant be accessed outside the class."""
class Test(object):
    def __init__(self):
        self.var=10
        self._var1=12
        self.__var2=22
    def get_var2(self):
        return self.__var2
    def setter_var2(self,num):
        self.__var2=num

    def func(self):
        print(self.var)
        print(self._var1)
        print(self.__var2)
    def __func(self):       #private method outside the class we cannot access the method.
        print(self.var)
        print(self._var1)
        print(self.__var2)
if __name__=="__main__":
    t = Test()
    t.func()
    print(t.get_var2())       #returns actual value at __var2
    print(t.setter_var2(33))  #sets new value but doesnt returns anything
    print(t.get_var2())       #again calling get_var2 bcoz it prints with updated value.