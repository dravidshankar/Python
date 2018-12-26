# -*- coding: utf-8 -*-
"""
Dictionary Datatype
Program to do:
    1. Add books into bookshop 
    2. Sell books from bookshop
"""
bookshop={}#initialize empt dictionary
while True:
    print("Enter any option: 1. Add, 2. Sell, 3. Finish")
    choice=int(input())
    if choice==1:
        title=input("Enter the title of the book")
        if title in bookshop.keys():#check for title
            bookshop[title]+=1#increment the value corresponding to tile
        else:
            bookshop.update({title:1})#update dictionary in case of a new title
        print(bookshop)
    elif choice ==2:
        title=input("Enter the title of the book")
        bookshop[title]-=1#Decerement the book count
        print(bookshop)
    else:
        break
    

    
    
        

