#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Q1 using generator comprehension
def mulrange(num):
    return (i*num for i in range(1,11))

inp_num = int(input("Enter number: "))
for i in mulrange(inp_num):
    print(i)


# In[13]:


#Q1 without using generator comprehension
def mulrange(num):
    i=1
    while(True):
        yield i*num
        i+=1
        if(i>=11): return

inp_num = int(input("Enter number: "))
for i in mulrange(inp_num):
    print(i)


# In[22]:


#Q2(a)Custom Error implemented using class
class UserNotFound(Exception):
    pass

def start():
    try:
        raise UserNotFound
    except UserNotFound as e:
        print("User Not Found Exception")
    else:
        print('The Code was executed without an error.')
    finally: 
        print("The Code in Finally Block is always executed.") 

start()


# In[39]:


#Q2(b)Custom Error using Exception or BaseException 
def start(n):
    try:
        if n >5:
            raise BaseException("The Input is Greater than 5 so it cannot be processed.")
        elif n<0:
            raise Exception("The Input is Negative Exception")
    except BaseException as e:
        print(e)
    else:
        
        print(f'{n} is the input which is in range 0-5.')
    finally: 
        print("The Code in Finally Block is always executed.") 

start(3)


# In[56]:


#Q2(c)full-fledged case for exception handling using try, except, else, finally

class CannotDivideException(Exception):
    pass
def divide(num1,num2):
    try:
        if num1 < 0 or num2 < 0:
            raise Exception("Cannot Divide Exception, Negative Case")
        result = num1/num2
    except ZeroDivisionError:
         print("Sorry ! You are dividing by zero ")
    except CannotDivideException as e:
        print("Exception: "+ e)
    else:
        print('Division was normally executed with result: '+ str(result))
    finally: 
        result = None
        print("Cleanup task") 

num1 = int(input("Enter Number to be divided"))
num2 = int(input("Enter Divisor "))
divide(num1,num2)


# In[98]:


#Q3
class Animal:
    hasLegs = 4
    
    def __init__(self, name, animal):
        self.name = name
        self.animal = animal
        
    def __str__(obj):
        return f"{obj.name} is an {obj.animal} Animal"
    
    def getDetails(self):
        return f"{self.name} is {self.age} years old"
    
    def sound(self):
        return f"{self.name} has a sound like {self.sound}"
    
    @classmethod 
    def usingString(cls, string):
        name,animal = string.split(',')
        return cls(name,animal)
    

class Dog(Animal):
    def __init__(self, name, animal, age):
        super().__init__(name,animal);
        self.age=age
        self.__sound = "Bark"
        
    @staticmethod
    def isVaccinated(age):
        return age>2 
    
class GermanSephard(Dog, Animal):

    def __str__(obj):
        return f"{obj.name} is an German Sephard with the {obj.eye} color of eye."
    
    @property
    def about(self):
        return self.name+','+self.animal+","+self.eye+", "+self.color
    
    @about.setter
    def about(self, about):
        self.color,self.eye = about.split(',')

class JapneseSpitz(Dog, Animal):
    pass


    


# In[101]:


bruno = Animal("Bruno", "Domestic")
print(bruno)

#(a)object declaration using @classmethod decorator
kali = Animal.usingString("Kali, Wild")
print(kali)


# In[104]:



#(b)static method example
khaire = Dog("Khaire", "Domestic", "4")
khaire.isVaccinated(2)


# In[105]:



#(c)@property and setter for it
shere = GermanSephard("Shere", "Domestic", "5")
shere.eye = "black"

#the below is @property decorator setter method
#this sets the color of German Sephard
shere.about = "Brown, Black"

#this is @property getter with about method which prints all the details
print(shere.about)


# In[111]:


#(d)class variable example
Animal.hasLegs

bruno = Animal("Bruno", "Domestic")
bruno.hasLegs

khaire = Dog("Khaire", "Domestic", "4")
khaire.hasLegs


# In[149]:


import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
    
    def __add__(self, other):     
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __iadd__(self, other):
        self.real += other.real
        self.imaginary += other.imaginary
        return Complex(self.real, self.imaginary) 

    def __lt__(self, other):
        self_mod = math.sqrt(self.real**2 + self.imaginary**2)
        other_mod = math.sqrt(other.real**2 + other.imaginary**2)
        return self_mod>other_mod
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real, self.imaginary * other.imaginary)

    def __truediv__(self, other):
        return Complex(self.real / other.real, self.imaginary /other.imaginary)

    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0)
    
    def __eq__(self, other):
        if self.real==other.real and self.imaginary==other.imaginary:
            return "both complex numbers are equal"
        else:
            return "both complex numbers are not equal"

x = Complex(2,1)
y = Complex(5,6)
z = Complex(2,1)

print(x+y)

print(x==z)

x+=z
print(x)

#to compare two complex numbers, we calculate their modulus value and compare them
y>z
z>y








