#!/usr/bin/env python3

def admin_login(username, password):
    if username.upper() == "ADMIN" and password == "12345":
        return 'Access granted'
    else:
        return 'Access denied'
    

def hows_the_weather(temperature):
    a=temperature
    if a <40:
        return "It's brisk out there!"
    elif a <66:
        return "It's a little chilly out there!"
    elif a <86:
        return"It's perfect out there!"
    else:
        return "It's too dang hot out there!"

    

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 5==0:
        return "Buzz"
    elif num % 3==0:
        return "Fizz"
    else:
        return num


def calculator(operation, num1, num2):
    a=operation
    if a == '+':
        return num1 + num2
    elif a =="-":
        return num1 - num2
    elif a =="*":
        return num1 * num2
    elif a =="/":
        return num1/num2
    else:
        print("Invalid operation!")
        return None

#Write a function `calculator()` that takes three arguments: an operation and two
#numbers. If the operation is one of the following: `+`, `-`, `*`, or `/`, return
#the value of calling the operation on the two numbers. Otherwise, output a
#message saying "Invalid operation!" and return `None`.


