#!/usr/bin/env python
# coding: utf-8

#Radius of the circle


import math as Math
Radius = float (input("Enter the radius of the circle:"))
Area = Math.pi*Radius*Radius
print("The area of the circle is",Area)


#Extension of a given file


filename = input("Enter the Filename: ")
file_extension = filename.split(".")
print ("The extension of the file is :", repr(file_extension[-1]))

