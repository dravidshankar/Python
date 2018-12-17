# -*- coding: utf-8 -*-
"""
Program to illustrate use of class:
    a. Create a class named Car
    b. Define a method "cost" inside the class Car
    c. Print price of the car inside method cost
    d. Create 2 objects of the class Car
    e. Initialize name, year and price with object 
"""
class Car:
    def __init__(self,model,year,price):
        self.model=model
        self.year=year
        self.price=price
    def cost(self):
        print("The price of",self.model,"which is made in",self.year,"is Rs",self.price)
car1=Car("Tiago",2016,600000)#object 1 created
car2=Car("Nexon",2017,800000)
car1.cost()
car2.cost() 
    
    
