#!/usr/bin/python3
class Square:
     def __init__(self, size):
         self.__size = size  # private instance attribute
         # Example usage:
         # Create an instance of Square with size 5
         square_instance = Square(5)

         # Access the private instance attribute
         print(square_instance._Square__size)
