# This is the logic part of our project
# We create "Functions" which are like little recipes for math

def add(x, y):
    """Adds two numbers together"""
    return x + y

def subtract(x, y):
    """Takes the second number away from the first"""
    return x - y

def multiply(x, y):
    """Multiplies two numbers"""
    return x * y

def divide(x, y):
    """Divides the first number by the second"""
    # We must check if y is zero so the computer doesn't get confused!
    if y == 0:
        return "Error: You cannot divide by zero!"
    return x / y