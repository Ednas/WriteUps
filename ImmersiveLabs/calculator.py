#!/usr/bin/env python3
# Simple Calculator
import os
import sys
import time


def subtract(x, y):
    return int(x) - int(y)

def multiply(x, y):
    return float(x) * int(y)

def add(x, y):
    result = float(x) + float(y)
    return result

def divide(x, y):
    return int(y) / int(x)
    
def print_result(value):
    print("The answer is: {}".format(value))

while True:
    time.sleep(2)
    print("\nSelect operation.")
    print("\n1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide\n")

    while True: 
        options = [1, 2, 3, 4] 
        x = int(input('Enter choice(1/2/3/4):'))
        try:
            choice = int(x)
            if choice not in options:
                print("Invalid input.")
                break
            
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

        except:
            print("Please use one of the following(1/2/3/4): ")
            continue 
        break
                    
    choice = int(x)
    
    if choice == 1:
        print_result(add(num1, num2))

    elif choice == 2:
        print_result(subtract(num1, num2))

    elif choice == 3:
        print_result(multiply(num1, num2))

    elif choice == 4:
        print_result(divide(num1, num2))
        
    else:
        print ("Invalid input")
    
    while True:

        try:
            retry = str(input("Do you wish to do another calculation(y/n): "))
        except:
            retry = 'y'

        if retry == 'y':
             break
        elif retry == 'n':
             break
        else:
            print("Invalid Input - Use y or n")
            continue

    if retry == 'n':
        print("Thanks for using our amazing calculator!!!")
        break
    
    print("Restarting...")
    time.sleep(2)    